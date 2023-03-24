from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
options.add_argument('log-level=2')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://bibliotheques.paris.fr/")
"""WebDriverWait(driver,20)
log_button = driver.find_element(By.ID, 'dropMenu1')


print(log_button.is_displayed(), 'displayed')
print(log_button.is_enabled(), 'enabled')
print(log_button.is_selected(), 'selected')"""
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'dropMenu1')))