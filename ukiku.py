from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as t




chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('disable-notifications')
chrome_options.add_argument("window-size=1280,720")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://pl.wikipedia.org/wiki/Ghost_Rider_(komiks)")


# try:
#     cookie_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH,'//button/div[text()="Zaakceptuj wszystko"]')))
#     print(cookie_button.location_once_scrolled_into_view)
#     t.sleep(1)
#     cookie_button.click()
#     print('rejected accepted')
# except Exception as e:
#     print('no cookie button')
# t.sleep(1)



print(driver.title)

tytul = driver.find_element(By.CLASS_NAME, "mw-page-title-main")
# tytul.clear()
# tytul.send_keys("cycki")
# tytul.send_keys(Keys.RETURN)



print(tytul.text)


assert tytul.text == "Ghost Rider (komiks)"
