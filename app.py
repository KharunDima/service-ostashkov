import json
from flask import Flask, render_template
import os

app = Flask(__name__)

# Загружаем данные из JSON
SERVICES_FILE = 'data/services.json'

if not os.path.exists(SERVICES_FILE):
    raise FileNotFoundError(f"Файл {SERVICES_FILE} не найден. Убедитесь, что файл существует перед запуском.")

try:
    with open(SERVICES_FILE, 'r', encoding='utf-8') as f:
        services_data = json.load(f)
except json.JSONDecodeError as e:
    raise ValueError(f"Ошибка парсинга JSON в файле {SERVICES_FILE}: {e}")
except Exception as e:
    raise Exception(f"Неизвестная ошибка при загрузке данных: {e}")

# === Данные: Логотипы брендов ===
logos_data = [
    {'name': 'Acer', 'image': '/static/images/marks/acer.jpg'},
    {'name': 'Apple', 'image': '/static/images/marks/apple.jpg'},
    {'name': 'Asus', 'image': '/static/images/marks/asus.jpg'},
    {'name': 'Dell', 'image': '/static/images/marks/dell.jpg'},
    {'name': 'eMachines', 'image': '/static/images/marks/em.jpg'},
    {'name': 'Fujitsu', 'image': '/static/images/marks/fujitsu.jpg'},
    {'name': 'HP', 'image': '/static/images/marks/hp.jpg'},
    {'name': 'Lenovo', 'image': '/static/images/marks/lenovo.jpg'},
    {'name': 'MSI', 'image': '/static/images/marks/msi.jpg'},
    {'name': 'Packard Bell', 'image': '/static/images/marks/pb.jpg'},
    {'name': 'Samsung', 'image': '/static/images/marks/samsung.jpg'},
    {'name': 'Sony', 'image': '/static/images/marks/sony.jpg'},
    {'name': 'Toshiba', 'image': '/static/images/marks/toshiba.jpg'},
    {'name': 'LG', 'image': '/static/images/marks/lg.jpg'}
]

# === Маршруты ===
@app.route('/')
def index():
    """Главная страница"""
    return render_template('index.html', logos=logos_data)

@app.route('/price-laptops')
def price_laptops():
    """Прайс-лист: ноутбуки"""
    return render_template('price_base.html', page_data=services_data['laptops'])

@app.route('/price-tv')
def price_tv():
    """Прайс-лист: телевизоры"""
    return render_template('price_base.html', page_data=services_data['tv'])

@app.route('/internet-services')
def internet_services():
    """Услуги по настройке интернета и роутеров"""
    return render_template('price_base.html', page_data=services_data['internet_services'])

@app.route('/contacts')
def contacts():
    """Страница контактов"""
    return render_template('contacts.html')

@app.route('/about')
def about():
    """Страница о нас"""
    return render_template('about.html')

# === Обработчики ошибок ===
@app.errorhandler(404)
def page_not_found(e):
    """Обработка ошибки 404 — страница не найдена"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Обработка ошибки 500 — внутренняя ошибка сервера"""
    return render_template('500.html'), 500

# === Запуск приложения ===
if __name__ == '__main__':
    # Перед деплоем отключите debug=True
    debug_mode = False  # Установите в True только для локальной разработки
    port = int(os.environ.get('PORT', 5001))  # Используйте переменную окружения PORT
    app.run(debug=debug_mode, host='0.0.0.0', port=port)