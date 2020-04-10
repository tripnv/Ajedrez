from __future__ import print_function
import tensorflow as tf 
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt 
import os 
import cv2
import IPython.display as display
from PIL import Image
import pathlib



def collect_image_paths(path, batch_size):
    imagepaths, labels = list(), list()
    #imgs = np.array()
    label = 0
    classes = sorted(os.walk(path).__next__()[1])
    for c in classes:
        c_dir = os.path.join(path, c)
        walk = os.walk(c_dir).__next__()
        label= str(c)
        for sample in walk[2]:
            # jpg, jpeg, png images
            if sample.endswith('.jpg') or sample.endswith('.jpeg') or sample.endswith('.png'):
                    imagepaths.append(os.path.join(c_dir, sample))
                    labels.append(label)
    
    return imagepaths, labels

def read_pictures(paths, lbl):
    image_list = []
    p_sizes = (100,100)
    for i in range(len(paths)):
        img = cv2.imread(paths[i])
        cv2.resize(img, p_sizes, interpolation=cv2.INTER_AREA)
        ttl = (img, lbl[i])
        image_list.append(ttl)

    return image_list 

def main():
    x, y= collect_image_paths("/Users/soren/Desktop/chess_1/idsquare/pieces/", None)
    z = read_pictures(x, y)

main()