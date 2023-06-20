from ultralytics import YOLO
import os
import cv2
import argparse

parser = argparse.ArgumentParser();
parser.add_argument('-file', required=True, help='Path to an image or video to be analyzed using yolo');
args = parser.parse_args()

# obtaining the path to the trained model (last or best)
model_path = os.path.join('.', 'Speed Limit Detection', 'train', 'weights', 'best.pt')

# loading model
model = YOLO(model_path);

isVideo = False;
extension = args.file[len(args.file) - 4:]

# checking if it's in a accepted format
if (extension  == '.mp4'):
    isVideo = True

# running on images
def imagePrediction():
    content = cv2.imread(args.file)
    results = model.predict(content, conf=0.25);
    for result in results:
        print('Bounding Box: {}'.format(result.boxes.data.tolist()));
        # transformando tensor para numpy
        for box in result.boxes.cpu().numpy():
            # transformando para int (o default é float)
            x, y, w, h = box.xyxy[0].astype(int);
            # classes: ['z100', 'z30', 'z40', 'z50', 'z60', 'z70', 'z80', 'z90']
            # className = result.names[int(box.cls[0])];
            # print('Detected class: ', className)
            # cv2.putText(content, className, (int((x + w) / 3.4), y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.rectangle(content, (x, y), (x + w, y + h), (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('Result', content);
    cv2.waitKey(0);

def videoPrediction():
    pass

# loading an image or video
if not isVideo:
    imagePrediction()
else:
    videoPrediction()
