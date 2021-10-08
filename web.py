import os.path
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        systemPath = '/Users/mishrilalchhaparia/Projects/ImgEnh'    # Change this path - Hosting
        f.save(systemPath + app.config['UPLOAD_FOLDER'] + '/' + secure_filename(f.filename))
        return 'file uploaded successfully'


if __name__ == '__main__':
    app.run()
