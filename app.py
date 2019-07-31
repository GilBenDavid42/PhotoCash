from flask import Flask, render_template

app = Flask(__name__)


# Route for main page
@app.route('/')
def hello_world():
    return render_template("index.html")


# Run the flask server
if __name__ == '__main__':
    app.run()
