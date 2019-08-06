from Test_Suite.default_setting import *
import unittest
import time

# Test Case_id 정보
case_id = 18692

class C18692(unittest.TestCase):
    def test_C18692(self):
        # default_setting 수행
        p: default = default()
        p.setUp()

        # STATIC 접속 -> Email 필드에 비유효한 값 입력 후 회원가입 시도
        p.driver.get(addressLogin)
        p.driver.find_element_by_link_text("Create account").click()
        p.driver.find_element_by_id("username").send_keys("goyosebgoyose")
        p.driver.find_element_by_id("email").send_keys("aaaa@a aaa@a.c")
        p.driver.find_element_by_id("password").send_keys("1234567")
        p.driver.find_element_by_xpath("//button").click()
        time.sleep(1)

        valCheck = "Email is invalid."

        try :
            # Validate 문구 확인
            self.assertEqual(valCheck, p.driver.find_element_by_xpath("//div[2]/small").text)
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