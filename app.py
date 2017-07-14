import os
import classifier
from flask import Flask, render_template, request, url_for, redirect, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '.\\resources\\upload'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

#Index page
@app.route('/index')
def index():
    return render_template('index.html')

#Link page
@app.route('/link')
def link():
    return render_template('link.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_results', filename=filename))
    return render_template('upload.html')

#Results page
@app.route('/upload_results')
def upload_results():
    #clf = classifier.init_model('.\\resources\\txt_sentoken')
    filename = os.path.join('.\\resources\\upload', request.url.split('=')[-1])
    #return classifier.predict_on(clf, filename)
    return 'lol'
