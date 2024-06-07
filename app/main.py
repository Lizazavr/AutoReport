import datetime

from flask import Flask, render_template, request
from flask import jsonify, render_template, send_file
from datetime import date
from flask import Flask, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, FileField
from datetime import datetime
from wtforms.validators import DataRequired
from flask import flash, get_flashed_messages, redirect
import os
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired

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
    report_file = FileField('Выбрать файл', validators=[DataRequired()])
    submit = SubmitField('Загрузить')

class ModalForm(FlaskForm):
    new_report = SubmitField('Новый', validators=[DataRequired()])
    current_report = SubmitField('Текущий', validators=[DataRequired()])
    no_new_report = SubmitField('Нет', validators=[DataRequired()])
    add_report = SubmitField('Да', validators=[DataRequired()])

class PracticeItemForm(FlaskForm):
    group = StringField('Группа', validators=[DataRequired()])
    practice_type = SelectField('Тип практики', choices=[('internship', 'Производственная'), ('pre-diploma', 'Преддипломная')])
    period = StringField('Период прохождения', validators=[DataRequired()])
    teacher = StringField('ФИО преподавателя', validators=[DataRequired()])

class PracticeForm(FlaskForm):
    group = StringField('Группа', validators=[DataRequired()])
    practice_type = SelectField('Тип практики',
                                choices=[('internship', 'Производственная'),
                                         ('pre-diploma', 'Преддипломная')])
    period = StringField('Период прохождения', validators=[DataRequired()])
    teacher = StringField('ФИО преподавателя', validators=[DataRequired()])
    items = FieldList(FormField(PracticeItemForm), min_entries=16)
    submit = SubmitField('Готово')

@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files['report_file']
    print(file.filename)
    if file:
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'doc', file.filename)
        file.save(file_path)
        # Здесь можно добавить дополнительную логику, например, сохранение пути к файлу в базе данных
        return redirect(url_for('index'))
    return redirect(url_for('index'))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ReportForm()
    modal_form = ModalForm()
    practic_form = PracticeForm()
    show_report_modal = False
    show_add_report_modal = False
    close_modal = False
    count_group = 4
    course_groups = {
        '1': ['101', '102', '103'],
        '2': ['201', '202', '203'],
        '3': ['301', '302', '303'],
        '4': ['401', '402', '403']
    }
    semester_name = 'Весенний'

    if request.method == 'POST':
        if form.validate_on_submit():
            print(1)
            if form.update_bd.data:
                #answer = update_curriculum()
                #answer = 'Данные об учебных планах обновлены', 'success'
                answer, type_answer = 'Ошибка обновления данных', 'warning'
                show_popup_message(answer, type_answer)
                return redirect(url_for('index'))
            elif form.form_report.data:
                pass
            elif form.dowland_report.data:
                print("windows")
                # Открываем всплывающее окно для загрузки файла
                return render_template('main.html', form=form, modal_form=modal_form, practic_form=practic_form, now_year=datetime.now().year, show_upload_modal=True, show_report_modal=show_report_modal, show_add_report_modal=show_add_report_modal, close_modal=close_modal)
            elif form.submit.data:
                file = form.report_file.data
                filename = file.filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                answer, type_answer = 'Файл успешно загружен!', 'success'
                show_popup_message(answer, type_answer)
                return redirect(url_for('index'))
            elif form.new_report.data:
                show_report_modal = True
            elif form.current_report.data:
                close_modal = True
            # Добавьте логику для использования текущего отчета
            elif form.no_new_report.data:
                close_modal = True
            # Добавьте логику для использования существующего отчета
            elif form.add_report.data:
                show_add_report_modal = True
    return render_template('main.html', form=form, modal_form=modal_form, practic_form=practic_form, \
                           now_year=datetime.now().year, show_upload_modal=False, show_report_modal=show_report_modal, \
                           show_add_report_modal=show_add_report_modal, close_modal=close_modal,
                           count_group=count_group, course_groups=course_groups, semester_name=semester_name)


def show_popup_message(message, type_message):
    # Функция для вывода всплывающего сообщения
    flash(message, type_message)


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