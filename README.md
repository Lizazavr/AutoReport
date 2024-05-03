AutoReport - это сервис, предназначенный для автоматизации процесса формирования отчётности студентов. Сервис предоставляет работникам дирекции института удобный и эффективный способ создания и предоставления информации о предметах за выбранный год и семестр. Является расширением функциональности сайта ИМИТ ПетрГУ.

Установка AutoReport в существующий проект в качестве подсистемы с использованием технологии Blueprint.
1. Выполнить clone репозитория в существующий проект:
```
cd web/imit
git clone https://github.com/Autoreport-Dev-Team/autoreport
```
3. Перейти в директорию проекта:
4. ```
   cd autoreport
   ```
5. Установить зависимости из requirements.txt:
```
pip3 install -r requirements.txt
```
6. В конфигурационном файле autoreport_config.py установить путь до файла с путями до файлов учебных планов:
```
CONFIG_PLAN_FILES_PATH = "path/to/config.txt"
```
7. Вернуться в директорию исходного проекта:
```
cd ..
```
8. В файле, где инициализируется экземпляр flask, импортировать autoreport:
```
from autoreport.autoreport import autoreport
```
9. И подключить подсистему autoreport к проекту:
```
app.register_blueprint(autoreport, url_prefix='/autoreport'
```
