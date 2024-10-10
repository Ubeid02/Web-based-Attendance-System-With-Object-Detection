from ultralytics import YOLO

# Create model from scratch
model = YOLO('yolov8n.yaml')

# Create model pretrained
# model = YOLO('yolov8.pt')

# Training dataset
results = model.train(data='config.yaml', epochs=100, imgsz=640, workers=1, batch=3)