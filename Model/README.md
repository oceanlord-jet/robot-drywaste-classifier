# Garbage Classification with EfficientNetB0 + YOLOv8 + Grad-CAM

This project combines deep learning for image classification and object detection to build a smart, interpretable garbage classification system. It classifies waste into three categories: **metal**, **paper**, and **plastic**, while leveraging Grad-CAM to explain the model's predictions.

---

## Dataset Overview

The dataset consists of 2,684 images labeled into three categories:

- `metal`: 769 images  
- `paper`: 1,050 images  
- `plastic`: 865 images  

The images vary in lighting, orientation, and background, providing a realistic challenge for visual classification tasks.

---

## Model Architecture

We use **EfficientNetB0** as the base image classification model due to its excellent balance of accuracy and efficiency. It is trained on resized (224×224) images of garbage objects using data augmentation and label encoding for robust performance.

---

## Limitations of Base Model

While EfficientNetB0 performs well in clean, centered images, it struggles in cluttered or complex backgrounds. Irrelevant objects and noise in the image can reduce prediction confidence and accuracy.

---

## Improving Focus with YOLOv8

To address this, we integrate **YOLOv8** as a preprocessing step at inference time. YOLO detects and crops objects in the scene, and only the detected regions are passed to EfficientNetB0. This approach improves:

- Prediction confidence  
- Accuracy in real-world scenes  
- Model focus by reducing background noise

---

## Grad-CAM Visualizations

We use Grad-CAM to visualize where the model is focusing in each image. This provides interpretability and helps validate that predictions are based on relevant object features rather than distractions.

---

## Future Work

- Integrate YOLO into the training pipeline to provide focused crops during training, not just inference.
- Fine-tune YOLO on the garbage dataset to improve object detection accuracy.
- Extend support for multi-object detection and classification in a single image.

---

## Tech Stack

- Python 3.x
- TensorFlow / Keras
- OpenCV
- YOLOv8 (Ultralytics)
- Matplotlib and Seaborn
- Grad-CAM

## Acknowledgements

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [EfficientNet Paper](https://arxiv.org/abs/1905.11946)
- Grad-CAM implementation adapted from TensorFlow tutorials

## Kaggle Link-->https://www.kaggle.com/code/percival224/garbage-classification

