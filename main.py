import time

import argparse
import keras
from flyai.dataset import Dataset
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.models import Sequential

from model import Model
from path import MODEL_PATH

parser = argparse.ArgumentParser()
parser.add_argument("-e", "--EPOCHS", default=10, type=int, help="train epochs")
parser.add_argument("-b", "--BATCH", default=128, type=int, help="batch size")
args = parser.parse_args()

sqeue = Sequential()

sqeue.add(Conv2D(32, (3, 3), padding='same', input_shape=(32, 32, 3)))
sqeue.add(Activation('relu'))
sqeue.add(Conv2D(32, (3, 3)))
sqeue.add(Activation('relu'))
sqeue.add(Dropout(0.25))

sqeue.add(Conv2D(64, (3, 3), padding='same'))
sqeue.add(Activation('relu'))
sqeue.add(Conv2D(64, (3, 3)))
sqeue.add(Activation('relu'))
sqeue.add(MaxPooling2D(pool_size=(2, 2)))
sqeue.add(Dropout(0.25))

sqeue.add(Conv2D(128, (3, 3), padding='same'))
sqeue.add(Activation('relu'))
sqeue.add(Conv2D(128, (3, 3)))
sqeue.add(Activation('relu'))
sqeue.add(MaxPooling2D(pool_size=(2, 2)))
sqeue.add(Dropout(0.25))

sqeue.add(Conv2D(256, (3, 3), padding='same'))
sqeue.add(Activation('relu'))
sqeue.add(Conv2D(256, (1, 1)))
sqeue.add(Activation('relu'))
sqeue.add(MaxPooling2D(pool_size=(2, 2)))
sqeue.add(Dropout(0.25))

sqeue.add(Flatten())
sqeue.add(Dense(512))
sqeue.add(Activation('relu'))
sqeue.add(Dropout(0.5))
sqeue.add(Dense(10))
sqeue.add(Activation('softmax'))

# initiate RMSprop optimizer
opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)

# Let's train the model using RMSprop
sqeue.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])
sqeue.summary()

dataset = Dataset()
model = Model(dataset)

best_score = 0
for epochs in range(args.EPOCHS):
    first_time = int(time.time())
    x_train, y_train, x_test, y_test = dataset.next_batch(args.BATCH)
    history = sqeue.fit(x_train, y_train,
                        batch_size=args.BATCH,
                        verbose=1,
                        validation_data=(x_test, y_test))
    score = sqeue.evaluate(x_test, y_test, verbose=0)
    if score[1] > best_score:
        best_score = score[1]
        model.save_model(sqeue, MODEL_PATH, overwrite=True)
        print("step %d, best accuracy %g" % (epochs, best_score))
    print(str(epochs) + "/" + str(args.EPOCHS))
    end_time = int(time.time())
    print('time: ', first_time, end_time, end_time - first_time)
