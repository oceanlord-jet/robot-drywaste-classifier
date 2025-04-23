# Robotic Dry Waste Classifier with Niryo One

The **Robot Dry Waste Classifier** is a Niryo One robot designed to revolutionize waste management by automating the classification of dry waste. This robot is equipped with a camera and a deep learning model that allows it to capture and analyze images of waste materials to determine their type.

Built with a focus on efficiency and reliability, it offers an ideal solution for waste segregation in industrial and urban settings. The project includes Python scripts for controlling the robot’s movement, handling image classification, and managing the full sorting workflow. By integrating cutting-edge robotics and machine learning, the system aims to streamline waste management processes and promote sustainable practices.

---

## Project Overview

This system combines a **Niryo One robotic arm** with a deep learning model based on **EfficientNetB0**. The robot captures an image of a waste item, classifies it into one of three categories—**metal**, **paper**, or **plastic**—and moves it to the appropriate bin.

---

## Features

- Automated waste detection and classification  
- Image-based sorting using EfficientNetB0  
- Object handling via Niryo One robotic arm  
- Real-time camera capture and processing  
- Gradual and accurate item placement into categorized bins  

---

## Folder Structure

```plaintext
Robot/
├── classify_function.py        # Image classification logic using a Keras model
├── watchy.py                  # Main robot operation and sorting workflow
├── captured_image.jpg         # Snapshot captured by the robot camera
└── best_efficientnetb0_garbage.keras/
    ├── config.json            # Model architecture
    ├── model.weights.h5       # Trained weights
    └── metadata.json          # Metadata from the training environment
```

---

## How It Works

1. **Capture Image**  
   The robot moves to a predefined `watch` pose and captures an image using its onboard camera.

2. **Classify Waste**  
   The captured image is passed to a pretrained EfficientNetB0 model which predicts whether the item is `metal`, `paper`, or `plastic`.

3. **Sort Waste**  
   Based on the classification, the robot moves to the correct bin (`metalbin`, `paperbin`, or `plasticbin`) and places the item accordingly using its gripper tool.

---

## Requirements

- Python 3.x  
- TensorFlow / Keras  
- OpenCV  
- NumPy  
- pyniryo2 (Niryo Python API)

**Install dependencies:**

```bash
pip install tensorflow opencv-python pyniryo2 numpy
```

---

## Running the System

To run the full robot-powered sorting operation:

```bash
python watchy.py
```

To test classification alone (without the robot):

```bash
python classify_function.py
```

Ensure that the robot is powered on and connected over the network (default IP is `10.10.10.10`) and that all necessary poses (`watch`, `pick`, `metalbin`, `paperbin`, `plasticbin`) are saved in Niryo Studio.

---

## Model Information

The classification model is stored in Keras format:

- `config.json` contains the model architecture  
- `model.weights.h5` holds the trained weights  
- `metadata.json` includes training metadata (optional)

TensorFlow is configured to run on CPU only for broader hardware compatibility.

---

## Future Enhancements

- Integrate object detection (e.g., YOLO) to support multi-object scenes.  
- Train the classifier on additional material types (e.g., glass, organic).  
- Add real-time feedback or UI to monitor robot activity.  
- Deploy to edge devices (e.g., Jetson Nano or Raspberry Pi).

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- Niryo One Robot  
- EfficientNetB0 Paper  
- Ultralytics YOLO (for vision extension)  
- TensorFlow and Keras open-source community
