import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.optimizers import SGD, Adam
from keras.utils import np_utils
from keras.datasets import mnist

def load_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
        
    train_sample_count = 10000
    
    x_train = x_train[:train_sample_count]
    y_train = y_train[:train_sample_count]
   
    x_train = x_train.reshape(train_sample_count, 28*28)
    x_test = x_test.reshape(x_test.shape[0], 28*28)

    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')

    y_train = np_utils.to_categorical(y_train, 10)
    y_test = np_utils.to_categorical(y_test, 10)

    x_train = x_train / 255
    x_test = x_test / 255

    return (x_train, y_train), (x_test, y_test)

def main():
    (x_train, y_train), (x_test, y_test) = load_data()

    model = Sequential()
    model.add(Dense(input_dim=28*28, units=500, activation='relu'))
    model.add(Dense(units=500, activation='relu'))
    model.add(Dense(units=10, activation='softmax'))
    #model.compile(loss='mse', optimizer=SGD(lr=0.1), metrics=['accuracy'])
    #model.compile(loss='categorical_crossentropy', optimizer=SGD(lr=0.1), metrics=['accuracy'])
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x_train, y_train, batch_size=100, epochs=20)
    
    eval_result_of_train = model.evaluate(x_train, y_train)
    print('\nTrain Accuracy: ', eval_result_of_train[1])
    
    eval_result_of_test = model.evaluate(x_test, y_test)
    print('\nTest Accuracy: ', eval_result_of_test[1])

if __name__ == "__main__":
    main()
