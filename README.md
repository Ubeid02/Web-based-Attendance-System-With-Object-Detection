# Web-based Attendance System with Object Detection

This project is a **Web-based Attendance System** prototype that leverages **YOLO (You Only Look Once)**, a machine learning model for object detection. The system is designed to automate the process of attendance tracking by recognizing faces and verifying identities in real-time using object detection technology. All administrative tasks and attendance management are handled through a user-friendly web interface.

> **Note:** This project is currently **incomplete** and **not yet integrated with a database**. While the object detection component using YOLO is functional, the full system including attendance tracking and database storage is still under development.

## 📜 Features

- **Object Detection with YOLO**: Utilizes the YOLO machine learning model for detecting faces and confirming identities in images or video streams.
- **Real-time Attendance Tracking**: Automates attendance marking by detecting and recording individuals' presence (still under development).
- **Web-based Management**: Provides a web interface to manage attendance records (pending integration with database).
- **User Authentication**: Planned feature to restrict access to the admin panel where attendance data can be managed and reviewed.
- **Attendance Reports**: Planned feature to generate attendance reports that can be exported for further analysis.

## 🛠️ Technologies Used

- **YOLO (You Only Look Once)**: For real-time object detection.
- **Flask**: Backend web framework to serve the web interface and manage interactions.
- **MySQL** (to be integrated): Database management system for storing attendance data and user information.
- **HTML, CSS, JavaScript**: Front-end technologies for creating an intuitive user interface.
- **OpenCV**: For video capture and image processing during object detection.
- **NumPy**: Used for handling arrays and matrices in image processing.

## 🚀 Getting Started

### Prerequisites
- Flask
- MySQL (pending integration)
- OpenCV
- YOLO model

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Web-based-Attendance-System-with-Object-Detection.git

2. Install the required packages:
   ```bash
   pip install flask mysql-connector-python opencv-python-headless ultralytics numpy

3. Start the Flask application:
   ```bash
   flask run

4. Access the system at http://localhost:5000 (or your configured port).

## 📊 System Overview
YOLO Object Detection: Integrates real-time face recognition and object detection for marking attendance.
Admin Dashboard: A planned centralized web interface for viewing and managing attendance records.
Report Generation: To be implemented for generating attendance data reports.

## 🔒 Security
User authentication will ensure that only authorized personnel can access the attendance management system (planned feature).
Attendance data will be securely stored in a database (pending integration).

## 🚧 Project Status
This project is currently in development and is not yet fully functional. The integration with MySQL and full attendance tracking features are still in progress. The object detection module using YOLO is operational, but further work is needed for database interaction and management functionality.

## 🤝 Contribution
We welcome contributions! Please fork this repository and submit a pull request to contribute to the project.
