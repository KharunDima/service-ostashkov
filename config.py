import os
from pathlib import Path

# Базовые пути
BASE_DIR = Path(__file__).parent.absolute()
TEMPLATES_DIR = BASE_DIR / 'templates'
STATIC_DIR = BASE_DIR / 'static'
DATA_DIR = BASE_DIR / 'data'

# Конфигурация Flask
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

    # Настройки для production
    PREFERRED_URL_SCHEME = 'https'

    # Максимальный размер файлов (для будущих загрузок)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

# Контактная информация
CONTACT_INFO = {
    'phone': '+7 (915) 702-31-72',
    'email': 'kharun.dima@mail.ru',
    'telegram': '@kharun_dima',
    'whatsapp': '+79157023172',
    'address': 'г. Осташков, Тверская область',
    'work_hours': 'Пн-Вс: 9:00–21:00 (без выходных)'
}

# Социальные сети
SOCIAL_LINKS = {
    'telegram': 'https://t.me/kharun_dima',
    'whatsapp': 'https://wa.me/79157023172',
    'youtube': '#',
    'github': '#'
}

# Файлы данных
DATA_FILES = {
    'services': DATA_DIR / 'services.json',
    'logos': DATA_DIR / 'logos.json'
}

# Настройки PDF прайса
PDF_SETTINGS = {
    'price_file': STATIC_DIR / 'pdf' / 'price-list.pdf',
    'price_url': '/static/pdf/price-list.pdf',
    'price_title': 'Полный прайс-лист (PDF)'
}

# Настройки темы
THEME_SETTINGS = {
    'default': 'auto',
    'allow_auto': True
}

# Мета информация
SITE_INFO = {
    'name': 'Ремонт техники',
    'description': 'Профессиональный ремонт ноутбуков, телевизоров и настройка сетевого оборудования',
    'author': 'Сервисный центр в Осташкове',
    'keywords': 'ремонт, ноутбуки, телевизоры, Осташков, сервис'
}

# Настройки карусели
CAROUSEL_SETTINGS = {
    'interval': 5000,  # ms
    'pause_on_hover': True
}