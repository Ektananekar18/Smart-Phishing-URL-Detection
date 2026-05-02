
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        url = request.form.get("url")

        if url.startswith("https://"):
            result = "safe"
        else:
            result = "phishing"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)