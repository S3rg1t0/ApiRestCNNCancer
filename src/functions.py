import numpy as np
from PIL import Image
import io
from werkzeug.datastructures import FileStorage
from model import model, img_size




def preprocess_images(images):
    images = images.astype("float32") / 255.0
    return images

def predict(image: FileStorage):
    img = image.read()
    img = Image.open(io.BytesIO(img))
    img = img.resize(img_size)
    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_images(x)

    
    prediction = model.predict(x)
   
    print("Predicción:", prediction)  

    if prediction.item() < 0.5:
        result = {
            "label": "No cancer",
            "probability": prediction.item()
        }
    else:
        result = {
            "label": "Cancer",
            "probability": prediction.item()
        }
    
    return result


