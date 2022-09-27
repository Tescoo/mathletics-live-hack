import undetected_chromedriver as uc
import time, requests, json, random, os, sys, threading, uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

username = "XX-000000"
password = "xxxxxx00"
threads = 5 # please dont do anymore than 10, or pc will crash/will be too slow


def main():
    try:
        uuidlad = str(uuid.uuid4())
        chrome_options = Options()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument("--headless")
        driver = uc.Chrome(options = chrome_options)
        print("[~] Driver started!"+ " (" + uuidlad + ")")
        driver.get('https://login.mathletics.com/')
        login = driver.find_elements(By.CLASS_NAME, "input---192oZ")
        ewfw = driver.find_elements(By.CLASS_NAME, "check-button---2jvQy")
        login[0].send_keys(username)
        login[1].send_keys(password)
        ewfw[1].click()
        br = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/p[1]/button")
        br.click()
        time.sleep(4)
        print("[!] Logged in"+ " (" + uuidlad + ")")
        while True:
            try:
                ewfw = driver.find_elements(By.CLASS_NAME, "header-label---3lpN-")[2]
                ewfw.click()
                break
            except:
                pass
        print("[DEBUG] Clicked tab"+ " (" + uuidlad + ")")
        time.sleep(6)
        br = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div/div/article/section/div[1]/carousel/section-panel/scale-nine-container/div/scale-nine-container/div/div/div/ul/carousel-item[1]/li")
        print("[DEBUG] Clicked mathletics live"+ " (" + uuidlad + ")")
        br.click()
        time.sleep(6)
        print("[!] Authenticated to live mathletics"+ " (" + uuidlad + ")")
        while True:
            driver.get('https://live.mathletics.com/#/splashscreen')
            time.sleep(5)
            while True:
                try:
                    br = driver.find_elements(By.CLASS_NAME, "button_Go")[0].click()#
                    break
                except:
                    pass
            print("[~] Searching for match..."+ " (" + uuidlad + ")")
            while True:
                while True:
                    try:
                        nums = driver.find_element(By.CLASS_NAME, 'questions-text-alignment')
                        break
                    except:
                        pass
                print("[!] Game started"+ " (" + uuidlad + ")")
                while True:
                    try:
                        nums = driver.find_element(By.CLASS_NAME, 'questions-text-alignment').get_attribute('innerText')
                        add = nums.split('+' and '=')
                        ans = eval(add[0])
                        print("[!] Answered question, ANS: " + str(ans)+ " (" + uuidlad + ")")
                        aa = driver.find_element(By.CLASS_NAME, "questions-input-width-v3")
                        aa.send_keys(ans)
                        aa.send_keys(Keys.ENTER)
                        time.sleep(random.choice([0.3,0.3, 0.7, 1]))
                    except:
                        print("[!] Game ended!"+ " (" + uuidlad + ")")
                        time.sleep(6)
                        driver.get('https://live.mathletics.com/#/splashscreen')
                        break
                    
                break
    except Exception as e:
        print("[!?] Issue: " + str(e))



for i in range(threads):
    threading._start_new_thread(main, ())

while True:
    time.sleep(200)
