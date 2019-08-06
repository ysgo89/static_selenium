from Test_Suite.default_setting import *
import unittest
import time

# Test Case_id 정보
case_id = 18707

class C18707(unittest.TestCase):
    def test_C18707(self):
        # default_setting 수행
        p: default = default()
        p.setUp()
        p.test_static_access()
        time.sleep(1)
        # STATIC 비유효한 URL 접속
        p.driver.get('http://211.116.222.204/project/ZLfdsfdsdsfdsfdsfsZL4/defect-list/1')

        # Go home 버튼 클릭
        p.driver.find_element_by_xpath("//a[contains(text(),'Go home')]").click()
        time.sleep(1)

        # 프로젝트 생성 클릭
        p.driver.find_element_by_xpath("//div[2]/button/span").click()
        time.sleep(1)

        # 프로젝트 생성창 이름 객체
        cpCheck = "Create Project"
        # TestRail 결과 입력
        try :
            # 프로젝트 생성창 이름 비교 확인
            self.assertEqual(cpCheck, p.driver.find_element_by_css_selector("span.title").text)
            status_id = 1
        except :
            status_id = 5

        # Test Rail 결과 입력
        if status_id == 1:
            print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (run_id, case_id, passMsg))
            client.send_post(
                'add_result_for_case/%s/%s' % (run_id, case_id),
                {'status_id': status_id, 'comment': passMsg, })

        elif status_id == 5:
            print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (run_id, case_id, failMsg))
            client.send_post(
                'add_result_for_case/%s/%s' % (run_id, case_id),
                {'status_id': status_id, 'comment': failMsg, })

if __name__ == "__main__":
    unittest.main()