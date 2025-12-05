// custom.js - основной файл
document.addEventListener('DOMContentLoaded', function() {
    console.log('Сайт загружен!');

    // Функция переключения темы (остается для взаимодействия пользователя)
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
    const socialIcons = document.querySelectorAll('.social-icon');
    socialIcons.forEach(icon => {
        icon.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px) scale(1.1)';
        });
        icon.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    // Проверка логотипов
    const logosTrack = document.querySelector('.logos-track');
    if (logosTrack) {
        console.log('Анимация логотипов активна');
    }

    console.log('Все скрипты активированы');
});