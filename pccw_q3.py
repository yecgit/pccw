from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver_path = r'C:\geckodriver.exe'  # Replace with the path of geckdriver.exe
firefox_binary_path = r'C:\Program Files\Mozilla Firefox\firefox.exe' # Replace with the path of firefox.exe

service = Service(driver_path)
options = Options()
options.binary_location = firefox_binary_path
driver = webdriver.Firefox(service=service, options=options)

try:
    driver.get("https://practicetestautomation.com/practice-test-login/")

    username_field = driver.find_element(By.ID, value="username")
    username_field.send_keys("student")
    password_field = driver.find_element(By.ID, value="password")
    password_field.send_keys("Password123")

    submit_button = driver.find_element(by=By.ID, value="submit")
    submit_button.click()

    wait = WebDriverWait(driver,timeout=10,poll_frequency=1)
    post_header = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                                    "div.post-header h1.post-title").text == "Logged In Successfully")

    # Check the text of the element
    if post_header:
        print("Success message found: Logged In Successfully")

finally:
    # Close the browser
    driver.quit()