import json, os, io, imageio
from PIL import Image
import numpy as np

os.environ['KERAS_BACKEND'] = 'theano'

from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications import imagenet_utils


class KerasModel():

    def __init__(self, model_file, weights_file):
        # load json and create model
        json_file = open(model_file, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self.loaded_model = model_from_json(loaded_model_json)
        self.loaded_model.load_weights(weights_file)
        print("Prediction model loaded from disk")

    @staticmethod
    def prepare_image(image, target):
        # if the image mode is not RGB, convert it
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        # resize the input image and preprocess it
        image = image.resize(target)
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        image = imagenet_utils.preprocess_input(image)
        # return the processed image
        return image
    
    def predict_multiple(self, image_names):
        results = []
        for imagename in image_names:
            image = Image.open(imagename)
            image_loaded = KerasModel.prepare_image(image, target=(150,150))
            preds = self.loaded_model.predict(image_loaded)
            _, filename = os.path.split(imagename)
            results.append({'filename': filename, 'prediction': int(round(preds[0][0]))})
        return results
