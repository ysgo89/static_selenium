import default_setting
import unittest
import time
from random import *
import random

# Test Case_id 정보
case_id = 41888

class C18983(unittest.TestCase):
    def test_C18983(self):
        # default_setting 수행
        setglob = default_setting
        p = default_setting.default()
        p.setUp()
        p.test_static_access()

        # 한글 및 숫자를 랜덤으로 받기 위한 객체 생성
        list = ('사과', '감자', '포도', '수박', '낑깡', '요셉')
        i = randint(1, 100)
        s = random.sample(list, 1)

        # 확인용 객체 생성
        valCheck = "Key must only alphanumeric characters."
        valCheck1 = "Create Project"


        try:
            # random, sample 함수를 이용해 프로젝트 키에 한글+숫자 입력
            p.driver.find_element_by_xpath("//div[2]/button/span").click()
            p.driver.find_element_by_xpath("//mat-form-field/div/div/div/input").send_keys(setglob.pName)
            p.driver.find_element_by_xpath("//mat-form-field[2]/div/div/div/input").send_keys(s)
            p.driver.find_element_by_xpath("//mat-form-field[2]/div/div/div/input").send_keys(i)
            p.driver.find_element_by_xpath('//button[contains(text(), "Submit")]').click()
            time.sleep(1)

            self.assertEqual(valCheck, p.driver.find_element_by_id("mat-error-1").text)
            self.assertEqual(valCheck1, p.driver.find_element_by_css_selector("span.title").text)
            time.sleep(1)
            status_id = 1
        except :
            status_id = 5

         # Test Rail 결과 입력
        if status_id == 1:
            print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (setglob.run_id, case_id, setglob.passMsg))
            setglob.client.send_post(
                'add_result_for_case/%s/%s' % (setglob.run_id, case_id),
                {'status_id': status_id, 'comment': setglob.passMsg, })

        elif status_id == 5:
            print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (setglob.run_id, case_id, setglob.failMsg))
            setglob.client.send_post(
                'add_result_for_case/%s/%s' % (setglob.run_id, case_id),
                {'status_id': status_id, 'comment': setglob.failMsg, })

if __name__ == "__main__":
    unittest.main()