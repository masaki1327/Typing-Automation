import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

with webdriver.Chrome() as driver:
    driver.get('https://manabi-gakushu.benesse.ne.jp/gakushu/typing/homeposition.html')
    #driver.get('https://manabi-gakushu.benesse.ne.jp/gakushu/typing/nihongonyuryoku.html')
    #driver.get('https://manabi-gakushu.benesse.ne.jp/gakushu/typing/eigonyuryoku.html')
    
    #time.sleep(1)
    
    elem = driver.find_element(By.ID, "goSettingButton")
    elem.click()
    elem = driver.find_element(By.ID, "timeLimitButton")
    elem.click()
    #time.sleep(1)
    elem.send_keys(Keys.LEFT)
    #time.sleep(1)
    elem.send_keys(Keys.LEFT)
    #time.sleep(1)
    elem = driver.find_element(By.CLASS_NAME, "typingButton")
    elem.click()

    #time.sleep(1)
    body_element = driver.find_element(By.TAG_NAME, 'body')
    body_element.send_keys(Keys.SPACE)

    time.sleep(3)

    while True:
        sentence = driver.find_element(By.ID, "remaining").text
        print(sentence)
        for key in(sentence):
            body_element.send_keys(key)
            time.sleep(0.05)