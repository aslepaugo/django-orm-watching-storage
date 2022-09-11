# Пульт охраны банка

Веб-приложение для олтслеживания пропусков при доступе в хранилище банка. Помогает отследить историю нахождения сотрудников в хранилище для послеующего анализа, а также просматривать, кто находится в хранилище в данный момент и как долго.

## Как установить

1. Python3 должен быть уже установлен.

2. Склонировать проект и установить зависимости.

```bash
git clone https://github.com/aslepaugo/django-orm-watching-storage
cd django-orm-watching-storage
# Activate virtual environment
pip install -r requirements.txt
```

3. Настройки подключения к базе данных а также настройка режима отладки (свойство `DEBUG`) должны находиться в файле .env.

```bash
DB_ENGINE = YOUR_DB_ENGINE 
DB_HOST = YOUR_DB_HOST
DB_PORT = DB_PORT
DB_NAME = DB_NAME
DB_USER = DB_USER
DB_PASSWORD = DB_PASSWORD
DEBUG = False|True
SECRET_KEY = YOUR_UNIQUE_SECRET_KEY
ALLOWED_HOSTS = [YOURLIST, OF, ALLOWED, HOSTS]
```

## Пример запуска

```bash
python manage.py runserver 8000
```

Далее перейти по адресу <http://127.0.0.1:8000/>

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
