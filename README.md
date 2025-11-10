# YOLO Real-Time Object Detection

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95.0+-green.svg)](https://fastapi.tiangolo.com/)
[![YOLOv8](https://img.shields.io/badge/YOLO-v8-darkgreen.svg)](https://github.com/ultralytics/ultralytics)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-ready real-time object detection system built with YOLOv8 and FastAPI. This application provides live camera feed processing with object detection capabilities through an intuitive web interface.

## ✨ Features

- 🎯 Real-time object detection using **YOLOv8**
- 🎥 Live camera feed streaming with **FastAPI**
- 🚀 Optimized performance with **headless OpenCV**
- 🔄 Automatic camera reconnection on failure
- 🖥️ Responsive web interface with error handling
- 🐳 Docker support for easy deployment
- 📊 Health monitoring and logging
- 🔌 CORS support for API integration

---

## 🛠️ Tech Stack

- **Backend Framework:** FastAPI
- **ML Model:** YOLOv8 (Ultralytics)
- **Video Processing:** OpenCV
- **Server:** Uvicorn (ASGI)
- **Frontend:** HTML5, CSS3, JavaScript
- **Templating:** Jinja2

## 📋 Requirements

- Python 3.10 or higher
- Webcam or IP camera
- (Optional) NVIDIA GPU for acceleration

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/syedmehrabzaidi/object-detection-using-yolo.git
   cd object-detection-using-yolo
2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # or
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

5. **Access the application**
   - Open your browser and navigate to: http://localhost:8000
   - The live camera feed with object detection will start automatically

## 📁 Project Structure

```
object-detection-using-yolo/
├── app/
│   ├── main.py           # FastAPI application
│   ├── camera.py         # Camera handling
│   ├── yolo_model.py     # YOLO model implementation
│   └── templates/
│       └── index.html    # Web interface
├── config.yaml           # Configuration file
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
└── README.md
```
## 🐳 Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t yolo-detection .
   ```

2. **Run the container**
   ```bash
   docker run -d -p 8000:8000 yolo-detection
   ```

## ⚙️ Configuration

The application can be configured through `config.yaml`:

- Model selection (different YOLO versions)
- Camera source (webcam, IP camera)
- Detection confidence threshold
- API settings

## 🔧 Advanced Usage

### GPU Acceleration

To enable GPU acceleration (requires NVIDIA GPU with CUDA):

```python
# In app/yolo_model.py
model = YOLO("yolov8n.pt", device="cuda")
```
### Multiple Camera Support

The application can be extended to support multiple cameras:

1. Modify the Camera class to handle multiple sources
2. Update the API endpoints to specify camera IDs
3. Adjust the frontend to display multiple feeds

## 📝 API Documentation

Once the application is running, visit:
- API documentation: http://localhost:8000/docs
- Alternative documentation: http://localhost:8000/redoc

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👤 Author

**Syed Mehrab**
- Email: syedmehrab2288@gmail.com
- GitHub: [@syedmehrabzaidi](https://github.com/syedmehrabzaidi)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ultralytics](https://github.com/ultralytics/ultralytics) for YOLOv8
- [FastAPI](https://fastapi.tiangolo.com/) for the amazing web framework
- The OpenCV community for computer vision tools

Do you want me to do that?




