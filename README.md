# Project Intelligent Systems: Drones with Artificial Intelligence

This repo contains the code of the banana stalker team for the intelligent systems project in the summer term 2025.
The project utlizes a Raspberry Pi Zero 2 W and a Coral USB Edge TPU -> requires Python 3.9.

For more information, please refer to the [project documentation](https://frankfurt-uas-ai-drone.github.io).

## Models
This project utilizes pretrained models, all of which can be found [here](https://coral.ai/models/all/).
The models have been renamed to shorten the file names. They can be downloaded here:
- [effdet_lite3.tflite](https://raw.githubusercontent.com/google-coral/test_data/master/efficientdet_lite3_512_ptq_edgetpu.tflite) and [effdet_lite3.labels](https://raw.githubusercontent.com/google-coral/test_data/master/coco_labels.txt)
- [ssd_mobnet2_tf2.tflite](https://raw.githubusercontent.com/google-coral/test_data/master/tf2_ssd_mobilenet_v2_coco17_ptq_edgetpu.tflite) and [ssd_mobnet2_tf2.labels](https://raw.githubusercontent.com/google-coral/test_data/master/coco_labels.txt)