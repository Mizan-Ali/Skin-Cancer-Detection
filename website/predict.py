import PIL
import numpy as np
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense
from tensorflow.keras.layers import MaxPool2D, BatchNormalization, Dropout


UPLOAD_PATH = "./website/static/uploads/"
WEIGHTS_PATH = "./website/static/model_weights/weights.hdf5"

IMG_RES = {
    "resize": (28, 28),
    "input_shape": (28, 28, 3),
    "reshape": (-1, 28, 28, 3)
}

CLASSES = {
    0: "actinic keratoses and intraepithelial carcinomae (Cancer)",
    1: "basal cell carcinoma (Cancer)",
    2: "benign keratosis-like lesions (Non-Cancerous)",
    3: "dermatofibroma (Non-Cancerous)",
    4: "melanocytic nevi (Non-Cancerous)",
    5: "pyogenic granulomas and hemorrhage (Can lead to cancer)",
    6: "melanoma (Cancer)"
}


def create_model():
    model = Sequential()
    
    model.add(Conv2D(16, kernel_size=(3,3), input_shape=IMG_RES["input_shape"], activation='relu', padding='same'))
    model.add(MaxPool2D(pool_size=(2,2)))
    model.add(BatchNormalization())
    
    model.add(Conv2D(32, kernel_size=(3,3), activation='relu'))
    model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
    model.add(MaxPool2D(pool_size=(2,2)))
    model.add(BatchNormalization())
    
    model.add(Conv2D(128, kernel_size=(3,3), activation='relu'))
    model.add(Conv2D(256, kernel_size=(3,3), activation='relu'))
    model.add(Flatten())
    
    model.add(Dropout(0.2))
    model.add(Dense(256,activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    
    model.add(Dense(128,activation='relu'))
    model.add(BatchNormalization())
    
    model.add(Dense(64,activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    
    model.add(Dense(32,activation='relu'))
    model.add(BatchNormalization())
    
    model.add(Dense(7,activation='softmax'))
    
    Optimizer = Adam(learning_rate=0.001)
    model.compile(loss='sparse_categorical_crossentropy', optimizer=Optimizer, metrics=['accuracy'])
    
    model.load_weights(WEIGHTS_PATH)
    return model


MODEL = create_model()
def predict(filename):
    image = PIL.Image.open(UPLOAD_PATH + filename)
    image = image.resize(IMG_RES["resize"])
    image = np.array(image).reshape(IMG_RES["reshape"])
    
    prediction = MODEL.predict(image)[0]
    prediction = sorted(
        [(CLASSES[i], round(j*100, 2)) for i, j in enumerate(prediction)],
        reverse=True,
        key=lambda x: x[1]
    )
    
    return prediction
