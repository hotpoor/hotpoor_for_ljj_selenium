#!/bin/env python
#coding=utf-8
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/vendor/')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import requests,json


import time
import base64
# driver_path = "./chromedriver"
# browser = webdriver.Chrome(driver_path)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
browser = driver
browser.get('https://waifulabs.com/')
browser.implicitly_wait(20)

ele_imgs = None
def find_imgs():
    try:
        js = 'document.getElementsByClassName("button-content")[0].click();'  #js去掉上传文件“input”元素的属性，使之可见
        browser.execute_script(js)
        browser.implicitly_wait(20)
        imgs = browser.find_elements_by_class_name("girl")
        # imgs[0].children[0].children[0].children[1].children[0]
    except:
        print("except")
    finally:
        print("finally")
    return imgs
def more_imgs():
    try:
        js = 'document.getElementsByClassName("refresh-button")[0].click();'  #js去掉上传文件“input”元素的属性，使之可见
        browser.execute_script(js)
        browser.implicitly_wait(20)
        imgs = browser.find_elements_by_class_name("girl")
        # imgs[0].children[0].children[0].children[1].children[0]
    except:
        print("except")
    finally:
        print("finally")
    return imgs

ele_imgs = find_imgs()
get_imgs = []
for img in ele_imgs:
    img_html = img.get_attribute("outerHTML")
    img_html_uri = img_html.split("base64,")[1].split("&quot;)")[0]
    # print(img_html_uri)
    get_imgs.append(img_html_uri)
for img in get_imgs:
    # img_url = img
    # img_response = requests.get(img_url)
    t = int(round(time.time() * 1000))  # 毫秒级时间戳
    f = open(os.path.join(os.path.dirname(__file__),'./files/%s.%s'%(t,"jpg")), "ab")
    # f.write(img_response.content)  # 多媒体存储content
    imgdata = base64.b64decode(img)
    f.write(imgdata)
    f.close()
while True:
    ele_imgs = more_imgs()
    get_imgs = []
    for img in ele_imgs:
        img_html = img.get_attribute("outerHTML")
        img_html_uri = img_html.split("base64,")[1].split("&quot;)")[0]
        # print(img_html_uri)
        get_imgs.append(img_html_uri)
    for img in get_imgs:
        # img_url = img
        # img_response = requests.get(img_url)
        t = int(round(time.time() * 1000))  # 毫秒级时间戳
        f = open(os.path.join(os.path.dirname(__file__),'./files/%s.%s'%(t,"jpg")), "ab")
        # f.write(img_response.content)  # 多媒体存储content
        imgdata = base64.b64decode(img)
        f.write(imgdata)
        f.close()
    time.sleep(10)