from tensorflow.keras import *
from tensorflow.keras.layers import *
from path import *

def BiLSTM(inpput_shape):
    input_layer = Input(inpput_shape)
    x = Reshape((10, 30))(input_layer)
    x = Bidirectional(LSTM(256, return_sequences=True))(x)
    x = Convolution1D(100, 3, activation="relu")(x)
    x = Flatten()(x)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.5)(x)
    output_layer = Dense(27, activation='softmax')(x)
    return Model(inputs=input_layer, outputs=output_layer)
