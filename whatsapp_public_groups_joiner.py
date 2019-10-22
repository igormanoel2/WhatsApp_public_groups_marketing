# script to go through a list of whatsapp groups and join them.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import sys, time, random
import logging, os
import io

# Logging into the whatsapp account and setting up the browser
print("Waiting for the QR code . . .", file=sys.stderr)
LOGGER.setLevel(logging.WARNING)
driver = webdriver.Chrome(
    executable_path='/Users/Elyes Kouki/Desktop/GeeksData/Lead_Detection/chromedriver/chromedriver.exe')
driver.set_page_load_timeout(30)
driver.get("https://web.whatsapp.com")
wait = WebDriverWait(driver, 600)
time.sleep(30)

# oppening the groups list text file 
with io.open('what_pub_groups.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    count = 1  # a veriabel andicating our position in the file

for line in lines:
    # Loading the group link
    print(str(count) + "  processing " + line, file=sys.stderr)
    driver.get(line)
    driver.implicitly_wait(7)
    try:

        # hitting the first join bouton
        join_button = driver.find_element_by_css_selector("#action-button")
        join_button.click()
        time.sleep(7)

        # hitting the second join bouton
        join_group_button = driver.find_element_by_xpath(
            "/html/body/div[@id='app']/div[@class='_1FPJ- _39gtr app-wrapper-web']/span[2]/div[@class='_2t4Ic']/div/div/div/div/div/div[@class='_2NdzR']/div[@class='_2eK7W _3PQ7V']")
        join_group_button.click()
        count += 1




    except:
        print("unable to join group ... " + line, file=sys.stderr)
        count += 1
        pass
        # giving the browser time to load 
    sleep_time = random.randint(7, 9)
    time.sleep(sleep_time)
driver.close()
