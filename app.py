from flask import Flask, render_template, request
from weather_fetcher_cwa import fetch_weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    city = "臺北市"
    if request.method == "POST":
        city = request.form["city"]

    forecast = fetch_weather(city)
    return render_template("index.html", city=city, forecast=forecast)

if __name__ == "__main__":
    app.run(debug=True)
