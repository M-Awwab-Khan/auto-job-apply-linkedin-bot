from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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

driver.find_element(By.ID, 'username').send_keys(MY_EMAIL, Keys.TAB, MY_PASSWORD)
driver.find_element(By.CLASS_NAME, 'btn__primary--large').click()

jobs = driver.find_elements(By.CLASS_NAME, 'jobs-search-results__list-item')

for job in jobs:
    job.click()
    try:
        wait = WebDriverWait(driver, 5)  # 10 seconds timeout
        job_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "jobs-apply-button")))
    except TimeoutException as e:
        continue

    wait = WebDriverWait(driver, 5)  # 10 seconds timeout
    job_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "jobs-apply-button")))
    job_button.click()
    wait = WebDriverWait(driver, 5)  # 10 seconds timeout
    input_field = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "jobs-apply-button")))
    input_field.clear()
    input_field.send_keys('02382347982')

    driver.find_element(By.CSS_SELECTOR, 'button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view').click()

    if int(driver.find_element(By.CLASS_NAME, 'artdeco-completeness-meter-linear__progress-element').get_attribute('value')) < 50:
        driver.find_element(By.CLASS_NAME, 'artdeco-button__icon').click()
        driver.find_element(By.CSS_SELECTOR, 'button.artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view.artdeco-modal__confirm-dialog-btn').click()
    else:
        driver.find_element(By.CSS_SELECTOR, 'button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view').click()
        driver.find_element(By.CSS_SELECTOR, 'button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view').click()
        wait = WebDriverWait(driver, 10)  # 10 seconds timeout
        element_to_wait_for = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "artdeco-button__icon ")))
        element_to_wait_for.click()
