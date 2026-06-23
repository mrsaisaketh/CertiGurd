import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Dummy dataset (you can expand later)
texts = [
    "Bachelor of Technology University Certificate Roll No",
    "Government Approved Degree Certificate",
    "Fake certificate download template",
    "Editable certificate sample photoshop",
]

labels = [1, 1, 0, 0]  # 1 = original, 0 = fake

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

joblib.dump(model, "certificate_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved.")