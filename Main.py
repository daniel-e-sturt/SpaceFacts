from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(app.root_path, "home.html")

@app.route("/All%20Planets.html")
@app.route("/All Planets.html")
def planets():
    return send_from_directory(app.root_path, "All Planets.html")

if __name__ == "__main__":
    app.run(debug=True)
