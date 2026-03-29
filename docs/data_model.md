В проекте используется событийная модель данных (event-based model).

Каждое действие пользователя записывается как событие.

Таблица users

user_id — уникальный идентификатор пользователя
registration_date — дата регистрации
country — страна пользователя
device_type — тип устройства (iOS / Android)

Таблица products

product_id — идентификатор товара
category — категория товара
price — цена
brand — бренд

Таблица events

event_id — идентификатор события
user_id — пользователь
event_type — тип события
product_id — товар
event_time — время события
session_id — идентификатор сессии