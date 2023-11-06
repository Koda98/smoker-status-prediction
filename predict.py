import pickle
import json
from flask import Flask, request, jsonify
import numpy as np

model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

app = Flask('smoking')


@app.route('/predict', methods=['POST'])
def predict():
    patient = request.get_json()
    patient_array = np.array([list(patient.values())])
    X = patient_array.reshape(1, -1)
    smoking_prob = model.predict_proba(X)[0, 1]
    
    result = {'smoking probability': float(smoking_prob)}
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
