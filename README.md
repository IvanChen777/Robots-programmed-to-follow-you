# CIVIL-459 Deep Learning for Autonomous Vehicles - Final Project



## Group Members

- Tanguy Lewko (tanguy.lewko@epfl.ch)
- Chengkun Li (chengkun.li@epfl.ch)
- Yifeng Chen (yifeng.chen@epfl.ch)
- Aoyu Gong (aoyu.gong@epfl.ch)



## Introduction

In this project, we developed a detector and a tracker that were later used to implement a person-following algorithm on a Loomo robot. The algorithm was further tested during the Tandem race. The main challenge is that our algorithm should be effective even in hard conditions, for instance, when the target object is not in the frame or obstructed by other objects. This project is divided into three milestones: detection, tracking, and implementation on the robot.



## Milestones 1 and 2

### 1.1 Requirement

You can run the detector and tracker using [Google Colab](https://colab.research.google.com/?utm_source=scs-index).

- Google Colab contains most of needed packages and provides NVIDIA Tesla K80 with 16GB RAM.

### 1.2 Model

The architectures of YOLOv5 and Deep SORT are presented in [our report](./Project_Report.pdf).

### 1.3 Before running the detector and tracker

Before running the detector and tracker in Google Colab:

- First, create a directory called `DLAVproj` in your Google Drive, i.e., `/gdrive/MyDrive/DLAVproj`.
- Second, make sure the structure of this directory is the same as in the next section.
  - Download the directory containing the original source code of YOLOv5 [here](https://github.com/ultralytics/yolov5/tree/7c6a33564a84a0e78ec19da66ea6016d51c32e0a).
- Third, click `Change runtime type` in `Runtime` and select `GPU` as `Hardware accelerator`.
- Last, run the provided Jupyter notebooks with `Run all`.

### 1.4 Folder Structure

```
/gdrive/MyDrive/DLAVproj
|
├── yolov5                   # The directory containing the code of YOLOv5
|
├── best_weight.pt           # The saved model of YOLOv5s
|
├── TrainingDetection.ipynb  # The Jupyter notebook for training the detector
├── WebcamDetection.ipynb    # The Jupyter notebook for running the detector
|
└── Tracking.ipynb           # The Jupyter notebook for running the tracker
```



## Milestone 3

### 2.1 Requirement

You can run the detector using the V100 server.

- Before running the detector, install [requirements.txt](./requirements.txt) with

  ```bash
  pip install -r requirements.txt
  ```

  and all the required packages for `client.py` and `detector.py`.

### 2.2 Model

The architecture of YOLOv5 is presented in [our report](./Project_Report.pdf).

### 2.3 Before running the detector

Before running the detector on the V100 server:

- First, install all the required packages.

- Second, create a directory called `DLAVproj` in the V100 server, e.g., `/home/group8/DLAVproj`.

- Third, make sure the structure of this directory is the same as in the next section.

  - Download the directory containing the original source code of YOLOv5 [here](https://github.com/ultralytics/yolov5/tree/7c6a33564a84a0e78ec19da66ea6016d51c32e0a).

- Last, run the provided `client.py` with

  ```bash
  python client.py --ip-address 128.179.186.129 --max-count 5
  ```

### 2.4 Folder Structure

```
/home/group8/DLAVproj
|
├── venv                     # The virtual python environment containing all the required packages
|
├── yolov5                   # The directory containing the code of YOLOv5
|
├── requirements.txt         # The txt file for installing all the required packages of YOLOv5
|
├── best_weight.pt           # The saved model of YOLOv5s
|
├── client.py                # The python file for communicating with the robot
└── detector.py              # The python file for running the detector
```
