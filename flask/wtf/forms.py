from flask import Flask, render_template, redirect, url_for
from flask.ext.wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap
import os


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class PhotoForm(FlaskForm):
    photo = FileField(validators=[FileRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['UPLOAD_FOLDER'] = app.root_path
bootstrap = Bootstrap(app)


# обычный шаблон
@app.route('/nameform', methods=('GET', 'POST'))
def nameform():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        return redirect('/')
    return render_template('nameform.html', form=form)


# шаблон bootstrap
@app.route('/bsform', methods=('GET', 'POST'))
def bsform():
    form = NameForm()
    return render_template('bsform.html', form=form)


# загрузка файлов
@app.route('/upload', methods=('GET', 'POST'))
def upload():
    form = PhotoForm()
    if form.validate_on_submit():
        f = form.photo.data
        file_name = secure_filename(f.filename)
        f.save(os.path.join(
            app.config['UPLOAD_FOLDER'], 'upload', file_name
        ))
        return redirect('/')
    return render_template('upload.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
