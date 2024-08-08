from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("underConstruction.html")

@app.route("/testDB")
def testDB():
    return "test db"

if __name__ == "__main__":
    app.run()
