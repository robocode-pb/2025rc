import tensorflow as tf  # ШІ Модуль
import matplotlib.pyplot as plt  # Візуалізація даних
import numpy as np   # Робота з масивами

from CreateTrainData import CreateTrainData

TRAIN_DIRECTORY = "data/training" 

IMAGE_SIZE = 28 

ctd = CreateTrainData(TRAIN_DIRECTORY, IMAGE_SIZE)

X_train = np.load("X.npy")
y_train = np.load("y.npy")

X_train = np.array(X_train).reshape(-1, 28, 28, 1)
y_train = np.array(y_train)
X_train = X_train / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation="relu", input_shape=(28,28,1)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation="relu"),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer='adam',
             loss='sparse_categorical_crossentropy',
             metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=3)
model.save("myModel.keras")

# Візуалізація точності
plt.plot(history.history['accuracy'])
plt.title('Model accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.show()

# Візуалізація втрат
plt.plot(history.history['loss'])
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()