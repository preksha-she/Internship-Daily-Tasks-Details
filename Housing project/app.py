from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model safely
try:
    model = pickle.load(open("model.pkl", "rb"))
except Exception as e:
    print("Error loading model:", e)
    model = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if model is None:
            return render_template("index.html", prediction_text="Model not loaded!")

        # Get input values safely
        area = float(request.form.get("area", 0))
        bedrooms = float(request.form.get("bedrooms", 0))
        bathrooms = float(request.form.get("bathrooms", 0))

        # Make prediction
        features = np.array([[area, bedrooms, bathrooms]])
        prediction = model.predict(features)

        return render_template(
            "index.html",
            prediction_text=f"Predicted Price: {prediction[0]:,.2f}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}"
        )

if __name__ == "__main__":
    app.run(debug=True)