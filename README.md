# 🧫 End-To-End Cell Segmentation Using YOLOv8

This project provides an end-to-end pipeline for detecting and segmenting cells in microscopic images using **YOLOv8 (You Only Look Once version 8)**. It is suitable for tasks like biomedical image analysis, cell counting, and diagnostic automation.

---

## 🚀 Features

- ✅ Cell detection and segmentation using YOLOv8 (Segmentation variant)
- ✅ Complete pipeline: Data preprocessing → Training → Inference → Visualization
- ✅ Real-time prediction on image and video input
- ✅ Exportable to ONNX, TensorRT, and other formats
- ✅ Easy deployment via CLI or Web App (optional)

---

## 🧠 Model Overview

- **Model**: YOLOv8 Segmentation (`yolov8s-seg.pt` or any variant)
- **Framework**: PyTorch (via Ultralytics)
- **Task**: Instance segmentation (cells in microscopy images)

---

## 📂 Project Structure

End-To-End-Cell-Segmentation-YOLOv8/
├── data/ # Training and validation data
│ ├── images/
│ └── labels/
├── runs/ # YOLOv8 training outputs
├── yolov8_custom.yaml # Dataset configuration
├── train.py # Custom training script (optional)
├── predict.py # Inference script
├── requirements.txt # Project dependencies
├── Dockerfile # For containerization (optional)
├── README.md # Project documentation
└── app/ # Web app folder (Streamlit or Flask)

