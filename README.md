# Robotics Project: Automated Garbage Classification

**Automated Garbage Classification Robot**

This repository implements an end-to-end system for automatically classifying and sorting dry waste using a Niryo One robotic arm, deep learning-based vision models, and both real-world and simulated environments.

---

## Repository Structure

```plaintext
.
├── Model/                                  # Image classification pipeline
│   ├── README.md                           # Model training, evaluation, and interpretability
│   └── garbage-classification.ipynb        # Jupyter notebook with data exploration and training
├── Robot/                                  # Niryo One integration and hardware control
│   ├── README.md                           # Setup and usage instructions for physical hardware
│   ├── classify_function.py                # Image classification helper using EfficientNetB0
│   ├── watchy.py                           # Main sorting workflow controlling the robot
│   └── captured_image.jpg                  # Example snapshot from the robot camera
├── Simulation/                             # Virtual testing environment
│   └── README.md                           # Simulation setup and logic for sorting pipeline
└── README.md                               # Overview of full robotics project (this file)
```

---

## Module Descriptions

### 1. Model

Contains the deep learning pipeline and dataset organization for waste classification:

```plaintext
Model/
├── README.md                   # Detailed instructions for training and evaluation
├── garbage-classification.ipynb# Jupyter notebook with data exploration and model training
├── global-classification/      # Raw image dataset organized by category
│   ├── metal/                  # Metal waste images
│   ├── plastic/                # Plastic waste images
│   └── paper/                  # Paper waste images
└── test/                       # Test images for evaluation
```

- **README.md**: Instructions for reproducing the training experiments and visualizing model attention via Grad-CAM.
- **garbage-classification.ipynb**: Data preprocessing, augmentation, training with EfficientNetB0, evaluation metrics, and Grad-CAM interpretability.
- **global-classification/**: Contains categorized raw images for training and validation.
- **test/**: Contains holdout images used for final model evaluation.

---

### 2. Robot

Implements the real-world sorting system:
- **README.md**: Prerequisites, network setup (default IP `10.10.10.10`), saving Niryo Studio poses (`watch`, `pick`, `metalbin`, `paperbin`, `plasticbin`), and running scripts.
- **classify_function.py**: Loads the Keras classification model (`best_efficientnetb0_garbage.keras`) to predict waste categories.
- **watchy.py**: Coordinates pose movements, image capture, classification, and bin placement via the Niryo Python API (pyniryo2).
- **captured_image.jpg**: Sample image used for testing classification without hardware.

Model weights are located in `Robot/best_efficientnetb0_garbage.keras/`:
```plaintext
Robot/best_efficientnetb0_garbage.keras/
├── config.json            # Model architecture configuration
├── model.weights.h5       # Trained weights file
└── metadata.json          # Training metadata and environment details
```

---

### 3. Simulation

Provides a virtual testbed when hardware is unavailable:
- **README.md**: Instructions for running the simulation and visualizing the sorting workflow in a virtual environment.

---

- **Python 3.x**
- **TensorFlow / Keras** (EfficientNetB0)
- **OpenCV**
- **Ultralytics YOLOv8** (for multi-object detection extension)
- **pyniryo2** (Niryo One Python API)
- **Jupyter Notebooks**
- **OS**: Linux (WSL/Ubuntu) or Windows

---

## 🚀 Future Enhancements

- Expand classification to additional materials like glass and organic waste.
- Integrate YOLOv8 for simultaneous multi-object detection and sorting.
- Develop a real-time dashboard for monitoring robot performance.
- Port the system to edge devices (e.g., NVIDIA Jetson Nano, Raspberry Pi).

---
