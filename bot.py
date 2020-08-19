from time import sleep
import random
import math
import chromedriver_autoinstaller
from keyboard import press
from selenium import webdriver

# //Global variables
email = "****"
password = "*****"


def get_browser():
    global browser
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.get(r"https://linkedin.com")


def sign_in(username, password):
    signIn = browser.find_element_by_link_text('Sign in')
    signIn.click()
    sleep(random.uniform(2, 4))
    enter_mail = browser.find_element_by_id('username')
    enter_pass = browser.find_element_by_id('password')
    enter_mail.send_keys(email)
    enter_pass.send_keys(password)
    sleep(random.uniform(3, 4))
    click_login = browser.find_element_by_class_name('btn__primary--large')
    click_login.click()


def withdraw_page():  # My Network
    browser.find_element_by_xpath("//html/body/header/div/nav/ul/li[2]/a").click()
    sleep(random.uniform(3, 4))
    # Mange
    browser.find_element_by_xpath("//a [contains (@href, '/mynetwork/invitation-manager')]").click()
    sleep(random.uniform(2, 4))
    # Sent
    browser.find_element_by_xpath("//button [contains (@class, 'artdeco-tab ember-view')]").click()
    sleep(random.uniform(2, 4))
    # number of people that received invitation
    num = browser.find_element_by_xpath("//span [contains (@class, 'artdeco-pill__text')]").get_attribute('innerText')
    start = int(num.find('(')) + 1
    stop = num.find(')')
    numA = num[start:stop]
    pages = math.ceil(int(numA) / 100)
    single = (int(numA) % 100) + 1
    for i in range(1, pages):
        p = 101
        withdraw_click(p)
        # Next button
        browser.find_element_by_xpath("//section [contains (@class, 'mn-invitation-manager__artdeco-card')]//div/div[2]/div/button[2]").click()
    withdraw_click(single)  # last page
    print("End of withdraw function")


def withdraw_click(p):
    for x in range(1, p):
        time = browser.find_element_by_xpath("//ul [contains (@class, 'artdeco-list mn-invitation-list')]//li[" + str(x) + "]/div/div[1]/div/time")
        sleep(random.uniform(2, 4))
        if time.get_attribute('innerText')[2:7] == 'weeks' or time.get_attribute('innerText')[2:6] == 'week':  # to long time
            # withdraw button
            browser.find_element_by_xpath("//ul [contains (@class, 'artdeco-list mn-invitation-list')]//li[" + str(x) + "]/div/div[2]/button").click()
            sleep(random.uniform(2, 4))
        print(time.get_attribute('innerText')[2:7])
        scroll_page_down(time)


def search():
    click_search = browser.find_element_by_id('ember41')
    click_search.click()
    sleep(random.uniform(1, 4))
    # people  
    browser.find_element_by_xpath("//ul [contains (@class, 'search-typeahead-v2__entry-point-list display-flex')]//li[1]").click()
    sleep(random.uniform(4, 6))
    click_all_filters = browser.find_element_by_xpath("//button [contains (@class, 'search-filters-bar__all-filters flex-shrink-zero mr3 artdeco-button artdeco-button--muted ')]")

    sleep(random.uniform(2, 4))
    click_all_filters.click()
    sleep(random.uniform(4, 6))

    browser.find_element_by_xpath("//label[text()='2nd']").click()  # Connections 2nd Add connection of
    sleep(random.uniform(3, 5))
    enter_connection = browser.find_element_by_xpath("//input[@placeholder='Add connection of']")  # Add connection of
    enter_connection.send_keys('****')
    sleep(random.uniform(4, 6))
    press('down')
    sleep(random.uniform(1, 3))
    press('enter')
    sleep(random.uniform(2, 4))
    industries = browser.find_element_by_xpath("//input[@placeholder='Add an industry']")  # industries
    sleep(random.uniform(1, 3))
    industries.click()
    sleep(random.uniform(1, 3))
    industries.send_keys('Human Resources')
    sleep(random.uniform(1, 3))
    press('down')
    sleep(random.uniform(1, 3))
    press('enter')
    sleep(random.uniform(4, 7))
    browser.find_element_by_class_name('search-advanced-facets__button--apply').click()  # choose Apply
    sleep(random.uniform(2, 4))


def get_page():
    element = browser.find_element_by_class_name('search-results__total')
    text = element.get_attribute('innerText')
    if int(text.split()[0]) % 10 == 0:
        page = int(text.split()[0]) / 10  # number of pages of connection
    else:
        page = math.ceil(int(text.split()[0]) / 10)
    print(page)
    for x in range(1, int(page)):  # Next Button
        if page > 2:
            n = 11
            send_invite(n)

            nextBtn = browser.find_element_by_xpath("//button [contains (@class, 'artdeco-pagination__button artdeco-pagination__button--next artdeco-button')]")
            scroll_page_down(nextBtn)
            sleep(random.uniform(3, 5))
            nextBtn.click()
            sleep(random.uniform(3, 5))
    sleep(random.uniform(3, 5))
    n = int(text.split()[0]) % 10 + 1  # first or last page
    send_invite(n)
    sleep(random.uniform(2, 4))


def send_invite(n):
    print(n)
    for x in range(1, int(n)):
        status = browser.find_element_by_xpath("//ul [contains (@class, 'search-results__list list-style-none')]/li[" + str(x) + "]/div/div/div[3]/div/button")
        sleep(random.uniform(1, 3))

        if status.get_attribute('innerText') == 'Connect':
            status.click()
            sleep(random.uniform(2, 4))
            button2 = browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")  # Send now
            button2.click()
        scroll_page_down(status)
        sleep(random.uniform(1, 3))


def scroll_page_down(element):
    browser.execute_script("arguments[0].scrollIntoView()", element)
    sleep(random.uniform(1, 3))


def key_word():
    # My Network
    browser.find_element_by_xpath("//html/body/header/div/nav/ul/li[2]/a").click()
    sleep(random.uniform(3, 4))
    elm = browser.find_element_by_xpath("//h2[text()='More suggestions for you']")
    sleep(random.uniform(3, 4))
    browser.execute_script("arguments[0].scrollIntoView()", elm)
    sleep(random.uniform(4, 7))
    for x in range(1, 50):
        print(x)
        about = browser.find_element_by_xpath("//div[contains(@data-launchpad-scroll-anchor, 'pymk')]/section/section/ul/li[" + str(x) + "]/div/section/div[1]/a/span[4]").get_attribute('innerText').lower()
        matches = ["hr", "talent acquisition", "technical recruiter", "human resource", "i'm hiring", "hire", "recruitment"]

        if any(y in about for y in matches):
            browser.find_element_by_xpath("//div[contains(@data-launchpad-scroll-anchor, 'pymk')]/section/section/ul/li[" + str(x) + "]/div/section/div[2]/footer/button").click()
        sleep(random.uniform(2, 3))
        if x % 4 == 0:
            el = browser.find_element_by_xpath("//div[contains(@data-launchpad-scroll-anchor, 'pymk')]/section/section/ul/li[" + str(x + 1) + "]")
            scroll_page_down(el)


def menu():
    print("1. Friend's HR \n2. Key word ")
    choice = input()
    return choice


def main():
    ch = menu()
    get_browser()
    sleep(random.uniform(2, 4))
    sign_in(email, password)
    sleep(random.uniform(3, 4))
    withdraw_page()
    sleep(random.uniform(3, 4))

    if ch == "1":
        print("Friend")
        search()
        sleep(random.uniform(2, 4))
        get_page()
        sleep(random.uniform(2, 4))
    if ch == "2":
        print("Key word")
        key_word()

    print("Finish")


if __name__ == '__main__':
    main()
