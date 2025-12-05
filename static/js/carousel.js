// Optional: можно добавить кастомный JavaScript для карусели
document.addEventListener('DOMContentLoaded', function() {
    // Инициализация карусели
    const myCarousel = document.querySelector('#myCarousel')
    const carousel = new bootstrap.Carousel(myCarousel, {
        interval: 5000,
        wrap: true
    })
})