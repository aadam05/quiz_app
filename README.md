# Сохранение вопросов с викторины из внешнего API

## Как развернуть проект
- скачать репозиторий, перейти в директорию с ```docker-compose.yml```

- заполнить переменные среды в файле ```.env```

- собрать и запустить докер-сборку

```docker-compose up -d --build```

```docker-compose up```

- Перейти на swagger http://localhost:8000/docs

- Ввести число вопросов которые вы хотите сохранить http://localhost:8000/docs#/questions/create_questions_questions__post

- Получить все вопросы http://localhost:8000/docs#/questions/get_questions_questions__get

- При остановке или удалении контейнера, данные не удаляются