from os import getpid
from flask import Flask, render_template

app = Flask(__name__)

print("Running app")

with open("app.pid", "w") as f:
    f.write(str(getpid()))

@app.route("/")
def index():
    return render_template("underConstruction.html")

@app.route("/testDB")
def testDB():
    return "test db"

def run():
    app.run()

if __name__ == "__main__":
    app.run(port=50000)
