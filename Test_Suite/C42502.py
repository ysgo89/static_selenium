from Test_Suite.default_setting import *
import unittest
import time

# Test Case_id 정보
case_id = 42502

class C18710(unittest.TestCase):
    def test_C18710(self):
        # default_setting 수행
        p: default = default()
        p.setUp()
        p.test_static_access()
        time.sleep(1)

        # STATIC 비유효한 URL 접속
        p.driver.get(address+'/project/fds824728142/overview')

        # 404 페이지 문구 확인용 객체 생성
        check1 = "404"
        check2 = "The page you're looking for could not be found."
        check3 = "Make sure the address is correct and that the page hasn't moved."
        check4 = "Please contact your STATIC administrator if you think this is a mistake."
        check5 = "Go home"

        try :
            # 404 페이지 출력 문구 확인
            self.assertEqual(check1, p.driver.find_element_by_css_selector("span.ml-5").text)
            self.assertEqual(check2, p.driver.find_element_by_xpath("//h3").text)
            self.assertEqual(check3, p.driver.find_element_by_css_selector("div.wrapper.align-items-center > span").text)
            self.assertEqual(check4, p.driver.find_element_by_xpath("//span[2]").text)
            self.assertEqual(check5, p.driver.find_element_by_xpath("//a[contains(text(),'Go home')]").text)
            status_id = 1
        except :
            status_id = 5

        # Test Rail 결과 입력
        # if status_id == 1:
        #     print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (run_id, case_id, passMsg))
        #     client.send_post(
        #         'add_result_for_case/%s/%s' % (run_id, case_id),
        #         {'status_id': status_id, 'comment': passMsg, })
        #
        # elif status_id == 5:
        #     print('\nRun ID : %s\nTest Case ID: %s\nMessage : %s\n' % (run_id, case_id, failMsg))
        #     client.send_post(
        #         'add_result_for_case/%s/%s' % (run_id, case_id),
        #         {'status_id': status_id, 'comment': failMsg, })

if __name__ == "__main__":
    unittest.main()