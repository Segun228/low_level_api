# Проект API с тремя приложениями

## Описание API

В проекте реализовано три отдельных API с разными подходами:

1. **`api`**  
   - Без использования ORM и встроенных классов View.  
   - Поддерживает 4 основных HTTP-метода: `GET`, `POST`, `PUT`, `DELETE`.  
   - Пример тела запроса:  
     ```json
     {
       "username": "user_name",
       "email": "test@example.com",
       "password": "securepassword123"
     }
     ```

2. **`fbv_api`**  
   - Используется Django ORM.  
   - Вьюшки реализованы в функциональном стиле (Function-Based Views).  
   - Маршруты:  
     - `/posts/`
     - `/posts/<id>/`  
     - `/regular_users/` 
     - `/regular_users/<id>/`

   - Примеры тел запросов:  
     ```json
     {
       "username": "some_name",
       "email": "new_email@example.com",
       "password": "NewSecurePassword123"
     }
     ```  

     ```json
     {
       "title": "Здесь заголовок",
       "body": "Здесь тело поста",
       "images": [
         "https://example.com/image1.jpg",
         "https://example.com/image2.jpg"
       ]
     }
     ```

3. **`cbv_api`**  
   - Используется Django ORM.  
   - Вьюшки реализованы с помощью Class-Based Views.  
   - Маршруты:  
     - `/students/` и `/students/<id>/`  
   - Пример тела запроса:  
     ```json
     {
       "first_name": "Иван",
       "second_name": "Иванов",
       "patronymic": "Иванович",
       "class_number": 10,
       "letter": "А",
       "email": "ivan.ivanov@example.com"
     }
     ```

---

## Структура проекта

```bash
.
├── api
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── fbv_api
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── cbv_api
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── low_level_api
│   ├── settings.py
│   └── urls.py
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## Запуск проекта локально

1. Клонируйте репозиторий:

```bash
git clone <URL_репозитория>
cd <название_папки_репозитория>
```

2.	Установите зависимости:

```bash
pip install -r requirements.txt
```

3.	Перейдите в директорию с файлом manage.py (корень проекта):

```bash
cd <путь_к_директории_с_manage.py>
```

4.	Запустите сервер разработки на порту 8000:

```bash
python manage.py runserver
```

5.	Доступ к API будет по адресу:

```browser
http://127.0.0.1:8000/
```