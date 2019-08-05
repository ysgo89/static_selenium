# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from testrail import *
import os

# TestRail 접속 정보
client = APIClient('http://211.116.223.42/testrail')
client.user = 'goyoseb@suresofttech.com'
client.password = 'dudcks123!'

# STATIC 서버 아이디, 패스워드, 주소 정보
usr = "admin@static.io"
pwd = "!admin"
address = "http://211.116.222.204/login"

# 프로젝트 이름, 키
pName = "STATIC"
pKey = "PROKEY1"

# 업로드 배치파일 정보
dPath = "upload.bat"

class default(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def test_static_access(self):
        # STATIC 서버 열기 및 로그인
        driver = self.driver
        driver.get(address)
        driver.implicitly_wait(30)
        driver.find_element_by_id("email").send_keys(usr)
        driver.find_element_by_id("password").send_keys(pwd)
        driver.find_element_by_id("password").send_keys(Keys.RETURN)
        driver.implicitly_wait(30)

        # 프로젝트 전체 삭제하기
        # try :
        #     while 1:
        #         driver.find_element_by_css_selector("strong > a").click()
        #         driver.find_element_by_xpath("//div/a/span").click()
        #         driver.find_element_by_xpath("//nav/ul/li[6]/a/span").click()
        #         driver.find_element_by_xpath("//div[2]/button").click()
        #         #  프로젝트 이름 텍스트로 가져오기
        #         key_data = driver.find_element_by_xpath("//p[2]/strong").text
        #         # key_data = key.text
        #         driver.find_element_by_xpath("//div[2]/input").send_keys(key_data)
        #         driver.find_element_by_xpath("//div[3]/button/span").click()
        #
        # # 프로젝트가 없을 시 예외처리하여 프로젝트 생성 시도
        # except NoSuchElementException :
        #         driver.find_element_by_xpath("//div[2]/button/span").click()
        #         driver.find_element_by_xpath("//mat-form-field/div/div/div/input").send_keys(pName)
        #         driver.find_element_by_xpath("//mat-form-field[2]/div/div/div/input").send_keys(pKey)
        #         driver.find_element_by_xpath('//button[contains(text(), "Submit")]').click()

        # # 현재 파일의 폴더 위치 저장
        # pathSave = os.path.dirname(os.path.realpath(__file__))
        # print(pathSave)
        # # 현재 테스트 케이스의 위치로 이동
        # os.chdir(pathSave)
        # print(os.getcwd())
        # # 상위 폴더로 이동
        # os.chdir('../')
        # print(os.getcwd())
        # # dPath(upload.bat) 실행
        # os.system(dPath)


if __name__ == "__main__":
    unittest.main()