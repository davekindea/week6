from flask import Flask, request, jsonify
import joblib
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model
model = open('gbm_model.pkl','rb')
classfier=pickle(model)


@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.json
    df = pd.DataFrame(data)
    
    
    
    # Make predictions
    predictions = model.predict(df_transformed)
    proba = model.predict_proba(df_transformed)[:, 1]
    
    return jsonify({'predictions': predictions.tolist(), 'probabilities': proba.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
