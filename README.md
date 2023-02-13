# API yatube

### Описание
Yatube мини социальная сеть.

### Технологии
- Python3.9
- pip 22.0.4
- Django==3.2.16
- djangorestframework==3.12.4
- djangorestframework-simplejwt==4.7.2
- Pillow==9.3.0
- PyJWT==2.1.0
- requests==2.26.0

### Настройка проекта (Linux)
- В терминале:

```
git clone https://github.com/vitalikShcerbakov/api_final_yatube.git
```

- Перейти в каталог с проектом:

```
cd api_final_yatube
```

- Cозать вертуальное окружение venv:

```
python3.9 -m venv venv
```

- Активируем виртуальное окружение:

```
source venv/bin/activate
```

- Установить зависимостей:

```
pip install -r requirements.txt
```

### Запуск проекта в dev-режиме

- В папке с файлом manage.py выполните команды:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```

# Примеры:
### Список эндпоинтов
> GET запрос
```
http://127.0.0.1:8000/api/v1/
```
> Ответ
```
{
    "groups": "http://127.0.0.1:8000/api/v1/groups/",
    "posts": "http://127.0.0.1:8000/api/v1/posts/",
    "follow": "http://127.0.0.1:8000/api/v1/follow/"
}
```
### Получение публикаций
- Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.
>GET запрос
```
http://127.0.0.1:8000/api/v1/posts/
```
>Oтвет
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
### Создание публикации
- Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.

> POST запрос content type application/json

 - http://127.0.0.1:8000/api/v1/posts/
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
>Ответ (Удачное выполнение запроса - 201)
```
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```
>Ответ (Отсутствует обязательное поле в теле запроса 400)
```
{
  "text": [
    "Обязательное поле."
  ]
}
```
>Ответ (Запрос от имени анонимного пользователя 401)
```
{
  "detail": "Учетные данные не были предоставлены."
}
```
### Обновление публикации
- Обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.

> PUT запрос content type application/json

- http://127.0.0.1:8000/api/v1/posts/{id}/

PATH PARAMETERS
| id | integer |
| ------ | ------ |
| required | id публикации |

```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
>Ответ (Удачное выполнение запроса - 201)
```
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```
>Ответ (Отсутствует обязательное поле в теле запроса 400)
```
{
  "text": [
    "Обязательное поле."
  ]
}
```
>Ответ (Запрос от имени анонимного пользователя 401)
```
{
  "detail": "Учетные данные не были предоставлены."
}
```
### Авторы
Виталий Щербаков
