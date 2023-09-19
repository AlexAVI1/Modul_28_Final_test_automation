from settings import Data
from pages.base import Base
import pytest

class TestAuth(Base):
    def test_form_title_text(self, auth_page):
        form_title = auth_page.get_form_title_text()
        assert form_title == "Авторизация"
    # Продуктовый слоган ЛК "Ростелеком ID".
    @pytest.mark.xfail()
    def test_product_title_text(self, auth_page):
        product_title = auth_page.get_product_title()
        assert product_title == "Ростелеком ID"

        # Проверяем название формы ввода номера телефона
    @pytest.mark.xfail()
    def test_phone_input_title_text(self, auth_page):
        input_title = auth_page.get_input_title_text()
        assert input_title == "Номер"

    # Проверяем название формы ввода почты
    @pytest.mark.xfail()
    def test_email_input_title_text(self, auth_page):
        auth_page.click_tab_email()
        input_title = auth_page.get_input_title_text()
        assert input_title == "Почта"

    # Проверяем название формы ввода Логина
    def test_login_input_title_text(self, auth_page):
        auth_page.click_tab_login()
        input_title = auth_page.get_input_title_text()
        assert input_title == "Логин"

    # Перенаправление на нужную страницу при авторизации
    @pytest.mark.skip_if_captcha
    @pytest.mark.xfail()
    def test_authorization_relative_link(self, auth_page):
        auth_page.log_into_application(Data.valid_phone, Data.valid_password)
        relative_link = auth_page.get_relative_link()
        assert "redirect_uri" in relative_link
    # Авторизация пользователя с некорректным номером телефона
    @pytest.mark.skip_if_captcha
    @pytest.mark.parametrize("phone", list(Data.invalid_phone.keys()),
                             ids=list(Data.invalid_phone.values()))
    def test_invalid_phone_authorization(self, phone, auth_page):
        auth_page.log_into_application(phone, Data.valid_password)
        invalid_text = auth_page.get_invalid_data_text()
        assert invalid_text == "Неверный логин или пароль"

    # Авторизация с некорректной почтой
    @pytest.mark.skip_if_captcha
    @pytest.mark.parametrize("email", list(Data.invalid_email.keys()),
                             ids=list(Data.invalid_email.values()))
    def test_invalid_email_authorization(self, email, auth_page):

        auth_page.click_tab_email()
        auth_page.log_into_application(email, Data.valid_password)
        invalid_text = auth_page.get_invalid_data_text()
        assert invalid_text == "Неверный логин или пароль"

    # Авторизация с некорректным логином
    @pytest.mark.skip_if_captcha
    @pytest.mark.parametrize("login", list(Data.invalid_login.keys()),
                             ids=list(Data.invalid_login.values()))
    def test_invalid_login_authorization(self, login, auth_page):
        auth_page.click_tab_login()
        auth_page.log_into_application(login, Data.valid_password)
        invalid_text = auth_page.get_invalid_data_text()
        assert invalid_text == "Неверный логин или пароль"

    # Авторизация с некорректным лицевым счетом
    @pytest.mark.skip_if_captcha
    @pytest.mark.parametrize("ls", list(Data.invalid_ps.keys()),
                             ids=list(Data.invalid_ps.values()))
    def test_invalid_ls_authorization(self, ls, auth_page):
        auth_page.click_tab_ls()
        auth_page.log_into_application(ls, Data.valid_password)
        invalid_text = auth_page.get_invalid_data_text()
        assert invalid_text == "Неверный логин или пароль"

    #  Авторизация с некорректным паролем
    @pytest.mark.skip_if_captcha
    @pytest.mark.parametrize("password", list(Data.invalid_password.keys()),
                             ids=list(Data.invalid_password.values()))
    def test_invalid_password_authorization(self, password, auth_page):
        auth_page.log_into_application(Data.invalid_phone, password)
        invalid_text = auth_page.get_invalid_data_text()
        assert invalid_text == "Неверный логин или пароль"

    # Авторизация с неуказанной почтой
    def test_authorization_without_email(self, auth_page):
        auth_page.click_tab_email()
        auth_page.set_password(Data.valid_password)
        auth_page.click_login_button()
        error_text = auth_page.get_error_message_text()
        assert error_text == "Введите адрес, указанный при регистрации"

    # Авторизация без указания телефона
    def test_authorization_without_phone(self, auth_page):
        auth_page.set_password(Data.valid_password)
        auth_page.click_login_button()
        error_text = auth_page.get_error_message_text()
        assert error_text == "Введите номер телефона"

    # Авторизация без указания логина
    def test_authorization_without_login(self, auth_page):
        auth_page.click_tab_login()
        auth_page.set_password(Data.valid_password)
        auth_page.click_login_button()
        error_text = auth_page.get_error_message_text()
        assert error_text == "Введите логин, указанный при регистрации"

    # Авторизация без лицевого счета
    def test_authorization_without_ls(self, auth_page):
        auth_page.click_tab_ls()
        auth_page.set_password(Data.valid_password)
        auth_page.click_login_button()
        error_text = auth_page.get_error_message_text()
        assert error_text == "Введите номер вашего лицевого счета"


    # Проверка табов выбора аутентификации
    @pytest.mark.xfail()
    def test_authorization_tabs_text(self, auth_page):
        tabs_list = auth_page.get_tabs_list()
        assert tabs_list == ['Номер', 'Почта', 'Логин', 'Лицевой счёт']

    # Переходы на страницы авторизации с помощью других платформ
    def test_vk_authorization_link(self, auth_page):
        vk_link = auth_page.get_vk_link()
        assert "https://id.vk.com/auth" in vk_link

    def test_ok_authorization_link(self, auth_page):
        ok_link = auth_page.get_ok_link()
        assert "https://connect.ok.ru/dk" in ok_link

    def test_mail_ru_authorization_link(self, auth_page):
        mail_ru_link = auth_page.get_mail_ru_link()
        assert "https://connect.mail.ru/oauth/authorize" in mail_ru_link

    @pytest.mark.xfail(reason="Перенаправление на страницу авторизации происходит после повторного нажатия")
    def test_ya_authorization_link(self, auth_page):
        ya_link = auth_page.get_ya_link()
        assert "https://passport.yandex.ru/auth/" in ya_link

    def test_registration_link(self, auth_page):
        auth_page.click_registration_link()
        form_title = auth_page.get_form_title_text()
        assert form_title == "Регистрация"

    # При нажатии на ссылку 'Забыл пароль' открывается форма восстановление пароля
    def test_forgot_password_link(self, auth_page):
        auth_page.click_forgot_password_link()
        form_title = auth_page.get_form_title_text()
        assert form_title == "Восстановление пароля"

    # При нажатии на ссылку 'пользовательского соглашения' открывается страница пользовательского соглашения
    def test_agreement_link(self, auth_page):

        agreement_title = auth_page.get_agreement_title()
        assert "Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»" \
               == agreement_title
