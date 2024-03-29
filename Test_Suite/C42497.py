import default_setting
import unittest

# Test Case_id 정보
case_id = 42497

class C18701(unittest.TestCase):
    def test_C18701(self):
        # default_setting 수행
        setglob = default_setting
        p = default_setting.default()
        p.setUp()

        try:
            # 비유효한 값으로 로그인
            p.driver.get(setglob.addressLogin)
            p.driver.implicitly_wait(30)
            p.driver.find_element_by_id("email").send_keys("admin@stati.ciopioiii")
            p.driver.find_element_by_id("password").send_keys("abcd12fddd")
            p.driver.find_element_by_id("password").send_keys(setglob.Keys.RETURN)
        
            # 팝업창 문구 체크
            popCheck = p.driver.find_element_by_xpath("//ngb-alert").text
            print(popCheck)

            # 인증 실패 시 출력되는 문구 비교
            self.assertEqual("×\nInvalid Credentials",popCheck)
            status_id = 1
        except :
            status_id = 5

         # Test Rail 결과 입력
        if status_id == 1:
            print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (setglob.run_id, case_id, setglob.passMsg))
            setglob.client.send_post(
                'add_result_for_case/%s/%s' % (setglob.run_id, case_id),
                {'status_id': status_id, 'comment': setglob.passMsg, })

        elif status_id == 5:
            print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (setglob.run_id, case_id, setglob.failMsg))
            setglob.client.send_post(
                'add_result_for_case/%s/%s' % (setglob.run_id, case_id),
                {'status_id': status_id, 'comment': setglob.failMsg, })

if __name__ == "__main__":
    unittest.main()