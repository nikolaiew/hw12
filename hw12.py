import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.implicitly_wait(2)  # неявне очікування
driver.get("https://casenik.com.ua/user/login")

email_field = driver.find_element(By.XPATH, '//input[@id="email"]')
email_field.send_keys("liam_brown9793@gmail.com")
password_field = driver.find_element(By.XPATH, '//input[@id="pasword"]')
password_field.send_keys("Password2023")
login_button = driver.find_element(By.XPATH, '//button[@class="btn button-gen"]').click()

message2 = WebDriverWait(driver, 29).until_not(
    #EC.element_to_be_clickable((By.XPATH, "//div[@class = 'alert alert-success']"))
    EC.visibility_of_element_located((By.XPATH, "//div[@class = 'alert alert-success']"))
)  # реалізовано явне очікування, а саме: очікуй зникнення елементу, але не більше 29 сек. (якщо збільшити до 32 сек. і більше - код запрацює)

time.sleep(5)

driver.quit()
