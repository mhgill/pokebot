from selenium import webdriver
import time
import sys

def get_battle_url():
    base = 'https://zeta.pokemon-vortex.com/map/'
    url = 'https://zeta.pokemon-vortex.com/map/11'
    inp = raw_input("Enter Map number (default: 11): ")
    try:
        if int(inp) >= 2 and int(inp) <= 17:
            return base+inp
    except:
        return url

def getuser():
    return raw_input("Enter your username for login: ")

def getpass():
    return raw_input("Enter your password for login: ")

def battle(browser, delay, user, password,  url ):
    login(browser_handle,
          'https://www.pokemon-vortex.com/login/',
          '//*[@id="submit"]',
          '//*[@id="myusername"]',
          '//*[@id="mypassword"]',
          user,
          password,
          url
          )
    fail = 0
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
            time.sleep(delay)
            level=0
            try:
                level_text=browser.find_element_by_xpath('//*[@id="pkmnappear"]/form/p').text
                level = int(level_text[level_text.index(':') + 1:].strip())
            except:
                pass

            if level >= 50:
                break
            else:
                fail += 1


            if fail%2==0:
                browser.find_element_by_xpath('//*[@id="arrows"]/table/tbody/tr[1]/td[2]/img').click()
            else:
                browser.find_element_by_xpath('//*[@id="arrows"]/table/tbody/tr[3]/td[2]/img').click()

        except:
            pass


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
    inp = raw_input("\nEnter the Speed for searching (1-10) 1-Fastest, 10-slowest, note that if the speed\nis too high, than the bot might miss some pokemon (Default: 3): ")
    n = 0
    if len(inp) > 0:
        n = float(inp) / 10.0
    if n >= 0.1 and n <= 1:
        return n
    return default

def browser_choice():
    choicen = raw_input("Do you have the chrome browser? The bot only runs on chrome, press enter to continue... ")
    return webdriver.Chrome(sys.path[0] + "/chromedriver")

starting_message = "Welcome to this legendary searcher bot by GE Inc."
instructions = "To start the bot, enter all the paramaters that you will be asked for,\nif a parameter has a default value, you may press 'Enter' to use the default value. \nMake sure that the arrow keys on the map and the level text are in view, so the bot can see them."

print starting_message
print instructions
print "\n"
url = get_battle_url()
speed = get_speed()
user = getuser()
password = getpass()
browser_handle = browser_choice()

try:
    battle(browser_handle, speed, user, password, url)
except Exception as e:
    print e.__doc__
    print e.message
    print "Error...either you closed the window, or do not have the required browser. Press any key to exit"
    raw_input()
