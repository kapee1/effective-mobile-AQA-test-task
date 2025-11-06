FROM selenium/standalone-chrome:latest

USER root
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONPATH=/app
CMD ["pytest", "-q", "--alluredir=allure-results"]
