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
case_id = 18706
msg = 'Test Run complete'

class C18706(unittest.TestCase):
    def test_C18706(self):
        # default_setting 수행
        p: default = default()
        p.setUp()

        # STATIC 시스템 기본 계정 로그인
        p.driver.get(address)
        p.driver.implicitly_wait(30)
        p.driver.find_element_by_id("email").send_keys("admin@static.io")
        p.driver.find_element_by_id("password").send_keys("!admin")
        p.driver.find_element_by_id("password").send_keys(Keys.RETURN)
        p.driver.implicitly_wait(30)

        # TestRail 결과 입력
        try :
            # 시스템 기본 계정 로그인 시 Projects 페이지가 출력하는지 확인
            self.assertEqual("Projects", p.driver.find_element_by_css_selector("div.contents-title").text)
            status_id = 1
        except :
            status_id = 5

        client.send_post(
            'add_result_for_case/%s/%s' % (run_id, case_id),
            {'status_id': status_id, 'comment': msg,})
        print('\n Run ID : %s\n Test Case ID: %s\n Message : %s\n' % (run_id, case_id, msg))

if __name__ == "__main__":
    unittest.main()