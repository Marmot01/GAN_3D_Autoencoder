import tensorflow as tf
from GAN_model import GAE
from Dataset_Reader import Reader 
from Dataset_Reader import IdentityAugmentation
import os
import SimpleITK as sitk 
import numpy as np

datapath = r'../Data'
file_reference = r'../training/File_reference.csv'

img_ls = os.listdir(datapath)
train_set = np.zeros(shape=[len(img_ls), 48, 96, 96, 1], dtype=np.float32)

for idx, file in enumerate(img_ls):
    img = sitk.ReadImage(os.path.join(datapath, file))
    img = sitk.GetArrayFromImage(img)
    img = img[:,2:98,2:98,np.newaxis].astype(np.float32) / 255.
    train_set[idx] = img


model = GAE(encoded_dim=128)
model.train(train_set, batch_size=4, epochs=500)