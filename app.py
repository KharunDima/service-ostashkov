from flask import Flask, render_template

app = Flask(__name__)

# === Данные: Логотипы брендов ===
# Используются на главной и на странице /logos
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

# === Данные: Интернет-услуги ===
# Используются на странице /internet-services
services_data = [
    {'name': 'Прошивка роутера OpenWRT', 'price': '2 500 ₽', 'desc': 'Установка OpenWRT с полной настройкой'},
    {'name': 'Настройка обхода блокировок', 'price': '1 500 ₽', 'desc': 'YouTube, Telegram, WhatsApp, Discord'},
    {'name': 'Настройка VPN на роутере', 'price': '2 000 ₽', 'desc': 'WireGuard/OpenVPN на роутере'},
    {'name': 'Усиление Wi-Fi сигнала', 'price': '3 500 ₽', 'desc': 'Установка репитера/усилителя'},
    {'name': 'Ремонт роутера', 'price': 'от 1 000 ₽', 'desc': 'Диагностика и ремонт'},
    {'name': 'Настройка родительского контроля', 'price': '1 200 ₽', 'desc': 'Ограничение времени и контента'},
]


# === Маршруты ===

@app.route('/')
def index():
    """Главная страница"""
    return render_template('index.html', logos=logos_data)


@app.route('/logos')
def logos():
    """Страница с логотипами брендов"""
    return render_template('logos.html', logos=logos_data)


@app.route('/price-laptops')
def price_laptops():
    """Прайс-лист: ноутбуки"""
    return render_template('price_laptops.html')


@app.route('/price-tv')
def price_tv():
    """Прайс-лист: телевизоры"""
    return render_template('price_tv.html')


@app.route('/internet-services')
def internet_services():
    """Услуги по настройке интернета и роутеров"""
    return render_template('internet_services.html', services=services_data)

# === Обработчик ошибки 404 ===
@app.errorhandler(404)
def page_not_found(e):
    """Обработка ошибки 404 — страница не найдена"""
    return render_template('404.html'), 404

# === Запуск приложения ===
if __name__ == '__main__':
    # Запуск сервера: debug=True, порт 5001
    app.run(debug=True, port=5001)