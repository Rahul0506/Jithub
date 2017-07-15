import os
import classifier
import MySQLdb as mysql
import backend_manager
from flask import Flask, render_template, request, url_for, redirect, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '.\\resources\\upload'
DATASET_FOLDER = '.\\resources\\txt_sentoken'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DATASET_FOLDER'] = DATASET_FOLDER
db_keys = []
global text_clf

app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default',
))

text_clf = classifier.train_model(app.config['DATASET_FOLDER'])

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
            return redirect(url_for('result_upload', filename=filename))
    return render_template('upload.html')

#Results page
@app.route('/result_upload')
def result_upload():
    filename = os.path.join(app.config['UPLOAD_FOLDER'], request.url.split('=')[-1])

    file_handle = open(filename)
    data = file_handle.read()
    file_handle.close()

    result = classifier.predict(text_clf, data)
    if result[0]:
        result = 'positive'
    else:
        result = 'negative'
    return render_template('result_upload.html', result=result)

#Form data page
@app.route('/link', methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        database_name = request.form['database_name']
        table_name = request.form['table_name']
        user_name = request.form['user_name']
        password = request.form['password']
        global db_keys
        db_keys = [database_name, table_name, user_name, password]
    return redirect(url_for('link_loading'))

#Link being loaded
@app.route('/link_loading')
def link_loading():
    db = mysql.connect(host="127.0.0.1", port=3306, user=db_keys[2], passwd=db_keys[3], db=db_keys[0])
    input_dataset = db_link(db)
    pass_to_classifier(input_dataset, db)
    return render_template('link_loading.html')
