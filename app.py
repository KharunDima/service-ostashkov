import json
import os
from flask import Flask, render_template, send_file, abort

# Импортируем конфигурацию
from config import Config, DATA_FILES, PDF_SETTINGS, CONTACT_INFO, SOCIAL_LINKS, SITE_INFO

app = Flask(__name__)
app.config.from_object(Config)

def load_json_data(file_path):
    """Загружает данные из JSON файла с обработкой ошибок"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка парсинга JSON в файле {file_path}: {e}")
    except Exception as e:
        raise Exception(f"Неизвестная ошибка при загрузке данных: {e}")

# Загружаем данные при старте
try:
    SERVICES_DATA = load_json_data(DATA_FILES['services'])
    LOGOS_DATA = load_json_data(DATA_FILES['logos'])
except Exception as e:
    print(f"Ошибка загрузки данных: {e}")
    SERVICES_DATA = {}
    LOGOS_DATA = []

# Контекстный процессор для добавления глобальных переменных в шаблоны
@app.context_processor
def inject_global_data():
    """Добавляет глобальные данные во все шаблоны"""
    return {
        'site_info': SITE_INFO,
        'contact_info': CONTACT_INFO,
        'social_links': SOCIAL_LINKS,
        'current_year': 2024
    }

# === МАРШРУТЫ ===

@app.route('/')
def index():
    """Главная страница"""
    return render_template('index.html', logos=LOGOS_DATA)

@app.route('/price-laptops')
def price_laptops():
    """Прайс-лист: ноутбуки"""
    return render_template('price_base.html', page_data=SERVICES_DATA['laptops'])

@app.route('/price-tv')
def price_tv():
    """Прайс-лист: телевизоры"""
    return render_template('price_base.html', page_data=SERVICES_DATA['tv'])

@app.route('/internet-services')
def internet_services():
    """Услуги по настройке интернета и роутеров"""
    return render_template('price_base.html', page_data=SERVICES_DATA['internet_services'])

@app.route('/price-pdf')
def price_pdf():
    """Страница с PDF прайс-листом"""
    pdf_path = PDF_SETTINGS['price_file']
    pdf_size = "Не доступен"

    if pdf_path.exists():
        size_bytes = pdf_path.stat().st_size
        # Конвертируем в читаемый формат
        if size_bytes < 1024:
            pdf_size = f"{size_bytes} Б"
        elif size_bytes < 1024 * 1024:
            pdf_size = f"{size_bytes / 1024:.1f} КБ"
        else:
            pdf_size = f"{size_bytes / (1024 * 1024):.1f} МБ"

    return render_template('price_pdf.html', pdf_size=pdf_size)

@app.route('/download-price')
def download_price():
    """Скачивание PDF прайс-листа"""
    pdf_path = PDF_SETTINGS['price_file']

    if not pdf_path.exists():
        abort(404, description="Прайс-лист не найден")

    return send_file(
        pdf_path,
        as_attachment=True,
        download_name='price-list.pdf',
        mimetype='application/pdf'
    )

@app.route('/view-price')
def view_price():
    """Просмотр PDF прайс-листа в браузере"""
    pdf_path = PDF_SETTINGS['price_file']

    if not pdf_path.exists():
        abort(404, description="Прайс-лист не найден")

    return send_file(
        pdf_path,
        as_attachment=False,
        mimetype='application/pdf'
    )

@app.route('/contacts')
def contacts():
    """Страница контактов"""
    return render_template('contacts.html')

@app.route('/about')
def about():
    """Страница о нас"""
    return render_template('about.html')

# === ОБРАБОТЧИКИ ОШИБОК ===

@app.errorhandler(404)
def page_not_found(e):
    """Обработка ошибки 404 — страница не найдена"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Обработка ошибки 500 — внутренняя ошибка сервера"""
    return render_template('500.html'), 500

# === ТЕСТОВЫЙ МАРШРУТ ДЛЯ ПРОВЕРКИ 500 ОШИБКИ ===
@app.route('/test-500')
def test_500():
    """Тестовый маршрут для проверки страницы 500 ошибки"""
    # Искусственно вызываем ошибку
    raise Exception("Это тестовая ошибка для проверки страницы 500")

# === ЗАПУСК ПРИЛОЖЕНИЯ ===

if __name__ == '__main__':
    # Проверяем наличие PDF файла
    if not PDF_SETTINGS['price_file'].exists():
        print(f"ВНИМАНИЕ: PDF файл не найден: {PDF_SETTINGS['price_file']}")
        print("Создайте папку static/pdf и поместите туда price-list.pdf")

    # Настройки запуска
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.environ.get('PORT', 5001))
    host = os.environ.get('HOST', '0.0.0.0')

    app.run(debug=debug_mode, host=host, port=port)