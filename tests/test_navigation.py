import urls
import allure
from conftest import driver
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Клик по кнопке "О Нас"')
    @allure.description('На странице ищем кнопку "О нас" и проверяем, что клик по кнопке переводит на нужную секуцию страницы')
    def test_opens_about_section(self, driver):
        main = MainPage(driver)
        main.about_button_header_click()

        assert main.get_current_url()==urls.ABOUT_URL

    @allure.title('Клик по кнопке "Услуги"')
    @allure.description('На странице ищем кнопку "Услуги" и проверяем, что клик по кнопке переводит на нужную секуцию страницы')
    def test_opens_services_section(self, driver):
        main = MainPage(driver)
        main.services_button_header_click()

        assert main.get_current_url() == urls.SERVICES_URL

    @allure.title('Клик по кнопке "Проекты"')
    @allure.description('На странице ищем кнопку "Проекты" и проверяем, что клик по кнопке переводит на нужную секуцию страницы')
    def test_opens_projects_section(self, driver):
        main = MainPage(driver)
        main.projects_button_header_click()

        assert main.get_current_url()==urls.PROJECTS_URL

    @allure.title('Клик по кнопке "Отзывы"')
    @allure.description('На странице ищем кнопку "Отзывы" и проверяем, что клик по кнопке переводит на нужную секуцию страницы')
    def test_opens_reviews_section(self, driver):
        main = MainPage(driver)
        main.reviews_button_header_click()

        assert main.get_current_url()==urls.REVIEWS_URL

    @allure.title('Клик по кнопке "Контакты"')
    @allure.description('На странице ищем кнопку "Контакты" и проверяем, что клик по кнопке переводит на нужную секуцию страницы')
    def test_opens_contacts_section(self, driver):
        main = MainPage(driver)
        main.contacts_button_header_click()

        assert main.get_current_url()==urls.CONTACTS_URL