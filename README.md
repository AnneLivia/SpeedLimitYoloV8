## Train annotation YOLO

In this repository, it's been used YoloV8 to detect speed limit sign using a dataset exported from Roboflow.

## Custom dataset
- Dataset speed-limit was obtained from [roboflow.com](https://universe.roboflow.com/knubot/speed-limit-s6q3y).
- Folder structure and annotation (txt) format must follow:
    - class, x, y, width and height, ex: 0 0.4877835951134381 0.4790575916230367 0.9476439790575917 0.7835951134380454
    - A directory with two folders called images and labels are required for each set (train, validation).
    - The labels in txt must have the same name as the image.

## Results

<img src="https://github.com/AnneLivia/SpeedLimitYoloV8/blob/main/Speed%20Limit%20Detection/train/val_batch1_labels.jpg" alt='batch validation' width="50%"/>
