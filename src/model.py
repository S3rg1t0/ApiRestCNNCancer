import numpy as np
from tensorflow.keras.models import load_model

def preprocess_images(images):
    images = images.astype("float32") / 255.0
    return images

img_size = (50, 50)

model = load_model("modelos/modelo_cancer.h5")
