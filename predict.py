from ultralytics import YOLO

model = YOLO("./runs/detect/train/weights/best.pt")

model.predict("./photos/two.jpg", save=True, show=True, conf=0.7)