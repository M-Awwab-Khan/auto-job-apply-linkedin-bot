from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

MY_EMAIL = 'fakeofawwab@gmail.com'
MY_PASSWORD = 'A?@pHN)PD.3uuzT'

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3810377786&f_AL=true&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true')

signin = driver.find_element(By.LINK_TEXT, 'Sign in')
signin.click()

# Wait for the page to load completely, specifically wait for the presence of an element (adjust as needed)
wait = WebDriverWait(driver, 10)  # 10 seconds timeout
element_to_wait_for = wait.until(EC.presence_of_element_located((By.ID, "username")))

