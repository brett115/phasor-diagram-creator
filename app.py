from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World! This is a simple Python website."


@app.route("/about")
def about():
    return "<h2>About Page</h2><p>This is our simple about page.</p>"


if __name__ == "__main__":
    app.run(debug=True)
