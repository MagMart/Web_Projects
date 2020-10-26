from flask import Flask

app = Flask(__name__)

@app.route("/")
def goodbunny():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=False)
