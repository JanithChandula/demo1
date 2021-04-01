import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
print(’x_train: ’, x_train.shape)
K = len(np.unique(y_train)) # Classes
Ntr = x_train.shape[0]