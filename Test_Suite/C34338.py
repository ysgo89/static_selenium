from Test_Suite.default_setting import *
import unittest
import time

# Test Case_id 정보
case_id = 30722

class C34338(unittest.TestCase):
    def test_C34338(self):
        # default_setting 수행
        p: default = default()
        p.setUp()

        # 모든 특수 문자를 담는 배열 객체 생성
        list = ["`","~","!","@","#","$","%","^","&","*","(",")","-","=","_","+","[","]","{","}",";","'",":",'"',",",".","?","<",">","/"]
        # 특수 문자 입력 후 validate 확인용 객체 생성
        valCheck = "Please include at least one alphabetic character."

        # STATIC 접속 후 정상적인 Email, Password 값 입력
        p.driver.get(addressLogin)
        p.driver.find_element_by_link_text("Create account").click()
        p.driver.find_element_by_id("email").send_keys("goyosebbb@sures.com")
        p.driver.find_element_by_id("password").send_keys("12345511")

        try :
            # list를 받아와서 첫 번째부터 하나씩 num으로 대입
            for num in list:
                p.driver.find_element_by_id("username").clear()
                p.driver.find_element_by_id("username").send_keys(num)
                time.sleep(1)
                p.driver.find_element_by_xpath("//button").click()
                self.assertEqual(valCheck, p.driver.find_element_by_xpath("//small[2]").text)
                self.assertFalse(p.driver.find_element_by_xpath("//button").is_enabled())
                time.sleep(1)
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