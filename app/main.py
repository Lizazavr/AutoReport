import datetime

from flask import Flask, render_template, request
from flask import jsonify, render_template, send_file
from datetime import date
from flask import Flask, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from datetime import datetime
from wtforms.validators import DataRequired
from flask import flash, get_flashed_messages, redirect

UPLOAD_FOLDER = 'doc'
ALLOWED_EXTENSIONS = {'doc'}

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'your_secret_key'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

path = None
user_year = None
nameFile = None
data = None
type_report = None
name_report = None


class ReportForm(FlaskForm):
    user_year = SelectField('Год', choices=[(str(year), str(year)) for year in range(datetime.now().year, datetime.now().year + 5)], validators=[DataRequired()])
    semester = SelectField('Семестр', choices=[('fall', 'Осенний'), ('spring', 'Весенний')], validators=[DataRequired()])
    update_bd = SubmitField('Обновить данные об учебных планах')
    form_report = SubmitField('Сформировать отчёт')
    dowland_report = SubmitField('Загрузить отчёт')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ReportForm()
    if request.method == 'POST':
        print("post")
        if form.validate_on_submit():
            print("submit")
            if form.update_bd.data:
                print("db")
                find_db()
                return redirect(url_for('index'))
            elif form.form_report.data:
                pass
            elif form.dowland_report.data:
                pass
            else:
                # Обработка других случаев
                pass
    return render_template('main.html', form=form, now_year=datetime.now().year)

def find_db():
    print("db")
    # Логика обновления данных об учебных планах
    show_popup_message('Данные об учебных планах обновлены', 'success')

def show_popup_message(message, type):
    # Функция для вывода всплывающего сообщения
    if type == 'success':
        # Вывод всплывающего сообщения в правом нижнем углу светло-желтого цвета с границей
        flash(message, 'success')
    elif type == 'warning':
        # Вывод всплывающего сообщения в правом нижнем углу светло-желтого цвета с границей
        flash(message, 'warning')

@app.route('/report', methods=["POST", "GET"])
def web_report():
    """
    Взаимосвязь между клиентской частью и модулем funcs.py.
    Обрабатывает POST запросы, отправленные с клиентской части

    @return: вызов функций или render_template('main.html')
    """
    global year, term, type_report, name_report
    if request.method == 'POST':
        print("post")
        values = request.form.get('type')
        if values == 'dowland_report':
            print("Скачивание отчёта")
            # return download_report()
        elif values == 'upload_report':
            print("Загрузка отчёта")
            file = request.form.get('file')
            # return load_changed_report(year, term, file)
        elif values == 'upload_report':
            print("Загрузка отчёта")
            file = request.form.get('file')
            # return load_changed_report(year, term, file)
    return render_template('report.html')

if __name__ == "__main__":
    app.run(debug=True)