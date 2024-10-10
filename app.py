from flask import Flask, request, jsonify, render_template
import mysql.connector
from ultralytics import YOLO
import cv2
import numpy as np

app = Flask(__name__)
model = YOLO('./runs/detect/train/weights/best.pt')

# Configure
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="absensimahasiswa"
)

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({'message': 'Tidak ada bagian gambar'}),   400

    file = request.files['image']
    npimg = np.fromstring(file.read(), np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    
    results = model.predict(img)
    boxes = results.xyxy[0].tolist()
    conf = results.xyxy[1].tolist()
    cls = results.xyxy[2].tolist()
    
    faces = []
    for i, box in enumerate(boxes):
        x1, y1, x2, y2 = box[:4]
        faces.append({
            'koordinat': f"{x1},{y1},{x2},{y2}",
            'kepercayaan': float(conf[i]),
            'label': model.names[int(cls[i])]
        })
    
    return jsonify(faces)

if __name__ == '__main__':
    app.run(debug=True)
