from os import getpid
from flask import Flask, render_template

app = Flask(__name__)

print("Running app")

with open("app.pid", "w") as f:
    f.write(str(getpid()))
    print("PID:", getpid())

@app.route("/")
def index():
    return render_template("underConstruction.html")

def run():
    app.run()

if __name__ == "__main__":
    app.run(port=50000)
