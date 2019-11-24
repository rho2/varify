from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, BatchNormalization, GaussianNoise
import numpy as np
import data
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.utils import plot_model
from keras.optimizers import Adam

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)

n_data = np.array(data.load_images())
n_label = np.array(data.res_img)

datagen = ImageDataGenerator(rotation_range=90, brightness_range=[
                             0.3, 1.0], channel_shift_range=100)
it = datagen.flow(n_data, n_label, batch_size=4)

model = Sequential()
model.add(Conv2D(64, (2, 2), padding='same', input_shape=(256, 256, 3)))
model.add(Activation('relu'))
model.add(BatchNormalization())
model.add(GaussianNoise(0.2))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('sigmoid'))
model.add(MaxPooling2D(pool_size=(4, 4)))
model.add(BatchNormalization())
model.add(Dropout(0.7))

model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(4, 4)))
model.add(BatchNormalization())
model.add(Dropout(0.8))
model.add(GaussianNoise(0.2))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())

# model.add(Conv2D(64, (3, 3)))
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.8))

model.add(Dense(300))
model.add(Dense(1000))

model.add(Dense(64))
model.add(Activation('relu'))

model.add(Dense(5))
model.add(Activation('sigmoid'))


model.compile(Adam(learning_rate=0.0009),
              loss='mean_absolute_error',
              metrics=['accuracy'])

history = model.fit_generator(
    it, verbose=1, steps_per_epoch=10, epochs=100)
model.save('img.h5')

plot_model(model, to_file='model.png')

# Plot training & validation accuracy values
print(history.history)

plt.plot(history.history['accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
