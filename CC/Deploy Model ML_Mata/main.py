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
            model = models.load_model('{}/Blood_Sugar_Classification.h5'.format(os.getcwd()))
            model2 = models.load_model('{}/Mata_atau_Bukan.h5'.format(os.getcwd()))
            img_bytes = file.read()
            img = Image.open(io.BytesIO(img_bytes))
            img = img.resize((150, 150))
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
                img_64 = base64.b64encode(img).decode('utf-8')
                hasil = {
                    "predict_eye" : result_eye,
                    "image_eye" : img_64
                }
                return jsonify(hasil)
        except Exception as e:
            return jsonify({"error": str(e)})

    return 'Eye Predict'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))