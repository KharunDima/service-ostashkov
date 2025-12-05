// theme-loader.js - Загружается синхронно в head
(function() {
    'use strict';

    // 1. Проверяем localStorage
    const savedTheme = localStorage.getItem('theme');

    // 2. Если есть сохраненная тема, применяем ее сразу
    if (savedTheme === 'dark' || savedTheme === 'light') {
        document.documentElement.setAttribute('data-bs-theme', savedTheme);
        return;
    }

    // 3. Если тема 'auto' или не установлена, используем системную
    if (savedTheme === 'auto' || !savedTheme) {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        document.documentElement.setAttribute('data-bs-theme', prefersDark ? 'dark' : 'light');
    }
})();