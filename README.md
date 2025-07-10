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

```text
End-To-End-Cell-Segmentation-YOLOv8/
├── app.py                   # Main Flask app
├── cellSegmentation/        # Model training logic and pipeline
├── research/                # Data ingestion and validation scripts
├── templates/               # HTML files for web UI
├── data/                    # Input dataset (unzipped from data.zip)
├── runs/segment/            # YOLOv8 training results
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker configuration
├── setup.py                 # Package metadata
├── LICENSE                  # MIT License
└── README.md                # Project documentation


---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/End-To-End-Cell-Segmentation-YOLOv8.git
cd End-To-End-Cell-Segmentation-YOLOv8
```


### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Required Packages
```bash
pip install -r requirements.txt
```
## 🧬 Dataset Format

Your dataset must follow **YOLOv8 segmentation format**:

- Images in: `data/images/`
- Labels in: `data/labels/`
- Each `.txt` file contains polygon coordinates:

```txt
class_id x1 y1 x2 y2 ... xn yn
```
## 🔬 Applications

- Biomedical image analysis  
- Automated cell counting  
- Drug response analysis  
- Cancer research  
- Histopathological image processing  

---

## 📌 Future Enhancements

-  Post-processing with morphological filters  
-  Annotation tool integration (Label Studio, CVAT)  
-  Model optimization (ONNX, TensorRT)  
-  3D segmentation support  

---

## 📜 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more details.

---

## 👨‍💻 Author

**Rushikesh Gaikhe**  
🔗 [LinkedIn](https://www.linkedin.com/in/rushikesh-gaikhe)  
🐙 [GitHub](https://github.com/rushikeshgaikhe)
