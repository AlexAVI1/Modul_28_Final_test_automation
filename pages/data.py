# Данные для проверок авторизации.
class TestData:
    incorrect_email = {
        'sashka@yandex.ru': 'unregistered email',
        'sashkayandex.r': 'invalid email',
        'sas@com.ru': 'invalid email',
        'aqw@a.ru': 'invalid email',
        "A" * 1: '1 symbol',
        "A" * 10: '10 symbols',
        "A" * 256: '256 symbols',
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': 'russian',
        '的一是不了人我在有他这为之大来以个中上们': 'chinese',
        '|!@#$%^&*()-_=+`~?"№;:[]{}': 'specials',
        '12345678': 'digit'
    }

    incorrect_phone = {
        '9134225280': 'unregistered phone',
        '0000000000': 'invalid phone',
        "1" * 10: '10 symbols',
        "1" * 256: '256 symbols',
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': 'russian',
        '|!@#$%^&*()-_=+`~?"№;:[]{}': 'specials'
    }

    incorrect_login = {
        'sashka': 'unregistered login',
        'asd11eqw.': 'invalid login',
        'user_name!': 'invalid login',
        "A" * 1: '1 symbol',
        "A" * 5: '5 symbols',
        "A" * 256: '256 symbols',
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': 'russian',
        '|!@#$%^&*()-_=+`~?"№': 'specials symbols',
        '12345678': 'digit'
    }

    incorrect_ls = {
        '142536963258': 'unregistered ls',
        '777777777777': 'invalid ls',
        "1" * 12: '12 symbol',
        "1" * 256: '256 symbols'
    }

    incorrect_password = {
        'Zxcvb123454': 'unregistered password',
        "A" * 1: '1 symbol',
        "A" * 256: '256 symbols',
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': 'russian',
        '|!@#$%^&*()-_=+`~?"№': 'specials symbols',
        '12345678': 'digit'
    }

    VALID_EMAIL = "rambler91@rambler.ru"
    VALID_PHONE = "+71234568515"
    VALID_PASSWORD = "Rambler91"
