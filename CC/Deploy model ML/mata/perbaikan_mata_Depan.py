import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import io
import tensorflow as tf
import numpy as np
import string
import time
import base64
from PIL import Image
from tensorflow import keras
from keras import models
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({"error": "no file"})

        try:
            img64 = ''
            model = models.load_model('{}/Blood_Sugar_Classification.h5'.format(os.getcwd()))
            model2 = models.load_model('{}/Mata_atau_Bukan.h5'.format(os.getcwd()))
            img_bytes = file.read()
            img = Image.open(io.BytesIO(img_bytes))
            img = img.resize((150, 150))
            img.save('{}/mata_resize.jpg'.format(os.getcwd()))
            img = np.array(img)
            img = np.expand_dims(img, 0)
            

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
            if maks_mata < 0.90:
                return "Masukan foto kembali"
            else:
                result_eye = []
                predicted = np.argmax(model.predict(img))
                if predicted == 0:
                    result_eye.append("Terindikasi Diabetes (Glaukoma)")
                if predicted == 1:
                    result_eye.append("Terindikasi Diabetes (Katarak)")
                if predicted == 2:
                    result_eye.append("Tidak Terindikasi Diabetes")
                
                with open('{}/mata_resize.jpg'.format(os.getcwd()), 'rb') as binary_file:
                    binary_file_data = binary_file.read()
                    binary_file_encoded = base64.b64encode(binary_file_data).decode('utf-8')
                    img64 += binary_file_encoded

                hasil = {
                    "predict_eye" : result_eye,
                    "image_eye" : img64
                }
                return jsonify(hasil)
        except Exception as e:
            return jsonify({"error": str(e)})

    return 'Eye Predict 1'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))