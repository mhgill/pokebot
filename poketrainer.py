from selenium import webdriver
import time
import sys

def get_battle_url():
    url = 'https://theta.pokemon-vortex.com/battle-user/381236'
    inp = raw_input("Enter Battle Url, Default is: 'https://theta.pokemon-vortex.com/battle-user/381236' :")
    if len(inp) < 5:
        return url
    return inp

def getuser():
    return raw_input("Enter your username for login: ")

def getpass():
    return raw_input("Enter your password for login: ")


def battle(browser, delay, user, password,  url, ):
    login(browser_handle,
          'https://www.pokemon-vortex.com/login/',
          '//*[@id="submit"]',
          '//*[@id="myusername"]',
          '//*[@id="mypassword"]',
          user,
          password,
          url
          )
    while True:
        if 'login' in browser.current_url:
            login(browser_handle,
                  'https://www.pokemon-vortex.com/login/',
                  '//*[@id="submit"]',
                  '//*[@id="myusername"]',
                  '//*[@id="mypassword"]',
                  user,
                  password,
                  url
                  )
        try:
            #browser.execute_script("window.scrollTo(0, 500)")
            time.sleep(delay)
            browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/form/p/input').submit()
            fails = 0
            continue
        except:
            fails += 1

        try:
            #browser.execute_script("window.scrollTo(0, 490)")
            time.sleep(delay)
            # attackbt and continue bt after 1 fight
            browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/form[2]/div/input[2]').submit()
            fails = 0
            continue
        except:
            fails+=1

        try:
            if fails > 25:
                browser.get(url)
                fails = 0
        except:
            fails += 1

def login(browser, login_url, submit_bt_xpath, user_box_xpath, pass_box_xpath, username,  password, targ_url):

    while browser.current_url != targ_url:
        browser.get(login_url)
        browser.find_element_by_xpath(user_box_xpath).send_keys(username)
        browser.find_element_by_xpath(pass_box_xpath).send_keys(password)
        try:
            browser.find_element_by_xpath(submit_bt_xpath).submit()
        except:
            pass

        try:browser.find_element_by_xpath(submit_bt_xpath).click()
        except :
            pass

        browser.get(targ_url)

def get_speed():
    default = 0.3
    try:
        inp = raw_input("\nEnter the Speed for Battling (1-10) 1-Fastest, 10-slowest,note that if the speed\nis too high, than the bot will finish the battles too quickly (meaning 0 exp)\nor if your pokemon team loses, you will not get any exp or cash (Default: 3): ")
        n = 0
        if len(inp) > 0:
            n = float(inp) / 10.0
        if n >= 0.1 and n <= 1:
            return n
    except:
        return default

def browser_choice():
    choicen = raw_input("Do you have the chrome browser? The bot only runs on chrome, press enter to continue... ")
    return webdriver.Chrome(sys.path[0] + "/chromedriver")


starting_message = "Welcome to this battle bot by GE Inc.\n"
instructions = "To start the bot, enter all the paramaters that you will be asked for, " + "\n" + "if a parameter has a default value, you may press 'Enter' to use the default value." + "\n" + "Your first pokemon will be the battle pokemon, You should find a good opponent\nthat one of your pokemon can defeat easily to maximize income.\nThe example (default) url provided is for high level fire pokemon."

print starting_message
print instructions
print "\n"
url = get_battle_url()
speed = get_speed()
print "\n"
user = getuser()
print "\n"
password = getpass()
print "\n"
browser_handle = browser_choice()

try:
    battle(browser_handle, speed, user, password, url)
except:
    print "Error...either you closed the window, or do not have the required browser. Press any key to exit"
    raw_input()