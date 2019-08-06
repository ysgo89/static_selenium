from Test_Suite.default_setting import *
import unittest
import time

# Test Case_id 정보
case_id = 18704

class C18704(unittest.TestCase):
    def test_C18704(self):
        # default_setting 수행
        p: default = default()
        p.setUp()

        # STATIC 접속 -> User에 39자 초과되도록 입력 후 회원가입 시도
        p.driver.get(address)
        p.driver.find_element_by_link_text("Create account").click()
        p.driver.find_element_by_id("username").send_keys("aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd")
        p.driver.find_element_by_id("email").send_keys("admin123@static.ioi1")
        p.driver.find_element_by_id("password").send_keys("12348567")
        p.driver.find_element_by_xpath("//button").click()
        time.sleep(1)

        valCheck = "Username is too long (maximum is 39 characters)."

        # TestRail 결과 입력
        try :
            # Validate 문구 확인
            self.assertEqual(valCheck, p.driver.find_element_by_xpath("//small[2]").text)
            self.assertFalse(p.driver.find_element_by_xpath("//button").is_enabled())
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