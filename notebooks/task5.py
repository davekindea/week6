from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()
from sklearn.externals import joblib
classifier = joblib.load('path_to_model.pkl')
from sklearn.externals import joblib
joblib.dump(classifier, 'model.pkl')
features = np.array(features).reshape(1, -1)
prediction = classifier.predict(features)

# Define the input data model using Pydantic
class InputData(BaseModel):
    hour_woe: float
    Value_woe: float
    PricingStrategy_woe: float
    ProviderId_woe: float
    ProductId_woe: float
    month_woe: float
    year_woe: float
    ProductCategory_woe: float
    Amount_woe: float
    day_woe: float
    ChannelId_woe: float
@app.post('/')
def predict():
    return{
        "name":"david"
    }
@app.post('/predict')
def predict(data: InputData):
    # Convert the Pydantic model to a dictionary
    data_dict = data.dict()

    # Extract the WoE fields from the data
    features = [
        data_dict["hour_woe"],
        data_dict["ProviderId_woe"],
        data_dict["Value_woe"],
        data_dict["PricingStrategy_woe"],
        data_dict["ProductId_woe"],
        data_dict["month_woe"],
        data_dict["year_woe"],
        data_dict["ProductCategory_woe"],
        data_dict["Amount_woe"],
        data_dict["day_woe"],
        data_dict["ChannelId_woe"]
    ]

    # Make prediction using the classifier
    prediction = classifier.predict([features])

    # Convert prediction result to a human-readable string
    prediction_result = "is allowed" if prediction[0] >= 0.5 else "is not allowed"

    return {"prediction": prediction_result}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
