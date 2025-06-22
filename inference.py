# TODO: Refactor to absolute paths

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder, Quality
from picamera2.outputs import FfmpegOutput
import cv2
from pycoral.adapters import common, detect
from pycoral.utils.dataset import read_label_file
from pycoral.utils.edgetpu import make_interpreter
from time import sleep, time
from datetime import datetime

class InferenceController():
    def __init__(self):
        # Initialize Coral
        self.still_interpreter = make_interpreter("models/effdet_lite3/effdet_lite3.tflite")
        self.still_interpreter.allocate_tensors()
        self.still_size = common.input_size(self.still_interpreter)
        self.still_labels = read_label_file("models/effdet_lite3/effdet_lite3.labels")

        self.video_interpreter = make_interpreter('models/ssd_mobnet2/ssd_mobnet2_tf2.tflite')
        self.video_interpreter.allocate_tensors()
        self.video_size = common.input_size(self.video_interpreter)
        self.video_labels = read_label_file("models/ssd_mobnet2/ssd_mobnet2_tf2.labels")

        # Initialize Camera
        self.camera = Picamera2()
        self.recording_fps = 60.0
        self.playback_fps = 10.0
        self.video_config = self.camera.create_video_configuration(main= {"size": self.video_size, 'format': 'RGB888'}, controls={"FrameRate": self.recording_fps})
        self.still_config = self.camera.create_still_configuration({"size": self.still_size, 'format': 'RGB888'})
        self.camera.start()
        sleep(2) 

    def take_and_infer_still(self):
        self.camera.switch_mode(self.still_config)
        
        frame = self.camera.capture_array()
        processed_frame = self.process_frame(frame, video=False)

        cv2.imwrite(f"/home/pi/drone/images/{datetime.today().strftime('%Y-%m-%d_%H-%M-%S')}.jpg", processed_frame)
        print("Image processed and saved!")

    # TODO: Improve performance on video inference. Manages only 10FPS video on output.
    def stream_and_infer_video(self):
        self.camera.switch_mode(self.video_config)
        out = cv2.VideoWriter(f"/home/pi/drone/videos/{datetime.today().strftime('%Y-%m-%d_%H-%M-%S')}.avi", cv2.VideoWriter_fourcc(*'XVID'), self.playback_fps, self.video_size)

        try: 
            while True:
                recorded_frame = self.camera.capture_array()
                processed_frame = self.process_frame(recorded_frame, video=True)
                out.write(processed_frame)

        except KeyboardInterrupt:
            out.release()

    def process_frame(self, frame, video=False):
        if video:
            common.set_input(self.video_interpreter, frame)
            self.video_interpreter.invoke()
            objects = detect.get_objects(self.video_interpreter, score_threshold=0.7)
            labels = self.video_labels
        else:
            common.set_input(self.still_interpreter, frame)
            self.still_interpreter.invoke()
            objects = detect.get_objects(self.still_interpreter, score_threshold=0.7)
            labels = self.still_labels

        for obj in objects:
            bbox = obj.bbox
            cv2.rectangle(frame, (bbox.xmin, bbox.ymin), (bbox.xmax, bbox.ymax), (0, 255, 0), 2)
            cv2.putText(frame, f'{obj.id} {obj.score:.2f}', (bbox.xmin, bbox.ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            print(f"Detected: {labels.get(obj.id, obj.id)} (ID: {obj.id}, Score: {obj.score:.2f})")

        return frame