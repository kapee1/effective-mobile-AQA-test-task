# Автоматизация тестирования сайта effective-mobile.ru  
Проект: UI-тесты на Python + Selenium + Pytest + Allure + Docker  

---

## Описание проекта

Автоматизация тестирования главной страницы [effective-mobile.ru](https://effective-mobile.ru)  
с проверкой корректности переходов по разделам “О нас”, “Контакты” и другим.  
Тесты реализованы по паттерну Page Object с использованием Selenium WebDriver  
и системой отчётности Allure.  
Поддерживается запуск как локально, так и в Docker-контейнере.

---

## Структура проекта

```
efmobile-ui-tests/
│
├── allure/                # отчёты о тестировании (Allure)
├── pages/                 # реализация паттерна Page Object
│   ├── base_page.py       # базовый класс для всех страниц
│   └── main_page.py       # элементы и методы главной страницы
│
├── tests/                 # тестовые сценарии
│   └── test_navigation.py 
│
├── conftest.py            # фикстуры Pytest (инициализация WebDriver)
├── locators.py            # локаторы элементов интерфейса
├── urls.py                # все URL и основные константы
├── requirements.txt       # зависимости проекта
├── Dockerfile             # описание Docker-образа
├── README.md              # документация проекта
└── .gitignore
```

---

## 1. Локальный запуск

### Клонирование репозитория
```bash
git clone <repo_url>
cd efmobile-ui-tests
```

### Создание виртуального окружения
```bash
python -m venv .venv
```

### Активация окружения
```bash
.venv\Scripts\activate       # Windows
# или
source .venv/bin/activate    # Linux/macOS
```

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Запуск тестов
```bash
pytest -v --alluredir=allure-results
```

---

## 2. Просмотр отчёта Allure

### Генерация и открытие отчёта
```bash
allure serve allure-results
```

---

## 3. Запуск в Docker

### Сборка образа
```bash
docker build -t autotests .
```

### Запуск тестов
```bash
docker run --rm autotests
```

