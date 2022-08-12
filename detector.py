import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
from PIL import Image

import torch
import torch.nn.functional as F

import PIL
import pdb
import json
import cv2

class Detector(object):
    """docstring for Detector"""
    def __init__(self):
        super(Detector, self).__init__()
        # Set the path
        path_model = './yolov5'
        path_weights = './best_weight.pt'
        # Load the model
        self.model = torch.hub.load(path_model, 'custom', path=path_weights, source='local')
        self.model.max_det = 1
        self.model.conf = 0.6

    def load(self):
        pass

    def forward(self, img):
        #img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        #img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        #img = PIL.Image.fromarray(img_rgb, "RGB")
        
        results = self.model(img)
        results = results.pandas().xyxy[0].to_json(orient="records")
        results = json.loads(results)
        
        confidence = 0
        for result in results:
            xmin = int(result.get('xmin'))
            ymin = int(result.get('ymin'))
            xmax = int(result.get('xmax'))
            ymax = int(result.get('ymax'))
            confidence = float(result.get('confidence'))
        
        pred_y_label = confidence > 0.5
        if pred_y_label:
            x_center = (xmin + xmax) / 2
            y_center = (ymin + ymax) / 2
            pred_bboxes = np.array([x_center, y_center])
        else:
            pred_bboxes = np.array([10, 10])

        return pred_bboxes, [pred_y_label]