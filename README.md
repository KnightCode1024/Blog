# 🚀 Blog — современный блог на Django

[Описание](#описание) | [Возможности](#возможности) | [Архитектура](#архитектура) | [Модели](#модели) | [Быстрый-старт](#быстрый-старт) | [Технологии](#технологии) | [Деплой](#деплой) | [Документация](#документация)

---

## 📖 Описание

**Blog** — это мощная платформа для публикации и управления постами, построенная на Django. Проект предназначен для быстрого старта собственного блога, расширяемого и готового к продакшену. Поддерживает регистрацию, авторизацию через соцсети, работу с медиа, категории, теги, поиск, кэширование, масштабируемый деплой через Docker и красивый UI.

---

## ✨ Возможности

- 📝 Публикация, редактирование и удаление постов
- 🔍 Поиск по постам
- 🏷️ Категории и теги
- 👤 Пользовательские профили с фото и датой рождения
- 🔑 Регистрация и вход (в том числе через GitHub и VK)
- 🛡️ Капча для форм
- ⚡ Кэширование и Redis
- 🗺️ Sitemap для SEO
- 🛠️ Админ-панель Django
- 📦 Docker-окружение для быстрого старта
- 🐘 PostgreSQL и Nginx в комплекте
- 📂 Загрузка файлов и изображений к постам

---

## 🏗️ Архитектура

- **blog/** — основной Django-проект
  - **posts/** — управление постами, категориями, тегами
  - **users/** — регистрация, профили, аутентификация
  - **config/** — настройки, роутинг, wsgi/asgi
  - **static/**, **media/**, **templates/** — статика, медиа, шаблоны
- **nginx/** — кастомная конфигурация nginx для проксирования и отдачи статики
- **ssl/** — сертификаты (опционально)
- **compose.yml** — Docker Compose для продакшена и разработки

---

## 🗃️ Модели

### Post
- **title** — заголовок
- **slug** — уникальный URL
- **summury** — краткое описание
- **content** — текст поста
- **author** — автор (пользователь)
- **cat** — категория
- **tags** — теги
- **file** — вложение
- **image** — изображение
- **is_published** — статус публикации
- **time_create/time_update** — даты

### Category
- **name** — название
- **slug** — URL

### TagPost
- **tag** — название
- **slug** — URL

### User (расширен)
- **photo** — фото профиля
- **date_birth** — дата рождения

---

## ⚡ Быстрый старт

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/KnightCode1024/Blog.git
   cd Blog
   ```
2. **Создайте .env файл** (пример переменных см. в compose.yml)
3. **Запустите через Docker Compose:**
   ```bash
   docker compose up --build
   ```
   - Приложение: [http://localhost](http://localhost)
   - Админка: [http://localhost/admin/](http://localhost/admin/)
4. **Создайте суперпользователя:**
   ```bash
   docker compose exec blog python manage.py createsuperuser
   ```

---

## 🛠️ Технологии

- Python 3.12
- Django 5.1.7
- PostgreSQL
- Redis
- Nginx
- Gunicorn
- Docker
- Pillow, social-auth-app-django, django-simple-captcha, и др.

---

## 🚀 Деплой

### Быстрый деплой на сервер с HTTPS

1. **Настройте DNS:**
   - Укажите A-записи вашего домена (например, `kirillblog.ru` и `www.kirillblog.ru`) на IP вашего сервера.

2. **Склонируйте проект на сервер:**
   ```bash
   git clone https://github.com/KnightCode1024/Blog.git
   cd Blog
   ```

3. **Создайте необходимые папки для certbot:**
   ```bash
   mkdir -p certbot/conf certbot/www
   ```

4. **Создайте и настройте .env файл** (см. пример переменных в `.env.template.yml`).

5. **Откройте порты 80 и 443** на сервере (firewall, cloud-панель и т.д.).

6. **Первый запуск (получение сертификата):**
   - Сертификаты будут автоматически сохранены в `certbot/conf/live/ВАШ_ДОМЕН/`.
   - Запустите сервисы:
     ```bash
     docker compose up --build -d
     ```
   - Certbot автоматически запросит и сохранит SSL-сертификаты для вашего домена.

7. **Проверьте доступность сайта:**
   - Откройте https://ваш_домен (например, https://kirillblog.ru)
   - Админка: https://ваш_домен/admin/

8. **Создайте суперпользователя:**
   ```bash
   docker compose exec blog python manage.py createsuperuser
   ```

9. **Обновление сертификата:**
   - Certbot автоматически продлевает сертификаты при перезапуске контейнера certbot.
   - Для ручного обновления:
     ```bash
     docker compose run --rm certbot renew
     docker compose restart nginx
     ```

10. **Обновление зависимостей:**
   ```bash
   docker compose exec blog pip install -r requirements/prod.txt
   ```

11. **Миграции:**
    ```bash
    docker compose exec blog python manage.py migrate
    ```

#### Как это работает
- **nginx** проксирует запросы к Django и обслуживает статику/медиа.
- **certbot** автоматически получает и обновляет SSL-сертификаты (хранятся в `certbot/conf/live/ВАШ_ДОМЕН/`).
- **blog** — основной сервис Django.
- Все конфиги для nginx лежат в папке `nginx/`.

> ⚡ Если меняете домен — обновите его в `nginx/blog.conf` и пересоздайте сертификаты через certbot.

---

## 📚 Документация

- [Django docs](https://docs.djangoproject.com/ru/5.1/)
- [Docker Compose](https://docs.docker.com/compose/)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [Redis](https://redis.io/docs/)
- [Nginx](https://nginx.org/ru/docs/)

---

> Проект создан для быстрого старта современного блога, легко расширяется и кастомизируется под любые задачи. Если есть вопросы — создавайте issue или pull request!
