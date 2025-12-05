from flask import Flask, render_template

app = Flask(__name__)

# Выносим данные логотипов за пределы маршрутов — чтобы не дублировать
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



@app.route('/')
def index():
    return render_template('index.html', logos=logos_data)

@app.route('/logos')
def logos():
    return render_template('logos.html', logos=logos_data)

@app.route('/price-laptops')
def price_laptops():
    return render_template('price_laptops.html')

@app.route('/price-tv')
def price_tv():
    return render_template('price_tv.html')

@app.route('/internet-services')
def internet_services():
# Вынести  данные интернет-услуг за пределы маршрутов — чтобы не дублировать
    services_data = [
        {'name': 'Прошивка роутера OpenWRT', 'price': '2 500 ₽', 'desc': 'Установка OpenWRT с полной настройкой'},
        {'name': 'Настройка обхода блокировок', 'price': '1 500 ₽', 'desc': 'YouTube, Telegram, WhatsApp, Discord'},
        {'name': 'Настройка VPN на роутере', 'price': '2 000 ₽', 'desc': 'WireGuard/OpenVPN на роутере'},
        {'name': 'Усиление Wi-Fi сигнала', 'price': '3 500 ₽', 'desc': 'Установка репитера/усилителя'},
        {'name': 'Ремонт роутера', 'price': 'от 1 000 ₽', 'desc': 'Диагностика и ремонт'},
        {'name': 'Настройка родительского контроля', 'price': '1 200 ₽', 'desc': 'Ограничение времени и контента'},
    ]
    return render_template('internet_services.html', services=services_data)


if __name__ == '__main__':
    app.run(debug=True, port=5001)