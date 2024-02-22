from flask import Flask, request, render_template
import pickle
import sklearn

# load the model
with open('cb.pkl', 'rb') as file:
    model = pickle.load(file)

with open('LabelEncode.pkl', 'rb') as file:
    enc = pickle.load(file)

with open('Scaling.pkl', 'rb') as file:
    scl = pickle.load(file)

# create a flask application
app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    # read the file contents and send them to client
    return render_template('form.html')


@app.route("/classify", methods=["POST"])
def classify():
    # get the values entered by user
    print(request.form)

    airline = (request.form.get("airline"))
    source_city = (request.form.get("source_city"))
    departure_time = (request.form.get("departure_time"))
    stops = (request.form.get("stops"))
    flight_class = (request.form.get("flight_class"))
    destination_city = (request.form.get("destination_city"))
    arrival_time = (request.form.get("arrival_time"))
    days_left = float(request.form.get("days_left"))



    price = model.predict([
        [arrival_time, source_city, departure_time, stops, arrival_time, destination_city, flight_class, days_left]
    ])

    # price = model.predict([[3, 2, 2, 2, 5, 5, 1, 1]])

    result=f"Your flight fare will be ₹. {int(price[0]) }"
    return render_template('result.html', result=result)


# start the application
app.run(host="0.0.0.0", port=8000, debug=True)
