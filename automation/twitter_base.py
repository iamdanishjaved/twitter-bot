from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from automation.config import config


class Twitter:
    # add this wait so that your browser load HTML, and then you start locating your tags/selectors

    def __init__(self, browser):
        # Use one of the following, according to your setup
        try:
            if browser == 'chrome':
                self.driver = webdriver.Chrome(executable_path=config['chrome_driver_path'])
            else:
                self.driver = webdriver.Firefox(executable_path=config['driver_path'])
            self.wait = WebDriverWait(self.driver, 30)
        except Exception as e:
            print('[__init__] -- Error: %s' % e)
            try:
                self.driver.close()
            except:
                pass

    def login(self):
        try:
            self.driver.get(config['login_url'])
            username = config['username']
            password = config['password']
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['user_css_sel']))).send_keys(username)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, config['user_xpath_next']))).click()
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['pass_css_sel']))).send_keys(password)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, config['login_button_xpath_sel']))).click()
        except Exception as e:
            print('[login] -- Error: %s' % e)
            return self.driver.close()
        finally:
            print('[login] -- Logged In successfully!')
            return True

    def logout(self):
        sleep(10)
        self.driver.get(config['logout_url'])
        try:
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['logout_css_sel']))).click()
        except Exception as e:
            print('[logout] -- Error: %s' % e)
            self.driver.close()
            return False
        sleep(10)
        self.driver.quit()
        return True

    def search(self):
        try:
            tag = config['tag']
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['search_css_sel']))).click()
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['search_css_sel']))).send_keys(tag)
            sleep(10)
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, config['search_for_css_sel']))).click()
        except Exception as e:
            print('[search] -- Error: %s' % e)
            self.driver.close()
