import pickle  # to load the pickle file
from flask import (
    Flask,
    request,
    app,
    jsonify,
    url_for,
    render_template,
)  # to create web application
import numpy as np
import pandas as pd

app = Flask(__name__)

# loading the model
model = pickle.load(open("boston_model.pkl", "rb"))
scalar = pickle.load(open("scaling.pkl", "rb"))


@app.route("/")  # route in url -- home page
def home():
    return render_template(
        "home.html"
    )  # by default when app is triggered it will redirected to home.html page


@app.route("/predict_api", methods=["POST"])
def predict_api():
    data = request.json["data"]
    print(data)
    print(np.array(list(data.values())).reshape(1, -1))
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    output = model.predict(new_data)
    print(output[0])
    return jsonify(output[0])


@app.route("/predict", methods=["POST"])
def predict():
    data = [float(x) for x in request.form.values()]
    data = np.array(data).reshape(1, -1)
    data = scalar.transform(data)
    print(data)
    output = model.predict(data)[0]
    return render_template(
        "home.html",
        prediction_text="The Predicted house price value is {}".format(output),
    )


if __name__ == "__main__":
    app.run(debug=True)
