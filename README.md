# Задание: запуск автотестов для разных языков интерфейса

Этот репозиторий содержит Python-скрипты и тесты для платформы [Stepik](https://stepik.org/lesson/237240/step/10?unit=209628).

## О проекте

Основная цель этого репозитория - автоматизировать тестирование [сайта](http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/) с помощью Selenium WebDriver и Pytest.

## Возможности

- Автоматизированные тесты для отправки задач
- Обработка различных сценариев ошибок
- Повторно используемая настройка Selenium WebDriver
- Тестовый фреймворк на основе Pytest

## Начало работы

Чтобы начать работу с проектом, выполните следующие шаги:

1. Клонирование репозитория:

   git clone https://github.com/Inactive0073/qa_stepik_work.git

2. Настройка виртуального окружения

Windows:
   - cd qa_stepik_work
   - python -m venv venv
   - venv/bin/activate
     
Linux:
   - cd qa_stepik_work
   - python3 -m venv venv
   - source venv/bin/activate

4. Установка зависимостей:

   pip install -r requirements.txt

5. Запуск тестов:

   pytest --language=<YOUR_LOCAL> # по умолчанию pytest --language=ru test_items.py

## Конфигурация

Требований к конфигурационному файлу нет.

## Вклад

Если вы обнаружите какие-либо проблемы или у вас есть предложения по улучшению, не стесняйтесь создавать новый запрос или отправлять pull request. Вклад всегда приветствуется!
