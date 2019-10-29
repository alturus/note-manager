## Тестовое задание "Менеджер заметок"
Web-приложение для хранения заметок. Каждая заметка имеет заголовок, содержимое,
категорию и может быть помечена как “избранная”. Интерфейс приложения должен позволять
выполнять поиск/сортировку заметок пользователя по различным критериям.

## Использование
### Описание API

Users

HTTP-метод | Ресурс | Описание | Auth.
--- | --- | --- | ---
GET | /api/v1/users/ | Получить список пользователей | +
POST | /api/v1/users/ | Создание пользователя | -

Categories

HTTP-метод | Ресурс | Описание | Auth.
--- | --- | --- | ---
GET | /api/v1/categories/ | Получить список категорий | -
POST | /api/v1/categories/ | Создать категорию | +
GET | /api/v1/categories/{category_uuid}/ | Инф-ция о категории | -
PUT | /api/v1/categories/{category_uuid}/ | Изменить категорию | +
PATCH | /api/v1/categories/{category_uuid}/ | Изменить категорию | +
DELETE | /api/v1/categories/{category_uuid}/ | Удалить категорию | +

Notes

HTTP-метод | Ресурс | Описание | Auth.
--- | --- | --- | ---
GET | /api/v1/notes/ | Получить список заметок | +
POST | /api/v1/notes/ | Создать заметку | +
GET | /api/v1/notes/{note_uuid}/ | Инф-ция о заметке | +
PUT | /api/v1/notes/{note_uuid}/ | Изменить заметку | +
PATCH | /api/v1/notes/{note_uuid}/ | Изменить заметку | +
DELETE | /api/v1/notes/{note_uuid}/ | Удалить заметку | +

_Auth. - требуется наличие JWT-авторизации_

#### Регистрация нового пользователя
POST `/api/v1/users/`

Параметры запроса:

Имя | Тип | Описание
--- | --- | ---
username | string | Имя пользователя
password | string | Пароль

Success 200:

Имя | Тип | Описание
--- | --- | ---
username | string | Имя пользователя
access | string | Access-токен
refresh | string | Refresh-токен

Пример запроса:
```
curl -X POST \
  http://vps561804.ovh.net:8080/api/v1/users/ \
  -H 'Content-Type: application/json' \
  -d '{
	"username": "demo",
	"password": "demopass"
}'
```

Пример ответа:
```
{
    "username": "demo",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcyNDA4Nzg4LCJqdGkiOiI3YjFhY2Q3YjMwMjQ0YTU3ODRlZDk5ODk1OGJmNmEzYyIsInVzZXJfaWQiOjQ1LCJpc19hZG1pbiI6ZmFsc2V9.lLwr-0fBJjs3BIy8XhAzgMDQSI4JiJI-jfUyhl72_dI",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU3MzUzMTk4OCwianRpIjoiMzJjZDM0MGRkYWViNDE5ODk2NjFjYzQwZTk5NDkxMjgiLCJ1c2VyX2lkIjo0NSwiaXNfYWRtaW4iOmZhbHNlfQ.j76UeL0p9EeJKne8-gT_kndlRHi2cEYshbOtV4VMpX4"
}
```

#### Авторизация пользователя
Для операций требующих авторизации пользователя необходимо использование валидного токена JSON Web Token (JWT).

Пример токена:
```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcyNDA4Nzg4LCJqdGkiOiI3YjFhY2Q3YjMwMjQ0YTU3ODRlZDk5ODk1OGJmNmEzYyIsInVzZXJfaWQiOjQ1LCJpc19hZG1pbiI6ZmFsc2V9.lLwr-0fBJjs3BIy8XhAzgMDQSI4JiJI-jfUyhl72_dI
```

##### Получение токенов для зарегистрированного пользователя
POST `/api/v1/users/token/`

Параметры:

Имя | Тип | Описание
--- | --- | ---
username | string | Имя пользователя
password | string | Пароль

Success 200:

Имя | Тип | Описание
--- | --- | ---
access | string | Access-токен
refresh | string | Refresh-токен

Пример запроса:
```
curl -X POST \
  http://vps561804.ovh.net:8080/api/v1/users/token/ \
  -H 'Content-Type: application/json' \
  -d '{
	"username": "demo",
	"password": "demopass"
}'
```

Пример ответа:
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU3MzUzMzIzMiwianRpIjoiNTZiOTU0YjU2YjMxNGNhNGIxMDFjZDIyZDU0N2JhZmQiLCJ1c2VyX2lkIjoyfQ.3DxnNR2-c5hnde9g2fmGTrwYB24KVzKLhbD6Iu9DZ_0",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcyNDEwMDMyLCJqdGkiOiI2Zjg0ZDEyODdkNDY0OTg3YjlhMWExYzgxNmQxNmE4MCIsInVzZXJfaWQiOjJ9.a-Tu40xj2GBgJp8xVZ1Nqjfck7ryHGHUVkaDEE0Y4OA"
}
```

#### Получение списка заметок
GET `/api/v1/notes/`

Параметры запроса:

Имя | Тип | Описание
--- | --- | ---
ordering | string | Сортировка по полю
title | string | Фильтр по заголовку
category | string | Фильтр по категории
is_published | boolean | Фильтр по признаку "опубликована"
is_favorited | boolean | Фильтр по признаку "избранная"

Success 200:

Имя | Тип | Описание
--- | --- | ---
count | integer | Кол-во найденных заметок
next | string | URL на следующую страницу
previous | string | URL на предыдущую страницу
results | array | Массив с объектами заметок

Описание объекта в results

Имя | Тип | Описание
--- | --- | ---
url | integer | URL на запрос по заметке
uuid | uuid | Идентификатор заметки
owner | string | username создателя заметки
category | string | Наименование категории
title | string | Заголовок заметки
created | string | Дата и время создания заметки
modified | string | Дата и время последнего изменения
is_favorited | boolean | Признак "избранная" заметка
is_published | boolean | Признак "опубликованная" заметка

Пример запроса:
```
curl -X GET \
  'http://vps561804.ovh.net:8080/api/v1/notes/?ordering=-created&is_published=true&category=ca25b9a2-1306-4b32-a929-e302e4f84318' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcyNDExOTQ3LCJqdGkiOiJiY2ZkMjZhMjU0NDA0NTM5YTg3MDBmZTQzYTY0OTBiOCIsInVzZXJfaWQiOjN9.d_8yEonTGNuWqVIq0jTbv8VZ2lnDUg1taxeuAg33b2E' \
  -H 'Content-Type: application/json'
```

Пример ответа:
```
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "url": "http://vps561804.ovh.net/api/v1/notes/ed593d7f-d2ab-4bb9-b15a-f02f8924846d/",
            "uuid": "ed593d7f-d2ab-4bb9-b15a-f02f8924846d",
            "owner": "demo",
            "category": "Ссылка",
            "title": "https://github.com/alturus/",
            "created": "2019-10-25 04:11:36",
            "modified": "2019-10-25T04:11:43.665733Z",
            "is_favorited": false,
            "is_published": true
        },
        {
            "url": "http://vps561804.ovh.net/api/v1/notes/6193f896-c30f-4549-84a2-5cc904af0661/",
            "uuid": "6193f896-c30f-4549-84a2-5cc904af0661",
            "owner": "demo",
            "category": "Ссылка",
            "title": "Python 3.8.0 documentation",
            "created": "2019-10-25 04:01:51",
            "modified": "2019-10-25T04:10:03.331202Z",
            "is_favorited": true,
            "is_published": true
        }
    ]
}
```

#### Создание заметки
POST `/api/v1/notes/`

Параметры запроса:

Имя | Тип | Описание | Обязательное
--- | --- | --- | ---
category | string | Наименование категории | +
title | string | Заголовок заметки | +
body | string | Содержание заметки | -
is_favorited | boolean | Признак "избранная" заметка | -
is_published | boolean | Признак "опубликованная" заметка | -

Пример запроса:
```
curl -X POST \
  http://vps561804.ovh.net:8080/api/v1/notes/ \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTcyNDE1NDg5LCJqdGkiOiIxNjk4MTg1NGE1NTI0YjE4OTIwNzU3NmQ5Y2YwMGE4ZCIsInVzZXJfaWQiOjJ9.-5hXnfUS4iioxx0UO51blTZ-bI8y8akWrJcSZ1MqjIs' \
  -H 'Content-Type: application/json' \
  -d '{
	"category": "Заметка",
	"title": "Заметка 1",
	"body": "Текст заметки",
	"is_favorited": true,
	"is_published": true
}'
```

Пример ответа:
```
{
    "url": "http://vps561804.ovh.net:8080/api/v1/notes/b33d3cc3-58d1-41ac-9a17-14ab6e69b039/",
    "uuid": "b33d3cc3-58d1-41ac-9a17-14ab6e69b039",
    "owner": "demo",
    "category": "Заметка",
    "title": "Заметка 1",
    "body": "Текст заметки",
    "created": "2019-10-29 06:12:08",
    "modified": "2019-10-29T06:12:08.580020Z",
    "is_favorited": true,
    "is_published": true
}
```

#### Получение списка категорий
GET `/api/v1/categories/`

Success 200:

Имя | Тип | Описание
--- | --- | ---
url | string | URL на категорию
uuid | string | Идентификатор категории
name | string | Наименование категории
description | string | Описание категории

Пример запроса:
```
curl -X GET http://vps561804.ovh.net:8080/api/v1/categories/
```

Пример ответа:
```
[
    {
        "url": "http://vps561804.ovh.net/api/v1/categories/89014ece-579e-4833-9454-e836b5cbfecd/",
        "uuid": "89014ece-579e-4833-9454-e836b5cbfecd",
        "name": "Заметка",
        "description": "Простая заметка"
    },
    {
        "url": "http://vps561804.ovh.net/api/v1/categories/8c7b2b2a-8d84-4f6b-a196-38a0ae37f8da/",
        "uuid": "8c7b2b2a-8d84-4f6b-a196-38a0ae37f8da",
        "name": "TODO",
        "description": "Задача для выполнения"
    },
    {
        "url": "http://vps561804.ovh.net/api/v1/categories/ca25b9a2-1306-4b32-a929-e302e4f84318/",
        "uuid": "ca25b9a2-1306-4b32-a929-e302e4f84318",
        "name": "Ссылка",
        "description": "Ссылка на внешний источник"
    },
    {
        "url": "http://vps561804.ovh.net/api/v1/categories/802298be-3ce8-4416-ae39-fc5652e3a5e8/",
        "uuid": "802298be-3ce8-4416-ae39-fc5652e3a5e8",
        "name": "Памятка",
        "description": "NB"
    }
]
```

## Установка

TODO
