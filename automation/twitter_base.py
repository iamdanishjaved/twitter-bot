from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from automation.config import config

# Use one of the following, according to your setup
driver = webdriver.Firefox(executable_path=config['driver_path'])
# driver = webdriver.Chrome(executable_path=config['chrome_driver_path'])

driver.get(config['login_url'])


class Twitter:
    # add this wait so that your browser load HTML and then you start locating your tags/selectors
    wait = WebDriverWait(driver, 30)

    def __init__(self, **kwargs):
        pass

    def login(self):
        try:
            username = config['username']
            password = config['password']
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['user_css_sel']))).send_keys(username)
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['pass_css_sel']))).send_keys(password)
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['login_css_sel']))).click()
        except Exception as e:
            print('Error: %s' % e)
            return False
        finally:
            return True

    def logout(self):
        sleep(10)
        driver.get(config['logout_url'])
        try:
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['logout_css_sel']))).click()
        except Exception as e:
            print('Error: %s' % e)
            driver.close()
            return False
        sleep(10)
        driver.quit()
        return True

    def search(self):
        tag = config['tag']
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['search_css_sel']))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['search_css_sel']))).send_keys(tag)
        sleep(10)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['search_for_css_sel']))).click()
        # OR
        # self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['search_1st_css_sel']))).click()
