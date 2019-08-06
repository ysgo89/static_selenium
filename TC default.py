from Test_Suite.default_setting import *
from testrail import *
import unittest
import time
import os

# TestRail run_id, Test Case_id, Message 정보
run_id = 240
case_id = 30722

class C18701(unittest.TestCase):
    def test_C18701(self):
        # default_setting 수행
        p: default = default()
        p.setUp()
        p.test_static_access()

        # # TestRail 결과 입력
        # try :
        #     # 시스템 기본 계정 로그인 시 Projects 페이지가 출력하는지 확인
        #     self.assertEqual("Projects", p.driver.find_element_by_css_selector("div.contents-title").text)
        #     status_id = 1
        # except :
        #     status_id = 5
        #
        # # # TestRail 결과 입력
        # if status_id == 1:
        #     print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (run_id, case_id, passMsg))
        #     client.send_post(
        #         'add_result_for_case/%s/%s' % (run_id, case_id),
        #         {'status_id': status_id, 'comment': passMsg, })
        #
        # elif status_id == 5:
        #     print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (run_id, case_id, failMsg))
        #     client.send_post(
        #         'add_result_for_case/%s/%s' % (run_id, case_id),
        #         {'status_id': status_id, 'comment': failMsg, })

if __name__ == "__main__":
    unittest.main()