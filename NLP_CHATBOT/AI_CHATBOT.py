from flask import Flask, jsonify, request
import json
import pickle
import tensorflow as tf
from tensorflow import keras
from keras import models
from sklearn.preprocessing import LabelEncoder
import numpy as np
model = keras.models.load_model('chat_model.h5')
with open("data_dummy.json") as file:
    data = json.load(file)
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
with open('label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)
max_len = 20
app = Flask(__name__)

@app.route('/send', methods=['POST'])
def infer_image():
    user = request.form['User']
    result = model.predict(keras.preprocessing.sequence.pad_sequences(
                           tokenizer.texts_to_sequences([user]),
                           truncating = 'post',
                           maxlen = max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])
    for i in data['intents']:
        if i['tag'] == tag:
            x = {"Chatbot":"{}".format(np.random.choice(i['respon']))}
            return jsonify(x) 
    
@app.route('/form_predict', methods = ['POST'])
def form_predict():
    bahasa = request.form.get('bahasa')
    return 'Bahasa adalah {}'.format(bahasa)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')