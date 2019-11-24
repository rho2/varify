import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, GaussianNoise, Dropout
import data

N = len(data.dataset_easy[0])
print(N)

model = Sequential()
model.add(Dense(N))

model.add(Dense(100))
model.add(Dense(300))
model.add(Dense(1000))

model.add(Dense(300))
model.add(Dense(100))

model.add(Dense(5, activation='sigmoid'))

model.compile(optimizer='rmsprop',
              loss='mean_absolute_error',
              metrics=['accuracy'])

n_data = np.array(data.dataset_easy)
n_label = np.array(data.out_norm)

n_val_data = np.array(data.dataset_val)
n_val_label = np.array(data.val_res)

model.fit(n_data, n_label, epochs=250, batch_size=4, verbose=1, validation_data=(n_val_data, n_val_label))
model.save('question.h5')