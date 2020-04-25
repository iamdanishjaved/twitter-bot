config = dict(
    login_url='https://twitter.com/login',
    logout_url='https://twitter.com/logout',
    username='your_email_username_phone',
    password='your_password',

    # update CSS selectors here, if you are using xpath then login function will be change like "By.XPATH"
    user_css_sel='div.css-1dbjc4n:nth-child(6) > label input',
    pass_css_sel='div.css-1dbjc4n:nth-child(7) > label input',
    login_css_sel='.r-jwli3a',
    logout_css_sel='.r-jwli3a > span:nth-child(1) > span:nth-child(1)',
    search_css_sel='.r-30o5oe',
    search_for_css_sel='div.r-9qu9m4:nth-child(1) > span:nth-child(1)',
    search_1st_css_sel='#typeaheadDropdown-1 > div:nth-child(3) > div:nth-child(1) > li:nth-child(1) > '
                       'div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > '
                       'div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)',
    # remember to add this path if you have not placed driver in your default directory,
    # In case of Firefox drive name should exclude extension like .exe otherwise, chromedriver.exe
    driver_path='C:\\geckodriver',
    chrome_driver_path='C:\\geckodriver',
    tag='iamdanishjaved'
)
