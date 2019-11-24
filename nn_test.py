import numpy as np
import json
from keras.models import Sequential
from keras.layers import Dense, Activation, GaussianNoise
import re
from keras.models import load_model
import data


x = ["vim", "windows", "python", "spaces", "none", "algo"]

elem = []
editor_hot = [0] * len(data.editors)
editor_hot[data.editor_dict[x[0].lower()]] = 1
elem += editor_hot

oss_hot = [0] * len(data.oss)
oss_hot[data.oss_dict[x[1].lower()]] = 1
elem += oss_hot

lang_hot = [0] * len(data.languages)
lang_hot[data.languages_dict[x[2].lower()]] = 1
elem += lang_hot

car_hot = [0] * len(data.cars)
car_hot[data.cars_dict[x[4].lower()]] = 1
elem += car_hot

choice_indent = x[3].lower() == "tabs"
choice_employ = x[5].lower() == "human"

elem.append(choice_indent)
elem.append(choice_employ)

x = np.array([elem])

print(x)

model = load_model('questions.h5')
t = model.predict(x, verbose=2)

print(*t)