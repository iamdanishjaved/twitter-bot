from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from automation.config import config

# Use one of the following, according to your setup
driver = webdriver.Firefox(executable_path=config['driver_path'])
# driver = webdriver.Chrome(executable_path=config['driver_path'])

driver.get(config['login_url'])
# add this wait so that your browser load HTML and then you start locating your tags/selectors
wait = WebDriverWait(driver, 10)


def login():
    try:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['user_css_sel']))).send_keys(config['username'])
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['pass_css_sel']))).send_keys(config['password'])
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['login_css_sel']))).click()
    except Exception as e:
        print('Error: %s' % e)
    finally:
        # Here, do whatever you want to...
        logout()


def logout():
    sleep(10)
    driver.get(config['logout_url'])
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['login_css_sel']))).click()
    sleep(10)
    driver.quit()


if __name__ == '__main__':
    login()
