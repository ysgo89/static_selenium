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

# 아이디, 패스워드
usr = "admin@static.io"
pwd = "!admin"

# 프로젝트 이름, 키
pName = "STATIC"
pKey = "PROKEY1"

class app(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def test_static_access(self):
        driver = self.driver
        # driver.get("http://211.116.222.164/login")
        driver.get("http://211.116.222.92/login")
        driver.implicitly_wait(30)
        assert "STATIC" in driver.title # 타이틀이 STATIC 인지 확인

        driver.find_element_by_id("email").send_keys(usr)
        driver.find_element_by_id("password").send_keys(pwd)
        driver.find_element_by_id("password").send_keys(Keys.RETURN)
        driver.implicitly_wait(30)

        # 프로젝트 상태 저장
        try :
            while 1:
                driver.find_element_by_css_selector("strong > a").click()
                driver.find_element_by_xpath("//div/a/span").click()
                driver.find_element_by_xpath("//nav/ul/li[6]/a/span").click()
                driver.find_element_by_xpath("//div[2]/button").click()
                #  프로젝트 이름 텍스트로 가져오기
                key = driver.find_element_by_xpath("//p[2]/strong")
                key_data = key.text
                driver.find_element_by_xpath("//div[2]/input").send_keys(key_data)

                # key_input = driver.find_element_by_xpath("//div[2]/input")
                # key_input.send_keys(key_data)
                driver.find_element_by_xpath("//div[3]/button/span").click()

        except NoSuchElementException :
            driver.find_element_by_xpath("//div[2]/button/span").click()
            driver.find_element_by_xpath("//mat-form-field/div/div/div/input").send_keys(pName)
            driver.find_element_by_xpath("//mat-form-field[2]/div/div/div/input").send_keys(pKey)
            # 프로젝트 생성 버튼 클릭
            # driver.find_element_by_css_selector("button.btn.btn-brand-primary")
            driver.find_element_by_xpath('//button[contains(text(), "Submit")]').click()

            time.sleep(5)



if __name__ == "__main__":
    unittest.main()