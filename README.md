# api_final
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/name/api_final_yatube.git
cd api_final_yatube
```

### Cоздать и активировать виртуальное окружение:

```python -m venv venv
source venv/Scripts/activate
```

### Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Выполнить миграции:

```
cd yatube_api
python manage.py migrate
```

### Запустить проект:

```
python manage.py runserver
```

### Примеры запросов:

POST - запрос на добавление новой публикации в группу.
#### POST http://localhost:port/api/v1/posts/

``json
{
    "text": "В ближайшем будующем будут править роботы.",
    "group": 1
}```


#### Ответ:

``json
{
    "id": 2,
    "author": "user_name",
    "text": "В ближайшем будующем будут править роботы.",
    "pub_date": "2023-09-08T14:46:41.494905Z",
    "image": null,
    "group": 1
}```
