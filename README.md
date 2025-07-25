# **DjangoProject**
Это веб-приложение на Django для просмотра случайных цитат, добавления новых цитат и просмотра топ-10 самых популярных цитат на основе лайков и дизлайков. Приложение имеет адаптивный интерфейс с пастельно-фиолетовой темой и обеспечивает интерактивный функционал, такой как лайки/дизлайки и ограничения на добавление цитат.


# **Основные возможности**
* Просмотр цитаты: отображает случайную цитату с учетом веса (weight), увеличивает счетчик просмотров при каждом показе.
* Добавление цитаты: позволяет добавлять новые цитаты с проверками:
  * уникальность текста,
  * максимум три цитаты от одного источника,
  * вес цитаты от 0 до 10.
* Топ-10 цитат: показывает 10 самых популярных цитат, отсортированных по популярности (likes-dislikes).

# **Установка**
1. Клонируйте проект и установите зависимости
```
# git clone, etc
pip install -r requirements.txt
```
2.  Примените миграции
```
python manage.py migrate
```
# **Запуск**
1. Запустите сервер
```
python manage.py runserver
```
2. Открой браузер и перейди по адресу: http://127.0.0.1:8000/

