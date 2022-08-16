import io
import string
import time
import os
import numpy as np
import tensorflow as tf
import base64
from PIL import Image
from flask import Flask, jsonify, request
from tensorflow import keras
from keras import models

model = models.load_model('{}/Blood_Sugar_Classification.h5'.format(os.getcwd()))
model2 = models.load_model('{}/Mata_atau_Bukan.h5'.format(os.getcwd()))
def prepare_image(img):
    img = Image.open(io.BytesIO(img))
    img = img.resize((150, 150))
    img = np.array(img)
    img = np.expand_dims(img, 0)
    return img


def predict_result(img):
    result_eye = []
    predicted = np.argmax(model.predict(img))
    if predicted == 0:
        result_eye.append("{}% tidak terindikasi diabetes".format(np.max(model.predict(img)*100)))
    if predicted == 1:
        result_eye.append("{}% terindikasi diabetes".format(np.max(model.predict(img)*100)))
    if predicted == 2:
        result_eye.append("{}% terindikasi diabetes".format(np.max(model.predict(img)*100)))
    img_64 = base64.b64encode(img).decode('utf-8')
    hasil = {
        "predict_eye" : result_eye,
        "image_eye" : img_64
    }
    return hasil

def mata_atau_bukan(img):
    kelas_mata = []
    bukan_mata = []
    mata = []
    kelas = model2.predict(img, batch_size=50)
    kelas_mata.append(kelas)
    for x in kelas_mata:
        for i in x:
            a, b = i
            bukan_mata.append(a)
            mata.append(b)
    maks_mata = max(mata)
    return maks_mata


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
    prediksi_mata_atau_bukan = mata_atau_bukan(img)
    if prediksi_mata_atau_bukan < 0.90:
        return "Masukan foto kembali"
    else:
        return jsonify(predict_result(img))
    

@app.route('/', methods=['GET'])
def index():
    return 'Eye Predict'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')