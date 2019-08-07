from Test_Suite.default_setting import *
import unittest
import time

# Test Case_id 정보
case_id = 18949

class C18949(unittest.TestCase):
    def test_C18949(self):
        # default_setting 수행
        p: default = default()
        p.setUp()
        p.test_static_access()

        # 확인용 객체 생성
        valCheck = "Key is required."
        title = "Create Project"

        # 프로젝트 생성 버튼 클릭 후 Name만 입력
        p.driver.find_element_by_xpath("//div[2]/button/span").click()
        p.driver.find_element_by_xpath("//mat-form-field/div/div/div/input").send_keys(pName)
        p.driver.find_element_by_xpath('//button[contains(text(), "Submit")]').click()
        time.sleep(3)

        try :
            self.assertEqual(valCheck, p.driver.find_element_by_id("mat-error-1").text)
            self.assertEqual(title, p.driver.find_element_by_css_selector("span.title").text)
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