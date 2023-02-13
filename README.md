
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
```git clone https://github.com/vitalikShcerbakov/api_final_yatube.git```

- Перейти в каталог с проектом
```cd api_final_yatube```

- Cозать вертуальное окружение venv:
```python3.9 -m venv venv```

- Активируем виртуальное окружение.
```source venv/bin/activate```

-Установить зависимостей.
```pip install -r requirements.txt```

### Запуск проекта в dev-режиме

```
``` 
- В папке с файлом manage.py выполните команды:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```
### Авторы
Виталий Щербаков
