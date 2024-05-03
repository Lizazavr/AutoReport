
Установка AutoReport в существующий проект в качестве подсистемы с использованием технологии Blueprint.
1. Выполнить clone репозитория в существующий проект:
```
cd web/imit
git clone https://github.com/Autoreport-Dev-Team/autoreport
```
3. Перейти в директорию проекта:
''''cd autoreport''''
4. Установить зависимости из requirements.txt:
''''pip3 install -r requirements.txt''''
5. В конфигурационном файле autoreport_config.py установить путь до файла с путями до файлов учебных планов:
''''CONFIG_PLAN_FILES_PATH = "path/to/config.txt"''''
6. Вернуться в директорию исходного проекта:
''''cd ..''''
7. В файле, где инициализируется экземпляр flask, импортировать autoreport:
''''from autoreport.autoreport import autoreport''''
8. И подключить подсистему autoreport к проекту:
''''app.register_blueprint(autoreport, url_prefix='/autoreport'''''
