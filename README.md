# api_final
api final

### Что это вообще такое.

Учебное API для учебного блога.
Есть полное CRUD для постов и комментраиев к ним.
CR для подписок, и R для групп, соответственно.
Так же присутствует авторизация и аутентификация по JWT токену - функционал анонимного пользователся ограничен, нельзя менять чужой контент.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram2plus.git
```

```
cd kittygram2plus
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
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

### Примеры запросов:

http://127.0.0.1:8000/api/v1/posts/ - ключ к постам
http://127.0.0.1:8000/api/v1/posts/{id}/ - конкретный пост

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/ - все комменты
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/ - конкретный коммент

http://127.0.0.1:8000/api/v1/groups/ - группы

http://127.0.0.1:8000/api/v1/follow/ - подписки

http://127.0.0.1:8000/api/v1/jwt/create/,
http://127.0.0.1:8000/api/v1/jwt/refresh/,
http://127.0.0.1:8000/api/v1/jwt/verify/ - для авторизации