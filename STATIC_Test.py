# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re


usr = "admin@static.io"
pwd = "!admin"

class app(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def test_static_access(self):
        driver = self.driver
        driver.get("http://211.116.222.164/login")
        driver.implicitly_wait(30)
        assert "STATIC" in self.driver.title # 타이틀이 STATIC 인지 확인

        driver.find_element_by_id("email").send_keys(usr)
        driver.find_element_by_id("password").send_keys(pwd)
        driver.find_element_by_id("password").send_keys(Keys.RETURN)

        # 초기 화면 Projects의 Create 버튼 클릭
        driver.find_element_by_xpath('//b[contains(text(), "Create")]').click()
        time.sleep(10)

# 프로젝트 이름, 키 저장
# pName="STATIC"
# pKey="PROKEY1"
#
# # Project Name, Key 필드 값 입력
# elem = driver.find_element_by_id("mat-input-0")
# elem.send_keys(pName)
# elem = driver.find_element_by_id("mat-input-1")
# elem.send_keys(pKey)

# 버튼 Class? 로 찾기
# elem = driver.find_element_by_css_selector("button.btn.btn-brand-primary")

# 버튼의 이름으로 찾기
# elem = driver.find_element_by_xpath('//button[contains(text(), "Submit")]').click()

# 프로젝트 리스트 검색
# pList = driver.find_element_by_xpath(('//div
# print(pList)
# # body > app-root > app-common-layout > div > div > app-projects > div > div.list-layout > div
#
# body > app-root > app-common-layout > div > div > app-projects > div > div.list-layout > div > div > div
# /html/body/app-root/app-common-layout/div/div/app-projects/div/div[3]/div/div/div
# document.querySelector("body > app-root > app-common-layout > div > div > app-projects > div > div.list-layout > div > div > div")

if __name__ == "__main__":
    unittest.main()