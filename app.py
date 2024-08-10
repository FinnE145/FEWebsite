from flask import Flask, render_template

app = Flask(__name__)

print("Running app")

@app.route("/")
def index():
    return render_template("underConstruction.html")

@app.route("/testDB")
def testDB():
    return "test db"

def run():
    app.run()

if __name__ == "__main__":
    app.run()
