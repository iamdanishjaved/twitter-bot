from time import sleep
from automation.twitter_base import Twitter


if __name__ == '__main__':
    twitter = Twitter()
    login = twitter.login()
    if login:
        twitter.search()
        sleep(60)
        twitter.logout()
    else:
        print('Some error occurred. Please fix issue and try again.')
        exit()
