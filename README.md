# House Price Prediction

A Machine Learning project that predicts house prices based on property features. The project includes a FastAPI backend and an HTML/CSS/JavaScript frontend.

---

## Project Overview

This project predicts house prices using a trained Machine Learning model.

The user enters house details such as:

- Carpet Area
- Floor Number
- Bathrooms
- Balconies
- Location
- Furnishing
- Transaction Type
- Ownership
- Facing Direction

The application sends the data to the FastAPI backend, which loads the trained model and returns the predicted house price.

---

## Architecture

```
User
   │
   ▼
Frontend (HTML/CSS/JavaScript)
   │
HTTP Request (POST /predict)
   │
   ▼
FastAPI Backend
   │
Machine Learning Model (.pkl)
   │
Prediction
   ▼
Frontend displays the predicted price
```

---

# Tech Stack

- Python
- FastAPI
- Scikit-learn
- Pandas
- Joblib
- HTML
- CSS
- JavaScript

---

# Project Structure

```
House-Price-Prediction
│
├── backend
│   ├── main.py
│   ├── requirements.txt
│   └── locations.json
│
├── frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
└── README.md
```

---

# Dataset

Dataset Source:

https://www.kaggle.com/

Download the housing dataset from Kaggle and place it in your project before training the model.

---

# Backend Setup

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

Open the frontend folder and run the HTML page using Live Server in VS Code.

```
frontend/index.html
```

---

# API Reference

## GET /

Returns API status.

Example

```bash
curl http://127.0.0.1:8000/
```

---

## GET /locations

Returns all available locations.

```bash
curl http://127.0.0.1:8000/locations
```

---

## POST /predict

Example

```bash
curl -X POST http://127.0.0.1:8000/predict \
-H "Content-Type: application/json" \
-d '{
"carpet_area_sqft":1200,
"floor_num":3,
"Bathroom":2,
"Balcony":1,
"location_grouped":"bangalore",
"Furnishing":"Semi-Furnished",
"Transaction":"Resale",
"Ownership":"Freehold",
"facing":"East"
}'
```

Example Response

```json
{
  "Predicted Price": 10734200
}
```

---

# Model Performance

Replace these values with your model evaluation metrics.

| Metric | Value |
|---------|-------|
| MAE | ... |
| RMSE | ... |
| R² Score | ... |

---

# Screenshots

Add screenshots here.

Example:

- Home Page
- Prediction Result
- Swagger API

---

# Author

**Yara Faleh Tawfek**

Machine Learning Project
