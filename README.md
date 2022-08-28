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

3. Для подключения к Базе Данных необходимо заполнить ключи в файле [settings.py](/project/settings.py)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '{MY_HOST}',
        'PORT': '{PORT}',
        'NAME': '{DB_NAME}',
        'USER': '{USER_NAME}',
        'PASSWORD': '{PASSWORD}',
    }
}
```

Для производственного развертывания необходимо изменить значения:

```python
SECRET_KEY = '{GENERATE_SECRETE_KEY}'
DEBUG = False
```

## Пример запуска

```bash
python manage.py runserver 8000
```

Далее перейти по адресу <http://127.0.0.1:8000/>

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
