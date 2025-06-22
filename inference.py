from picamera2 import Picamera2
from picamera2.encoders import H264Encoder, Quality
from picamera2.outputs import FfmpegOutput
import cv2
from pycoral.adapters import common, detect
from pycoral.utils.edgetpu import make_interpreter
from time import sleep, time
from datetime import datetime

class InferenceController():
    def __init__(self):
        # Initialize Coral
        self.interpreter = make_interpreter('models/ssd_mobnet2/ssd_mobnet2_tf2.tflite')
        self.interpreter.allocate_tensors()
        self.size = common.input_size(self.interpreter)

        # Initialize Camera
        self.camera = Picamera2()
        self.preview_config = self.camera.create_preview_configuration({'format': 'RGB888'})
        self.video_encoder = H264Encoder()

        self.video_config = self.camera.create_video_configuration(main={"size": self.size}, encode="main")
        self.video_fps = 30.0
        self.still_config = self.camera.create_still_configuration({"size": self.size})

        self.camera.configure(self.preview_config)
        self.camera.set_controls({"FrameRate": self.video_fps})
        self.camera.start()
        sleep(2) 

    def take_and_infer_still(self):
        self.camera.switch_mode(self.still_config)
        
        frame = self.camera.capture_array()
        processed_frame = self.process_frame(frame)

        cv2.imwrite(f"/home/pi/drone/images/{datetime.today().strftime('%Y-%m-%d_%H-%M-%S')}.jpg", processed_frame)
        print("Image processed and saved!")

    # TODO: Processing stream with a smaller model works, but video looks like it runs at double playback speed
    def record_video(self):
        self.camera.switch_mode(self.still_config)
        out = cv2.VideoWriter(f"/home/pi/drone/videos/{datetime.today().strftime('%Y-%m-%d_%H-%M-%S')}.avi", cv2.VideoWriter_fourcc(*'XVID'), self.video_fps, self.size)
        
        frame_time = 1.0 / self.video_fps

        try: 
            while True:
                start = time()

                frame = self.camera.capture_array()
                processed_frame = self.process_frame(frame)
                out.write(frame)

                elapsed = time() - start
                if elapsed < frame_time:
                    sleep(frame_time - elapsed)

        except KeyboardInterrupt:
            self.close()
            out.release()

    def close(self):
        self.camera.close()

    # TODO: Create dynamic file names in a dedicated directory
    def infer_video(self):
        cap = cv2.VideoCapture("test.mp4")
        out = cv2.VideoWriter("inferred.avi", cv2.VideoWriter_fourcc(*'XVID'), self.video_fps, self.size)
        
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                print("Exiting post-processing...")
                break

            processed_frame = self.process_frame(frame)

            out.write(processed_frame)
        
        cap.release()
        out.release()
        print("Successfully exited.")

    def process_frame(self, frame, video=False):
        common.set_input(self.interpreter, frame)
        self.interpreter.invoke()

        objects = detect.get_objects(self.interpreter, score_threshold=0.5)

        for obj in objects:
            bbox = obj.bbox
            cv2.rectangle(frame, (bbox.xmin, bbox.ymin), (bbox.xmax, bbox.ymax), (0, 255, 0), 2)
            cv2.putText(frame, f'{obj.id} {obj.score:.2f}', (bbox.xmin, bbox.ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return frame