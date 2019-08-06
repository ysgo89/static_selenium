from Test_Suite.default_setting import *
import unittest

# Test Case_id 정보
case_id = 18706

class C18706(unittest.TestCase):
    def test_C18706(self):
        # default_setting 수행
        p: default = default()
        p.setUp()

        # STATIC 시스템 기본 계정 로그인
        p.driver.get(addressLogin)
        p.driver.implicitly_wait(30)
        p.driver.find_element_by_id("email").send_keys("admin@static.io")
        p.driver.find_element_by_id("password").send_keys("!admin")
        p.driver.find_element_by_id("password").send_keys(Keys.RETURN)
        p.driver.implicitly_wait(30)

        try :
            # 시스템 기본 계정 로그인 시 Projects 페이지가 출력하는지 확인
            self.assertEqual("Projects", p.driver.find_element_by_css_selector("div.contents-title").text)
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