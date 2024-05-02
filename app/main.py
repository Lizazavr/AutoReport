from flask import Flask, render_template, request
from flask import jsonify, render_template, send_file
from flask import send_from_directory, flash
from docx import Document
from flask import redirect, url_for
from htmldocx import HtmlToDocx
from collections import defaultdict
import mariadb
import sys
import os
import unittest
import webbrowser
import datetime

from werkzeug.utils import secure_filename
from coverage import coverage

UPLOAD_FOLDER = 'doc'
ALLOWED_EXTENSIONS = {'doc'}

app = Flask(__name__, template_folder='../templates')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

year = None
term = None
path = None
user_year = None
nameFile = None
data = None
type_report = None
name_report = None


@app.route('/', methods=["POST", "GET"])
def index():
    """
    Взаимосвязь между клиентской частью и модулем funcs.py.
    Обрабатывает POST запросы, отправленные с клиентской части

    @return: вызов функций или render_template('main.html')
    """
    global year, term, type_report, name_report
    if request.method == 'POST':
        print("post")
        values = request.form.get('type')
        if values == 'upload':
            print("Обновление бд")
            #return update_curriculum()
            return jsonify({"success": False, "errortype": "db no connection", "message": "Нет ответа от базы данных."})
        elif values == 'report':
            print("Формирование отчёта")
            type_report = "gen"
            year = request.form.get('year')
            term = request.form.get('term')
            # pract = generate_report(year, term)
            return jsonify({"22102": "учебная", "22202": "производственная", "22301": "учебно-ознакомительная", "22303": "учебно-ознакомительная", "22305": "учебно-ознакомительная"})
        elif values == 'gen_report':
            print("Генерация отчёта")
            pract = request.form.get('pract')
            # return generate_report(year, term, pract)
            return render_template("report.html", type_report=type_report, name_report=name_report)
        elif values == 'gen_report':
            print("Загрузка отчёта")
            type_report = "upload"
            file = request.form.get('file')
            # return load_new_report(year, term, file)
            return render_template("report.html", type_report=type_report, name_report=name_report)


    return render_template('main.html')

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