# Развертывание на локальной машине
1. Создаем виртуальное окружение:
- Копируем в папку QuoteApi файлы Pipfile и Pipfile.lock
из проекта Jinja2_ex
[packages]
flask = "*"
httpie = "*"
[dev-packages]
autopep8 = "*"
- Выполняем команды
pipenv sync
pipenv graph

2. Устанавливаем зависимости в соответствии с requirements.txt
pipenv install Flask-SQLAlchemy
pipenv install Flask-Migrate
cat Pipfile (видим, что два пакета доставлено в наше во)

3. Копируем информацию о местонахождении окружения
и добавляем ее для своего удобства в файл:
pipenvs_for_workspace_settings.txt
pipenv --venv

4. Активируем во
pipenv shell
exit (деактивация)

5. Создаем локальную БД: flask db upgrade
(она будет создана на основе файлов миграций в папке migrations)
появился файл main.db
