import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, GaussianNoise, Dropout
import data

N = len(data.human_data[0])
print(N)

model = Sequential()
model.add(Dense(N))

model.add(Dense(10))
model.add(Dense(7))
model.add(Dense(5, activation='sigmoid'))

model.compile(optimizer='rmsprop',
              loss='mean_absolute_error',
              metrics=['accuracy'])

n_data = np.array(data.human_data)
n_label = np.array(data.out_norm)

model.fit(n_data, n_label, epochs=5000, batch_size=32, verbose=1)
model.save('human.h5')
