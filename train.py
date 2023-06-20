from ultralytics import YOLO

# Load a model (using the smallest one)
# build a new model from YAML
model = YOLO('yolov8n.yaml')  

# Train the model
# documentation: https://docs.ultralytics.com/modes/train/#arguments
model.train(data='dataset/data.yaml', epochs=10, imgsz=640, project='Speed Limit Detection')
