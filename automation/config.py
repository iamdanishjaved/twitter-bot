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

    # remember to add this path if you have not placed driver in your default directory,
    # In case of Firefox drive name should exclude extension like .exe otherwise, chromedriver.exe
    driver_path='C:\\geckodriver'
)
