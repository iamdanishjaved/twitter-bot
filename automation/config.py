config = dict(
    login_url='https://twitter.com/login',
    logout_url='https://twitter.com/logout',
    username='your_email_or_username',
    password='your_password',

    # update CSS selectors here, if you are using xpath then login function will be change like "By.XPATH"
    user_css_sel='input[name="text"]',
    user_xpath_next="//span[text()='Next']",
    pass_css_sel='input[name="password"]',
    login_button_xpath_sel="//span[text()='Log in']",
    logout_css_sel='[data-testid="confirmationSheetConfirm"]',
    search_css_sel='[placeholder="Search Twitter"]',
    search_for_css_sel='[data-testid="TypeaheadUser"]',
    # remember to add this path if you have not placed driver in your default directory,
    # In case of Firefox drive name should exclude extension like .exe otherwise, chromedriver.exe
    driver_path='C:\\geckodriver',
    chrome_driver_path='C:\\chromedriver',
    tag='iamdanishjaved'
)
