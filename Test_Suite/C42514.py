from default_setting import *
import unittest

# Test Case_id 정보
case_id = 42514

class C18708(unittest.TestCase):
    def test_C18708(self):
        # default_setting 수행
        p: default = default()
        p.setUp()

        # 유효하지 않은 메일 양식으로 회원가입 시도
        p.driver.get(addressLogin)
        p.driver.find_element_by_link_text("Create account").click()
        p.driver.find_element_by_id("username").send_keys("goyoseb")
        p.driver.find_element_by_id("email").send_keys("aaaaa@a.c")
        p.driver.find_element_by_id("password").send_keys("123456789")
        p.driver.find_element_by_xpath("//button").click()
        time.sleep(1)

        # 유효하지 않은 메일 양식을 사용 시 출력되는 문구의 객체 생성
        valCheck = "×\nAn account for that name/e-mail/password invalid."

        try :
            # validate 문구 비교
            self.assertEqual(valCheck, p.driver.find_element_by_xpath("//ngb-alert").text)
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