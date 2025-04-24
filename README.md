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
├── Simulation/                             # Virtual testing environment in Webots
│   ├── worlds/                             # Simulation world definitions
│   │   ├── arm_robot.wbt                   # Main world file with UR5e setup and environment
│   │   └── .arm_robot.wbproj              # Webots project configuration file
│   └── controllers/                        # Robot control scripts
│       └── simple_pick_place/              # Pick and place controller
│           ├── simple_pick_place.py        # Main robot control logic
│           └── __init__.py 
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

The simulation implements a robotic waste classification system with the following components:

1. **Robot Setup**:
   - Universal Robots UR5e robotic arm mounted on a fixed base
   - Robotiq 3-finger gripper for object manipulation
   - JetBot Raspberry Pi Camera for object detection and classification

2. **Environment**:
   - Factory-themed background with proper lighting
   - 10x10 meter arena with parquet flooring
   - Three colored boxes representing different types of waste:
     - Red box
     - Green box
     - Blue box
   - Three designated bins for waste sorting

3. **Functionality**:
   - The robot uses computer vision to identify waste objects
   - Pick and place operations are simulated with precise joint control
   - The gripper can perform basic open/close operations
   - Objects are sorted into their respective bins based on classification

The simulation serves as a testbed for developing and validating waste classification algorithms and robot control strategies before deployment on physical hardware.
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
