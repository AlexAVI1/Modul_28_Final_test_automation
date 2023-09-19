
### Проект состоит из:
* pages\base_page - содержит общие методы
* pages\auth_page - содержит методы для авторизации
* pages\base - содержит тестовый класс
* pages\data - содержит данные для тестирования авторизации
* pages\locators - содержит локаторы
* tests\test_page - содержит все автотесты
* pages\tests requirements.txt содержит библиотеки и зависимости проекта.

### Тест-кейсы доступны по ссылке
https://docs.google.com/spreadsheets/d/1lGlOk40i2bpN2ELCunceJ-3ZE9XTwyUJp399A_Mq2cw/edit?usp=sharing

### При разработке тест-кейсов были применены следующие техники тест-дизайна: 
* предугадывание ошибок;
* анализ граничных значений.


### Инструменты, которые использовались.
* Pytest.
* Selenium
* Для определения локаторов использовался DevTools.

### Запуск тестов:
*  для запуска тестов в браузере Chrome необходимо скачать файл chromedriver.exe
* установить все библиотеки и зависимости: `pip install -r requirements.txt`.
* запустить тесты: `pytest tests/test_page.py`.


