from Test_Suite.default_setting import *
from testrail import *
import unittest
import time
import os

# TestRail 접속 정보
client = APIClient('http://211.116.223.42/testrail')
client.user = 'goyoseb@suresofttech.com'
client.password = 'dudcks123!'

# TestRail run_id, Test Case_id, Message 정보
run_id = 240
case_id = 18701
msg = 'Test Run complete'

class C18701(unittest.TestCase):
    def test_C18701(self):
        # default_setting 수행
        p: default = default()
        p.setUp()

        # 비유효한 값으로 로그인
        p.driver.get(address)
        p.driver.implicitly_wait(30)
        p.driver.find_element_by_id("email").send_keys("admin@stati.ciopioiii")
        p.driver.find_element_by_id("password").send_keys("abcd12fddd")
        p.driver.find_element_by_id("password").send_keys(Keys.RETURN)
        
        # 팝업창 문구 체크
        popCheck = p.driver.find_element_by_xpath("//ngb-alert").text
        print(popCheck)

        # TestRail 결과 입력
        try :
            # 인증 실패 시 출력되는 문구 비교
            self.assertEqual("×\nInvalid Credentials",popCheck)
            status_id = 1
        except :
            status_id = 5

        client.send_post(
            'add_result_for_case/%s/%s' % (run_id, case_id),
            {'status_id': status_id, 'comment': msg,})
        print('\n Run ID : %s\n Test Case ID: %s\n Message : %s\n' % (run_id, case_id, msg))

if __name__ == "__main__":
    unittest.main()