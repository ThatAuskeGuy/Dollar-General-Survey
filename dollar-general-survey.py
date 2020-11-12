import selenium

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import random
from selenium.common.exceptions import NoSuchElementException


time_visited = input('Time of visit (HH:MM): ').split(':')
store_num = input('Store Number: ')
survey_code = input('Survey Code (xxxx-xxxx-xxxx-xxx): ' ).split('-')
name = input('First and Last Name (Joe Mama): ').split()
phone = input('Phone Number (555-555-5555): ')
email = input('Email: ')

""" Driver setup """
driver = webdriver.Chrome("../chromedriver")
driver.get("http://www.dgcustomerfirst.com")

""" Definitions """
def next_button():
    driver.find_element_by_xpath('//*[@id="NextButton"]').click()

def questions():
    ids = driver.find_elements_by_xpath('//*[contains(@id, "FNSR")]')
    try:
        for ii in ids:
            attr = ii.get_attribute('id')
            driver.find_element_by_xpath(('//*[@id="{}"]/td[3]/span').format(attr)).click()
    except NoSuchElementException:
        try:
            attr = ii.get_attribute('id')
            driver.find_element_by_xpath(('//*[@id="{}"]/div[3]/div/div[2]').format(attr)).click()
        except NoSuchElementException:
            attr = ii.get_attribute('id')
            driver.find_element_by_xpath(('//*[@id="{}"]/div[2]/div/div[1]/span/span').format(attr)).click()

def textbox():
    fill_text = ['I was just not overly satisfied by my experience', 'I just found it to be satisfactory', 'It was just a quick trip to get some food. I wasn\'t looking for an excellent experience.']
    rand_text = random.choice(fill_text)
    driver.find_element_by_xpath('//*[starts-with(@id, "S")]').send_keys(rand_text)

def checkboxes():
    ids = driver.find_elements_by_xpath('//*[contains(@id, "FNSR")]')
    for ii in ids:
        attr = ii.get_attribute('id')
        random_number = random.choice([0,1,2])
        if random_number == 1:
            driver.find_element_by_xpath(('//*[@id="{}"]/span/span').format(attr)).click()

def sweepstakes_entry():
    sweepstakes_items = [name[0], name[1], phone, email, email]
    ids = driver.find_elements_by_xpath('//*[starts-with(@id, "S")]')
    n = 0
    for ii in ids:
        attr = ii.get_attribute('id')
        driver.find_element_by_xpath(('//*[@id="{}"]').format(attr)).send_keys(sweepstakes_items[n])
        n+=1
    driver.find_element_by_xpath('//*[contains(@id, "FNSR")]').click()



""" Survey information screen """
Select(driver.find_element_by_xpath(('//*[@id="InputHour"]'))).select_by_visible_text(time_visited[0]) # time of visit - hour
Select(driver.find_element_by_xpath(('//*[@id="InputMinute"]'))).select_by_visible_text(time_visited[1]) # time of visit - minute
driver.find_element_by_xpath('//*[@id="InputStoreNum"]').send_keys(store_num) # store number
n = 1
for num in survey_code:
    driver.find_element_by_xpath('//*[@id="CN{}"]'.format(n)).send_keys(survey_code[n-1]) # survey code
    n+=1
next_button()

""" Survey Questionaire """
sweepstakes = False

while sweepstakes != True:
    try:
        driver.find_element_by_xpath('//*[@id="FNSR000043"]/div[2]/div/div[1]/span/span').click()
        sweepstakes = True
        next_button()
        sweepstakes_entry()
        next_button()
    except NoSuchElementException:
        try: 
            questions()
            next_button()
        except NoSuchElementException:
            try:
                textbox()
                next_button()
            except NoSuchElementException:
                try:
                    checkboxes()
                    next_button()
                except:
                    break
