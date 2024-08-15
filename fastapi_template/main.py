from fastapi import FastAPI, Query
import os
import uvicorn

class DummyModel:
    def predict(self, X):
        return "dummy prediction"

def load_model():
    predictor = DummyModel()
    return predictor

app = FastAPI()
app.predictor = load_model()

@app.get("/hello")
def read_hello():
    return {"message": "hello world"}

@app.get("/predict")
def predict(X: str = Query(..., description="Input text for prediction")):
    result = app.predictor.predict(X)
    return {"input_value": X, "predicted_value": result, "message": "prediction successful"}

def run():
    uvicorn.run("fastapi_template.main:app", host="0.0.0.0", port=8000, reload=True)
