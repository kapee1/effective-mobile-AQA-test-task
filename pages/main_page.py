from pages.base_page import BasePage
import allure
from locators import Locators

class MainPage(BasePage):

    @allure.step('Клик по кнопке "О нас"')
    def about_button_header_click(self):
        self.click(Locators.about_button)

    @allure.step('Клик по кнопке "Услуги"')
    def services_button_header_click(self):
        self.click(Locators.services_button)

    @allure.step('Клик по кнопке "Проекты"')
    def projects_button_header_click(self):
        self.click(Locators.projects_button)

    @allure.step('Клик по кнопке "Отзывы"')
    def reviews_button_header_click(self):
        self.click(Locators.reviews_button)

    @allure.step('Клик по кнопке "Контакты"')
    def contacts_button_header_click(self):
        self.click(Locators.contacts_button)


