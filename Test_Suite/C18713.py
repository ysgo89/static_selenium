from Test_Suite.default_setting import *
import unittest

# Test Case_id 정보
case_id = 18713

class C18713(unittest.TestCase):
    def test_C18713(self):
        # default_setting 수행
        p: default = default()
        p.setUp()

        # 회원가입 페이지 이동 후 로그인 페이지로 이동
        p.driver.get(addressLogin)
        p.driver.find_element_by_link_text("Create account").click()
        p.driver.find_element_by_link_text("Sign in instead").click()

        # 회원가입 팝업창에서 로그인 페이지로 돌아와 로그인 페이지가 맞는지 확인하기 위한 객체 생성
        valCheck = "Sign in"

        try :
            # validate 문구 비교
            self.assertEqual(valCheck, p.driver.find_element_by_css_selector("span.headline").text)
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