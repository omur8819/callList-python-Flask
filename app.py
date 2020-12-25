from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "HomePage"

@app.route("/search")
def search():
    pass

if __name__ == "__main__":
    app.run(debug = True) 