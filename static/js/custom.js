// custom.js - основной файл JavaScript
document.addEventListener('DOMContentLoaded', function() {
    console.log('Сайт загружен!');

    // Функция переключения темы
    const setTheme = function (theme) {
        if (theme === 'auto') {
            const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            document.documentElement.setAttribute('data-bs-theme', isDark ? 'dark' : 'light');
        } else {
            document.documentElement.setAttribute('data-bs-theme', theme);
        }
        localStorage.setItem('theme', theme);
    };

    // Показываем активную тему в dropdown
    const showActiveTheme = (theme) => {
        const activeBtn = document.querySelector(`[data-bs-theme-value="${theme}"]`);
        if (!activeBtn) return;
        document.querySelectorAll('[data-bs-theme-value]').forEach(btn => {
            btn.classList.remove('active');
        });
        activeBtn.classList.add('active');
    };

    // Инициализация из localStorage
    const currentTheme = localStorage.getItem('theme') || 'auto';
    showActiveTheme(currentTheme);

    // Клик по кнопкам темы
    document.querySelectorAll('[data-bs-theme-value]').forEach(btn => {
        btn.addEventListener('click', () => {
            const theme = btn.getAttribute('data-bs-theme-value');
            setTheme(theme);
            showActiveTheme(theme);
        });
    });

    // Следим за изменением системной темы (для auto режима)
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (localStorage.getItem('theme') === 'auto') {
            document.documentElement.setAttribute('data-bs-theme', e.matches ? 'dark' : 'light');
        }
    });

    // Активация tooltips
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));

    // Анимация социальных иконок
    const socialIcons = document.querySelectorAll('.social-icon, .social-link');
    socialIcons.forEach(icon => {
        icon.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px) scale(1.1)';
        });
        icon.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    // Анимация карточек на странице "О нас"
    const statsCards = document.querySelectorAll('.stats-card, .contact-card');
    statsCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
        });
    });

    // Плавная прокрутка для якорных ссылок
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;

            e.preventDefault();
            const targetElement = document.querySelector(href);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Анимация логотипов
    const logosTrack = document.querySelector('.logos-track');
    if (logosTrack) {
        console.log('Анимация логотипов активна');

        // Пауза анимации при наведении
        logosTrack.addEventListener('mouseenter', () => {
            logosTrack.style.animationPlayState = 'paused';
        });

        logosTrack.addEventListener('mouseleave', () => {
            logosTrack.style.animationPlayState = 'running';
        });
    }

    // Telegram кнопки - добавляем счетчик кликов
    const telegramButtons = document.querySelectorAll('a[href*="t.me"]');
    telegramButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            console.log('Переход в Telegram для записи');
            // Можно добавить Google Analytics или другую аналитику
        });
    });

    console.log('Все скрипты активированы');
});

// Функция для копирования текста (если понадобится в будущем)
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        console.log('Текст скопирован: ' + text);
    }).catch(err => {
        console.error('Ошибка копирования: ', err);
    });
}