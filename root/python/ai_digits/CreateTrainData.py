import cv2
import os
import random
import numpy as np
from tqdm import tqdm

class CreateTrainData:
  def __init__(self, train_directory, image_size):
    self. train_directory = train_directory
    self. image_size = image_size
    self.class_names = []
    if not os.path.isfile("X.npy"):
      self.create_class_names()
      self.create_training_data()
    else:
      print("Train data exists!")

  def create_class_names(self):
    for folder_name in os.listdir(self.train_directory):
      self.class_names.append(folder_name)
  
  def create_training_data(self):
    training_data = []
    for number_directory in os.listdir(self.train_directory):
        path_to_image = os.path.join(self.train_directory, number_directory)
        class_index = self.class_names.index(number_directory)

        for number_image in tqdm(os.listdir(path_to_image)):  # Правильне вкладення циклу
            image_path = os.path.join(path_to_image, number_image)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, (self.image_size, self.image_size))
            training_data.append([image, class_index])

    random.shuffle(training_data)
    X, y = zip(*training_data)  # Розпаковка списку
    X = np.array(X).reshape(-1, self.image_size, self.image_size, 1)  # Додавання каналу
    y = np.array(y)

    np.save("X.npy", X)
    np.save("y.npy", y)