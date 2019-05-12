from flask import Flask, render_template, request
from visual import stats

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    return render_template("mainpage.html")
    # line_chart.render_in_browser()

@app.route("/stats", methods=["GET", "POST"])
def build():
    chart = stats()
    return chart.render_response()


if __name__ == "__main__":
    app.run(debug=True)