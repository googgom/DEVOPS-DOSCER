# Проект: python + SQL в Docker

## Описание

Данный проект представляет собой веб-приложение на python с использованием базы данных PostgreSQL. Приложение запускается в Docker-контейнерах и поддерживает автоматические миграции базы данных.

## Основной функционал

- Запуск сервера на python.
- Работа с PostgreSQL.
- Интерфейс для получения и добавления пользователей.
- Конфигурация приложения через переменные окружения.
- Выполнение автоматических миграций базы данных при запуске.

## Условия запуска

- Docker и Docker Compose должны быть установлены.

## Установка и запуск

1. Склонируйте репозиторий, зайдите внутрь и запустите Docker:

```bash
git clone https://github.com/googgom/DEVOPS-DOSCER.git
cd DEVOPS-DOSCER
docker-compose up --build
```
## Использование приложения

После запуска докера(и сообщения в консоле об окончании миграции) можно получить доступ к приложению через браузер.

Список пользователей доступен по адресу: [http://localhost:3456](http://localhost:3456)

Для создания нового пользователя в базе данных создан html интерфейс: [http://localhost:3456/submit](http://localhost:3456/submit)

## Структура проекта

- **src/migration.py**: Скрипт автоматических миграций базы данных.
- **src/server.py**: Файл запуска сервера.
- **src/db.py**: Файл подключения к базе данных.
- **src/router.py**: Файл обработки взаимодействия сервера.
- **docker-compose.yml**: Настройки Docker Compose для запуска приложения и базы данных.
- **Dockerfile**: Описание сборки Docker-образа для приложения.
## Конфигурация

Приложение использует переменные окружения, задаваемые в `docker-compose.yml`:

- **PORT**: Порт для запуска приложения (по умолчанию 3456).
- **DATABASE_URL**: URL для подключения к базе данных PostgreSQL.
- **POSTGRES_DB**, **POSTGRES_USER**, **POSTGRES_PASSWORD**: Настройки базы данных.

## Выполнение условий лабораторной работы

1. **Образ должен быть легковесным**

   Используется базовый образ `python:3.11-alpine`, минимизирующий размер.

2. **Использовать базовые легковесные образы - alpine**

   Все сервисы (python, PostgreSQL) используют версии образов на базе `alpine`.

3. **Вся конфигурация приложения должна быть через переменные окружения**

   Переменные окружения передаются в `docker-compose.yml`.

4. **Статика (зависимости) должна быть внешним томом volume**

   Внешний том используется для хранения зависимостей и данных базы.

5. **Создать файл docker-compose для старта и сборки**

   Файл `docker-compose.yml` присутствует и обеспечивает сборку.

6. **Использование базы данных**

   Приложение работает с PostgreSQL, запускаемым в отдельном контейнере.

7. **Выполнение автоматических миграций**

   Перед запуском сервера выполняется скрипт миграций базы данных.

8. **Контейнер запускается от непривилегированного пользователя**

   В `Dockerfile` создаётся и используется непривилегированный пользователь.

9. **Очистка кеша**

   После установки зависимостей выполняется очистка кеша `pip --no-cache-dir`.
