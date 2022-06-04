import imghdr
import io
import string
import time
import os
import cv2
from unittest import result
import numpy as np
import tensorflow as tf
import base64
from PIL import Image
from flask import Flask, jsonify, request
from tensorflow import keras
from keras import models

model = models.load_model('D:\MBKM\BANGKIT\TensorFlow Practice\.venv\My_Model_4.h5')
def prepare_image(img):
    img = np.array(Image.open(io.BytesIO(img)))
    img = cv2.resize(img, (426, 426, 3))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = gaussian = cv2.addWeighted(img,4, cv2.GaussianBlur(img , (0,0) , 426/10) ,-4 ,128)
    #img = base64.b64encode(img).decode('utf-8')
    return img


def predict_result(img):
    result = []
    predicted = np.argmax(model.predict(img))
    if predicted == 0:
        # return "Terindikasi Diabetes"
        result.append("Terindikasi Diabetes Ringan")
        # return result
    if predicted == 1:
        # return "Terindikasi Diabetes"
        result.append("Terindikasi Diabetes Sedang")
        # return result
    if predicted == 2:
        # return "Tidak Terindikasi Diabetes"
        result.append("Tidak Terindikasi Diabetes")
        # return result
    if predicted == 3:
        # return "Terindikasi Diabetes"
        result.append("Terindikasi Diabetes Parah")
        # return result
    if predicted == 4:
        # return "Terindikasi Diabetes"
        result.append("Terindikasi Diabetes Sangat Parah")
        # return result
    img_64 = base64.b64encode(img).decode('utf-8')
    hasil = {
        # "predict" : result,
        "image_base64" : img_64
    }
    return hasil

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def infer_image():
    if 'file' not in request.files:
        return "The Image doesn't exist"
    
    file = request.files.get('file')

    if not file:
        return "File not found"

    img_bytes = file.read()
    img = prepare_image(img_bytes)
    prediction=predict_result(img)
    return jsonify(prediction)
    

@app.route('/', methods=['GET'])
def index():
    return 'Eye Predict'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')