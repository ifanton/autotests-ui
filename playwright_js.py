from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until='networkidle'  # Ждем полной загрузки страницы
    )

    # Выполняем JS-код для замены текста заголовка
    page.evaluate(
        """
        const title = document.getElementById('authentication-ui-course-title-text');
        title.textContent = 'New Text';
        """
    )

    page.wait_for_timeout(2000)

    # Передача аргументов через анонимную функцию
    page.evaluate(
        """
        (text) => { // Принимаем аргумент в JS функции
        const title = document.getElementById('authentication-ui-course-title-text');
        title.textContent = text;
        }
        """,
        'Some Text'  # Передаём аргумент из Python
    )

    page.wait_for_timeout(2000)

    # Форматирование строки в Python
    next_text = 'Another Text'

    page.evaluate(f"""
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = '{next_text}';
    """)

    page.wait_for_timeout(2000)
