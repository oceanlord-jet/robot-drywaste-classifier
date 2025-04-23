# Robotics Project: Automated Garbage Classification

**Automated Garbage Classification Robot**

This project presents an automated garbage classification system utilizing a Niryo robotic arm integrated with a high-resolution camera to identify, classify, and sort waste items into designated containers for paper, plastic, and metal. The system leverages advanced machine learning techniques, specifically EfficientNetB0 for object classification and YOLOv8 for multi-object detection. The integration of these technologies enables real-time, accurate sorting operations. Comprehensive testing reveals strong system reliability and sorting precision, making a substantial contribution to efficient, scalable, and environmentally sustainable waste management solutions.

---

## 📁 Project Structure

```plaintext
.
├── Model/                     # Image classification pipeline
│   └── README.md              # Details on model training and evaluation
├── Robot/                     # Niryo One robot integration
│   └── README.md              # Instructions for running on real hardware
├── Simulation/                # Virtual testing and visualization
│   └── README.md              # Description of the simulated sorting logic
└── README.md                  # (This file) Overview of the full robotics project
```

---

## 🔍 What Each Part Does

### 1. Model

Uses **EfficientNetB0** to classify waste images into three categories: `metal`, `paper`, and `plastic`. Grad-CAM is used to visualize where the model focuses its attention, helping validate its predictions. Includes:
- Data preprocessing  
- Augmentation and training  
- Evaluation and interpretability

[Explore the Model →](./Model)

---

### 2. Robot

Controls the **Niryo One robotic arm** to perform real-time sorting. It captures an image, classifies it using the trained model, and moves the object to the appropriate bin. It is designed for reliability and ease of integration with physical systems.

[Explore the Robot Module →](./Robot)

---

### 3. Simulation

Allows users to test the sorting process in a **virtual environment** when access to physical hardware is limited. It mimics the classification and decision logic of the robot workflow.

[Explore the Simulation →](./Simulation)

---

## 🛠 Technologies Used

- Python 3.x  
- TensorFlow / Keras  
- OpenCV  
- Ultralytics YOLO (in Model)  
- pyniryo2 (in Robot)  
- Jupyter Notebooks  
- Linux (WSL/Ubuntu) or Windows  

---

## 🚀 Goals

- Automate waste classification and sorting  
- Support sustainable waste management practices  
- Provide a modular framework for both physical and simulated testing  
- Encourage further research in smart robotics and machine learning for environmental applications

---

## 📄 License

This project is licensed under the MIT License.

