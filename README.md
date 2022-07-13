# Test_project
Api для просмотра/создание/редактирование блюд, категорий
Поддержка авторизации с возможностью редактирование записей и для анонимов просмотр записей с поддержкой JWT токена
# Установка
Для установки Test_project, требуется:
1. клонировать репозиторий командой 
```git clone git@github.com:andrey-praktikum-98/test_project.git```
5. установить виртуальное окружение
`python3 -m venv venv`
Подробная инструкция: [Документация env](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments).
6. Активировать виртуальное окружение
`source venv/Scripts/activate`
7. Установка пакетов из requirements.txt
`python -m pip install -r requirements.txt`
Подробная инструкция: [Документация freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/#examples).
8. Загрузить пакеты в файл requirements.txt
`python -m pip freeze > requirements.txt`
9. Обновить миграции 
`python manage.py makemigrations`
`python manage.py migrate`
9. запустить проект ```python manage.py runserver```
# Примеры запросов и ответов
# Запрос на получение категорий с блюдами (GET)
``` http://127.0.0.1:8000/api/v1/foods/  ```
# Ответ
```
{
    "count": 6,
    "next": "http://127.0.0.1:8000/api/v1/foods/?page=2",
    "previous": null,
    "results": [
        {
            "id": 4,
            "name_ru": "Выпечка",
            "name_en": null,
            "name_ch": null,
            "order_id": 10,
            "foods": [
                {
                    "internal_code": null,
                    "code": 5,
                    "name_ru": "булочка",
                    "description_ru": "булочка с кунжутом",
                    "description_en": null,
                    "description_ch": null,
                    "is_vegan": false,
                    "is_special": false,
                    "cost": "140.00",
                    "additional": []
                },
                {
                    "internal_code": null,
                    "code": 6,
                    "name_ru": "Самса",
                    "description_ru": "Самса с мясом",
                    "description_en": null,
                    "description_ch": null,
                    "is_vegan": false,
                    "is_special": false,
                    "cost": "75.00",
                    "additional": []
                }
            ]
        },
        {
            "id": 4,
            "name_ru": "Выпечка",
            "name_en": null,
            "name_ch": null,
            "order_id": 10,
            "foods": [
                {
                    "internal_code": null,
                    "code": 5,
                    "name_ru": "булочка",
                    "description_ru": "булочка с кунжутом",
                    "description_en": null,
                    "description_ch": null,
                    "is_vegan": false,
                    "is_special": false,
                    "cost": "140.00",
                    "additional": []
                },
                {...}
                ...
            ]
        },
        {...},
        {
            "id": 3,
            "name_ru": "Напитки",
            "name_en": null,
            "name_ch": null,
            "order_id": 10,
            "foods": [
                {
                    "internal_code": null,
                    "code": 11,
                    "name_ru": "Чай",
                    "description_ru": "Чай 100 гр",
                    "description_en": null,
                    "description_ch": null,
                    "is_vegan": false,
                    "is_special": false,
                    "cost": "150.00",
                    "additional": []
                },
                {
                    "internal_code": null,
                    "code": 2,
                    "name_ru": "кола",
                    "description_ru": "Кола",
                    "description_en": null,
                    "description_ch": null,
                    "is_vegan": false,
                    "is_special": false,
                    "cost": "123.00",
                    "additional": []
                },
                {
                    "internal_code": null,
                    "code": 3,
                    "name_ru": "спрайт",
                    "description_ru": "Спрайт",
                    "description_en": null,
                    "description_ch": null,
                    "is_vegan": false,
                    "is_special": false,
                    "cost": "123.00",
                    "additional": []
                },
                {
                    "internal_code": null,
                    "code": 4,
                    "name_ru": "байкал",
                    "description_ru": "Байкал",
                    "description_en": null,
                    "description_ch": null,
                    "is_vegan": false,
                    "is_special": false,
                    "cost": "123.00",
                    "additional": []
                }
            ]
        }
    ]
}
```
# Автор
Автор проекта: andrey-praktikum-98
