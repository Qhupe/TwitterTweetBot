from selenium import webdriver
import time
import random
import string


from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://twitter.com/")
kullanici_adi = str('username')
time.sleep(1)


giris_yap = browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span/span")
giris_yap.click()

time.sleep(3)

giris_yap = browser.find_element(By.XPATH,"/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a/div/span/span")
giris_yap.click()
time.sleep(3)
browser.find_element(By.NAME,'username').send_keys(kullanici_adi)
butonnext=browser.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div")
butonnext.click()
time.sleep(2)
browser.find_element(By.NAME,"password").send_keys("inputyourpassword")
time.sleep(2)
buttongiris=browser.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div")
buttongiris.click()
time.sleep(3)

latters=string.ascii_uppercase

harfdizi=list(latters)
print(harfdizi)


latters=string.ascii_uppercase
harfdizi=list(latters)
harfdizi.remove("Q")
harfdizi.remove("W")
harfdizi.remove("X")
kelime=""

for i in range(500):
    listharf = []

    kelime=""
    for i in range(6):
        harf = random.choice(harfdizi)
        listharf.append(harf)

    print(listharf)

    for i in listharf:
        listkelime = list()
        sözlük = open("sözlük\{}.txt".format(i), encoding="utf-8")
        listkelime = sözlük.read().split("\n")
        sayirand = random.randint(0, len(listkelime)-1)
        print(sayirand)
        kelime = kelime +" "+listkelime[sayirand]
    print(kelime)



    browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div").send_keys("# {}".format(kelime))
    butonTweet = browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div")
    butonTweet.click()
    time.sleep(2)
    del listkelime
    del listharf
