# SVM Text Classification API

This project is a text classification API built using **FastAPI**. The application uses a Support Vector Machine (SVM) model trained with TF-IDF features to classify text into predefined categories. It includes endpoints for training the model and making predictions.

---

## Features

- **Train the Model**: Train an SVM model using labeled text data.
- **Make Predictions**: Predict the class of a given text input via a FastAPI endpoint.
- **Performance Monitoring**: Monitor execution time for predictions.

---

## Directory Structure

```plaintext
Spam-Classification-Project/
├── app/
│   ├── main.py             # FastAPI entry point
│   ├── routes.py           # API route definitions
├── model/
│   ├── monitor.py          # Execution time monitoring decorator
│   ├── predict.py          # Model predictor class
│   ├── train.py            # Script for training the model
│   ├── dataset.csv         # Sample dataset for training
│   ├── svm_model.pkl       # Trained SVM model (saved using joblib)
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

---

## Prerequisites

Make sure you have the following installed on your system:

- **Python 3.8+**
- **pip**

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/Spam-Classification-Project.git
   cd Spam-Classification-Project
   ```

2. **Set Up a Virtual Environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### 1. Train the Model

Run the `train.py` script to train the model using the provided dataset:

```bash
python model/train.py
```

Make sure the dataset (`dataset.csv`) is in the correct format:
- **Columns**:
  - `text`: Input text data.
  - `label`: Corresponding class labels.

### 2. Start the API Server

Run the FastAPI server using Uvicorn:

```bash
uvicorn app.main:app --reload --port 8080
```

The server will be available at `http://127.0.0.1:8080`.

### 3. Test the API

#### Welcome Endpoint

- **URL**: `http://127.0.0.1:8080/`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "message": "Welcome to the SVM Text Classification API"
  }
  ```

#### Predict Endpoint

- **URL**: `http://127.0.0.1:8080/predict/`
- **Method**: `POST`
- **Query Parameters**:
  - `text` (string): The input text to classify.
- **Example**:
  ```bash
  curl -X POST "http://127.0.0.1:8080/predict/?text=This%20is%20an%20example%20text"
  ```
- **Response**:
  ```json
  {
    "status": "success",
    "data": {
      "prediction": "class_label",
      "probability": [0.8, 0.2]
    }
  }
  ```

---

## Monitoring Prediction Time

The `monitor.py` file provides a decorator (`monitor_prediction_time`) that logs the execution time of the prediction function. Logs will appear in the terminal or can be redirected to a file.

---

## Dependencies

All dependencies are listed in the `requirements.txt` file. They include:

- **FastAPI**: For building the web API.
- **Uvicorn**: For running the ASGI server.
- **scikit-learn**: For model training and prediction.
- **joblib**: For saving and loading the trained model.
- **pandas**: For data manipulation.

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## Testing

Use **Swagger UI** to test the API:

1. Open `http://127.0.0.1:8080/docs` in your browser.
2. Test the `/predict/` endpoint with a sample text input.

---

## License

This project is licensed under the [MIT License](LICENSE).
