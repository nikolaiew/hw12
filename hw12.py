import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.implicitly_wait(2)  # задаємо неявне очікування
driver.get("https://www.ctrs.com.ua/")

slp = 2  # змінна тривалості примусової затримки для зручності спостереження за тестом

# Очікуємо кнопку зворотнього зв'язку (але не більше 10 сек), яка з'являється з затримкою
feedback_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="dib"]/button'))).click()
time.sleep(slp)

# Обираємо варіант "Написати до служби підтримки" - відкривається нове вікно
write_to_support = driver.find_element(By.XPATH, '//a[@href="https://my.ctrs.com.ua/uk/support/tickets"]').click()
time.sleep(slp)

# переходимо у відповідне нове вікно та обираємо контрольний напис
write_to_support_page = driver.window_handles[1]
driver.switch_to.window(write_to_support_page)
signin_signup_message = driver.find_element(By.XPATH, '//h2')
print(signin_signup_message.text)  # контрольний вивід

# перевірка відповідності отриманого напису з очікуємим
assert signin_signup_message.text == 'Вхід / реєстрація', 'FAILED! Something wrong!'
time.sleep(slp)
driver.quit()
