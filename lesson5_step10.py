from selenium import webdriver
import time

def registrationCheck_1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)

    # Kод, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('//input[@placeholder="Введите имя"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@placeholder="Введите фамилию"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[@placeholder="Введите Email"]')
    input3.send_keys("Smolensk@mail")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

def registrationCheck_2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
    browser.get(link)

    # Kод, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('//input[@placeholder="Введите имя"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@placeholder="Введите фамилию"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[@placeholder="Введите Email"]')
    input3.send_keys("Smolensk@mail")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

registrationCheck_1()
registrationCheck_2()



