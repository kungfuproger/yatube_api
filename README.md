# Yatube API

API для блога Yatube.

Функционал - CRUD для постов и комментов, CR-- для подписок и -R-- для групп.

Авторизация и аутентификация - по JWT токену.

Права доступа - доступ анонимного пользователя ограничен, пользователям нельзя изменять чужие записи.

### Как запустить проект:

Клонировать репозиторий.

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### ЭНДПОИНТЫ

1. `admin/` - админ-панель Django.
2. `redoc/` - документация Redoc по API проекта.
3. `api/v1/<URL>/` - функционал и URL's действий в соответствии с Redoc документацией.
