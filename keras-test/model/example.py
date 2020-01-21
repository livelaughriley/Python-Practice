from time import time
from keras import optimizers, utils
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import TensorBoard
from scipy import stats
import numpy as np
import pandas as pd
import tensorboard

path = 'C:\\Users\RRoach\Documents\OneDrive - IMODULES ' \
       'SOFTWARE\Desktop\Projects\keras-test\data\wisc_bc_data.csv'

# fix random number seed for reproducibility
np.random.seed(7)

# split into input (X) and output (Y) variables
dataset_raw = np.genfromtxt(path, delimiter = ',', dtype = 'str')

dataset = dataset_raw[:, 1:]
x_train = dataset[1:, 1:]
y_train = dataset[1:, 0]

# preprocessing

x_train = np.ndarray.astype(x_train, dtype = 'float')

## scale X
def normalize_scale(data):
	mins = np.min(data, axis = 0)
	maxs = np.max(data, axis = 0)
	return ((data - mins)) / ((maxs - mins))

def test_normalize_scale(data):  ### test normalize_scale()
	a = normalize_scale(data)
	print(stats.describe(a))
test_normalize_scale(x_train)

x_train = normalize_scale(x_train)

y_train[y_train == 'M'] = 1
y_train[y_train == 'B'] = 0

one_hot_labels = utils.to_categorical(y_train, num_classes = 2)
# if Y[Y == 'M', ]:
#     Y[Y == 1, ] doesnt work
# else: Y[Y == 0, ]


# create model
model = Sequential()
model.add(Dense(12, input_dim = 30, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(2, activation = 'sigmoid'))

# model optimizer
opt = optimizers.Adam(lr = 0.001, beta_1 = 0.9, beta_2 = 0.999, epsilon = None, decay = 0.0, amsgrad = False)

# compile model
model.compile(loss = 'categorical_crossentropy', optimizer = opt, metrics = ['accuracy'])

# tensorboard callback
tensorboard = TensorBoard(log_dir = 'logs/{}'.format(time()))

# fit the model
model.fit(x_train, one_hot_labels, epochs = 150, batch_size = 10, verbose = 1, callbacks = [tensorboard])

# evaluate the model
scores = model.evaluate(x_train, one_hot_labels)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))