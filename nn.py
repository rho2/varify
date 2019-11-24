import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, GaussianNoise, Dropout
import data

N = len(data.dataset_easy[0])
print(N)

model = Sequential()
model.add(Dense(N))

model.add(Dense(100))
model.add(Dense(100))

model.add(Dense(50))

model.add(Dense(100))

model.add(Dense(5, activation='sigmoid'))

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

n_data = np.array(data.dataset_easy)
n_label = np.array(data.out_norm)

model.fit(n_data, n_label, epochs=100, batch_size=4, verbose=1)
model.save('got_predict.h5')