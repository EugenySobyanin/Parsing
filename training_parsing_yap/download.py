import re
import requests_cache

from bs4 import BeautifulSoup
from pathlib import Path
from urllib.parse import urljoin


BASE_DIR = Path(__file__).parent

DOWNLOADS_URL = 'https://docs.python.org/3/download.html'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(DOWNLOADS_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')
    main_tag = soup.find('div', {'role': 'main'})
    table_tag = soup.find('table', {'class': 'docutils'})

    # Нашли нужный тег, использовав регулярку
    pdf_a4_tag = table_tag.find('a', {'href': re.compile(r'.+pdf-a4\.zip$')})
    # Достали относительную ссылку
    pdf_a4_link = pdf_a4_tag['href']
    # Получили полную ссылку
    arhive_url = urljoin(DOWNLOADS_URL, pdf_a4_link)
    # Создаем имя для сохраняемого файла
    file_name = arhive_url.split('/')[-1]

    # Формируем путь до директории downloads
    downloads_dir = BASE_DIR / 'downloads'
    # Создаем директорию
    downloads_dir.mkdir(exist_ok=True)
    # Получаем путь до архива, объединив имя файла с директорией
    arhive_path = downloads_dir / file_name

    # Загрузка архива по ссылке
    response = session.get(arhive_url)

    # В бинарном режиме открыватся файл на запись по указанному пути
    with open(arhive_path, 'wb') as file:
        file.write(response.content)
