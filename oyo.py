import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s=Service('C:/Users/dell/Desktop/chromedriver.exe')
driver=webdriver.Chrome(service=s)

driver.get("https://www.oyorooms.com/")
time.sleep(3)

driver.find_elements(By.XPATH,value='//*[@id="root"]/div/div[3]/div[1]/div[2]/div/div[1]/a')[0].click()
time.sleep(8)

with open('oyobanglore.html', 'a', encoding='utf-8') as f:
    time.sleep(5)
    html = driver.page_source
    time.sleep(1)
    f.write(html+'\n\n')
    time.sleep(2)

for i in range(2,22):
    l=[2,3,4,5,6,7,8,9]
    m=[16,17,18,19,20,21]
    if i in l:
        driver.find_element(By.XPATH,value=f'//*[@id="root"]/div/div[3]/div/div/section/div[1]/div/div/a[{i}]').click()
        time.sleep(8)
        with open('oyobanglore.html', 'a', encoding='utf-8') as f:
            time.sleep(5)
            html = driver.page_source
            time.sleep(1)
            f.write(html+'\n\n')
            time.sleep(2)
    elif i in m:
        driver.find_element(By.XPATH,value=f'//*[@id="root"]/div/div[3]/div/div/section/div[1]/div/div/a[{i-6}]').click()
        time.sleep(8)
        with open('oyobanglore.html', 'a', encoding='utf-8') as f:
            time.sleep(5)
            html = driver.page_source
            time.sleep(1)
            f.write(html+'\n\n')
            time.sleep(2)
    else:
        driver.find_element(By.XPATH, value='//*[@id="root"]/div/div[3]/div/div/section/div[1]/div/div/a[9]').click()
        time.sleep(8)
        with open('oyobanglore.html','a',encoding='utf-8') as f:
            time.sleep(5)
            html=driver.page_source
            time.sleep(1)
            f.write(html+'\n\n')
            time.sleep(2)
driver.close()
