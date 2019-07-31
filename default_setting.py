# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-
from nose.tools import assert_is_not
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from testrail import *
import os

# STATIC 서버 아이디, 패스워드 정보
usr = "admin@static.io"
pwd = "!admin"

# 프로젝트 이름, 키
pName = "STATIC"
pKey = "PROKEY1"

# TestRail 접속 정보
client = APIClient('http://211.116.223.42/testrail')
client.user = 'goyoseb@suresofttech.com'
client.password = 'dudcks123!'

# TestRail run_id, Testcase_id, Message 정보
run_id = 240
case_id = 30722
msg = 'Test Auto Checking'

# 데이터 업로드 파일 경로
dPath = "upload.bat"

class app(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def test_static_access(self):
        driver = self.driver
        driver.get("http://211.116.222.92/login")
        driver.implicitly_wait(30)
        driver.find_element_by_id("email").send_keys(usr)
        driver.find_element_by_id("password").send_keys(pwd)
        driver.find_element_by_id("password").send_keys(Keys.RETURN)
        driver.implicitly_wait(30)

        # 프로젝트 전체 삭제하기
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

        # 프로젝트가 없을 시 예외처리하여 프로젝트 생성 시도
        except NoSuchElementException :
                driver.find_element_by_xpath("//div[2]/button/span").click()
                driver.find_element_by_xpath("//mat-form-field/div/div/div/input").send_keys(pName)
                driver.find_element_by_xpath("//mat-form-field[2]/div/div/div/input").send_keys(pKey)
                driver.find_element_by_xpath('//button[contains(text(), "Submit")]').click()

        # 배치파일 열기
        os.system(dPath)

        # TestRail 결과 입력
        # try :
        #     assert "STATIC11" in driver.title
        #     status_id = 1
        # except :
        #     status_id = 5
        #
        # client.send_post(
        #     'add_result_for_case/%s/%s' % (run_id, case_id),
        #     {'status_id': status_id, 'comment': msg,})
        # print('\n Run ID : %s\n Test Case ID: %s\n Message : %s\n' % (run_id, case_id, msg))


if __name__ == "__main__":
    unittest.main()