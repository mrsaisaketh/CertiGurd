import joblib

model = joblib.load("certificate_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_certificate(text):
    X = vectorizer.transform([text])
    prob = model.predict_proba(X)[0][1]
    prediction = model.predict(X)[0]
    return prediction, prob