from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib import request
from PIL import Image
import datetime,io



dt_now = datetime.datetime.now()
dt_now = dt_now.strftime('%Y年%m月%d日_%H時%M分%S秒')

def img_get():

    tan = []

    url ="https://www.toyama-douro.toyama.toyama.jp/kl/camimg/camimg239.jpg"

    driver = "C:/Program Files/Google/Chrome/chromedriver.exe"

    driver = webdriver.Chrome(driver)
    driver.get(url)

    img_elem = driver.find_element(by=By.XPATH, value='/html/body/img')
    img_elem = img_elem.get_attribute('src')
    f = io.BytesIO(request.urlopen(img_elem).read())
    img = Image.open(f)

    img.save(fr'I:/python/amedas/{dt_now}.jpeg')
    
    return


img_get()