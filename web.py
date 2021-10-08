from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


def move_forward():
    # Moving forward code
    print("Moving Forward...")


if __name__ == '__main__':
    app.run()
