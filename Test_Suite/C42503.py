import default_setting
import unittest
import time

# Test Case_id 정보
case_id = 42503

class C9008(unittest.TestCase):
    def test_C9008(self):
        # default_setting 수행
        setglob = default_setting
        p = default_setting.default()
        p.setUp()

        # 비밀번호 입력 후 validate 확인용 객체 생성
        valCheck = "Please include at least one alphabetic character."

        try:
            # STATIC 접속 후 정상적인 Username과 Email 값 입력
            p.driver.get(setglob.addressLogin)
            p.driver.find_element_by_link_text("Create account").click()
            p.driver.find_element_by_id("password").send_keys("1234567")
            p.driver.find_element_by_id("email").send_keys("goyosebb@sure.com")


            # 숫자 리스트를 자동으로 만들어 주는 range 함수 생성
            for num in range(0, 21):
                p.driver.find_element_by_id("username").clear()
                p.driver.find_element_by_id("username").send_keys(num)
                time.sleep(1)
                p.driver.find_element_by_xpath("//button").click()
                self.assertEqual(valCheck, p.driver.find_element_by_xpath("//small[2]").text)
                self.assertFalse(p.driver.find_element_by_xpath("//button").is_enabled())
                time.sleep(1)
                # 0부터 1씩 증가
                num = num + 1
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