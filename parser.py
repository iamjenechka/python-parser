import requests
from bs4 import BeautifulSoup

# URL сайта для парсинга
url = "https://example.com"

# Отправляем GET-запрос на сайт
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Создаем объект BeautifulSoup для парсинга HTML-кода
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Ищем все заголовки (например, h2 с классом 'title')
    articles = soup.find_all("h2", class_="title")
    
    print("Заголовки статей:")
    for article in articles:
        # Извлекаем текст заголовка
        print(article.get_text(strip=True))
else:
    print(f"Ошибка при запросе: {response.status_code}")
