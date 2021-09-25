import time, random
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait


try:
    """
    Позитивный автотест регистрации тестового юзера на Яндекс Дзен по номеру телефона.
    Данные для полей "Имя" и "Фамилия" предлагаются на английском языке.
    Пароль считывается из файла.
    """
    waiting = random.randint(2,5) # переменная для установки паузы в диапазоне 2-5 секунд
    browser = Chrome()

    browser.get("https://zen.yandex.ru/")
    print(browser.title)

    time.sleep(waiting)

    def slow_mode(element, text):
        # Имитация ручного ввода текста
        for character in text:
            element.send_keys(character)
            time.sleep(0.4)

    # Поиск нужного элемента по CSS-селектору
    sign_up_button = browser.find_element_by_css_selector\
        ("div.zen-ui-header2__right-items a:nth-child(3)")
    sign_up_button.click()

    time.sleep(waiting)

    original_window = browser.current_window_handle

    # Заполнение имени пользователя
    user_name = browser.find_element_by_css_selector\
        ('input[name="firstname"]')
    slow_mode(user_name,"Diana")

    time.sleep(waiting)

    # Заполнение фамилии пользователя
    user_lastname = browser.find_element_by_css_selector\
        ('input[name="lastname"]')
    slow_mode(user_lastname,"Novikova")

    time.sleep(waiting)

    # Заполнение логина пользователя
    user_login = browser.find_element_by_css_selector\
        ('input[name="login"]')
    slow_mode(user_login,"mytestlogin1239")

    time.sleep(waiting)

    # Чтение пароля из текстового файла и ввод в текстовое поле
    my_password = browser.find_element_by_css_selector\
        ('input[name="password"]')
    with open('ya_dzen_password', 'r') as password:
        Password = password.read().replace('\n', '')
    slow_mode(my_password, Password)

    # Проверка отображения пароля
    toggler = browser.find_element_by_css_selector\
        ('button.field-type__toggler').click()

    time.sleep(waiting)

    # В поле подтверждения пароля вводятся данные из файла ya_dzen_password
    confirm_password = browser.find_element_by_css_selector\
            ('input[name="password_confirm"]')
    slow_mode(confirm_password, Password)

    # Ввод номера телефона
    phone_number = browser.find_element_by_css_selector\
    ('input[name="phone"]')
    slow_mode(phone_number, "9998887766")

    time.sleep(waiting)

     # Кнопка подтверждения номера телефона
    confirm_phone_number = browser.find_element_by_css_selector\
        ('.registration__send-code button').click()

    time.sleep(waiting)

    # Ожидание ввода кода вручную (формат кода: 111-111）
    try:
        phone_code = browser.find_element_by_xpath\
            ('//input[@id="phoneCode"]')
        WebDriverWait(browser,30).until(
            lambda browser:len(phone_code.get_attribute("value")) == 6)
    except Exception as error:
        print(f"Произошла ошибка, ее TraceBack: {error}")

    time.sleep(waiting)

    # Переход на страницу пользовательского соглашения
    try:
        terms_of_use = browser.find_element_by_css_selector\
            ('a[href="https://yandex.ru/legal/rules/"]').click()
        time.sleep(4)
        browser.switch_to.window(original_window)
    except Exception as error:
        print(f"Произошла ошибка, ее TraceBack: {error}")

    time.sleep(waiting)

    # Переход на страницу политики конфиденциальности
    try:
        privacy_policy = browser.find_element_by_css_selector\
            ('a[href="https://yandex.ru/legal/confidential/"]').click()
        time.sleep(4)
        browser.switch_to.window(original_window)
    except Exception as error:
        print(f"Произошла ошибка, ее TraceBack: {error}")

    time.sleep(waiting)

    # Проверка, что чекбокс принятия условий выбран по умолчанию
    rule_checkbox_input = browser.find_element_by_css_selector\
        ('span [id="eula_accepted"]')
    rule_checkbox = rule_checkbox_input.get_attribute('checked')
    print("value of checkbox: ", rule_checkbox)
    assert rule_checkbox is not None, 'Чекбокс не выбран по умолчанию'


    # Подтверждение регистрации
    try:
        submit = browser.find_element_by_css_selector\
            ('.form__submit button').click()
    except Exception as error:
        print(f"Произошла ошибка, ее TraceBack: {error}")

finally:
    time.sleep(10)
    browser.quit()



