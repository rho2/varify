import numpy as np
import json
from keras.models import Sequential
from keras.layers import Dense, Activation, GaussianNoise
import re
from keras.models import load_model
import data
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
import sys
import tensorflow as tf

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)


img = load_img(sys.argv[1], target_size=(256, 256))
print(img.size)

img = img_to_array(img)
x = np.array([img])

model = load_model('img.h5')
t = model.predict(x, verbose=2)

t *= 7

print(*t)
