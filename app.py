# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:16:15 2020

@author: MDTha
"""

from flask import Flask, request, jsonify
from flask_cors import CORS

#from location of file get what you need

app = Flask(__name__)
CORS(app)

model = 

@arr.route("/predict", methods=['POST'])
def predict():
    doc = request.json["document"]
    q = request.json["question"]
    try:
        out = model.predict(doc,q)
        return jsonify({"result":out})
    except Exception as e:
        print(e)
        return jsonify({"result":"Model Failed"})

if __name__ == "__main__":
    app.run('0.0.0.0',port=8000)