from fastapi import APIRouter, HTTPException, Query
from model.predict import ModelPredictor
from model.monitor import monitor_prediction_time
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

router = APIRouter()
predictor = ModelPredictor("model/svm_model.pkl")
# monitor = monitor_prediction_time()

@router.post("/predict/")
# @monitor
def predict(text: str):
    logging.info(f"Received text: {text}")
    try:
        result = predictor.predict(text)
        logging.info(f"Prediction result: {result}")
        return {"status": "success", "data": result}
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))