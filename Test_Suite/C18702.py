from Test_Suite.default_setting import *
import unittest
import time

# TestRail run_id, Test Case_id, Message 정보
run_id = 240
case_id = 30722
passMsg = 'Test Run Success !!'
failMsg = 'Test Run Fail !!'

class C18702(unittest.TestCase):
    def test_C18702(self):
        # default_setting 수행
        p: default = default()
        p.setUp()
        p.test_static_access()
        time.sleep(1)
        # STATIC 비유효한 URL 접속
        p.driver.get('http://211.116.222.204/project/155ddddd5555555/defect-list/1000000ddddd00000000?revisionSeq=2')

        # 404 페이지 확인
        a=p.driver.find_element_by_css_selector("span.ml-5").text
        b=p.driver.find_element_by_xpath("//h3").text
        c=p.driver.find_element_by_css_selector("div.wrapper.align-items-center > span").text
        d=p.driver.find_element_by_xpath("//span[2]").text
        e=p.driver.find_element_by_xpath("//a[contains(text(),'Go home')]").text

        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        # TestRail 결과 입력
        try :
            # 시스템 기본 계정 로그인 시 Projects 페이지가 출력하는지 확인
            self.assertEqual("404", p.driver.find_element_by_css_selector("span.ml-5").text)
            # self.assertEqual("Projects", p.driver.find_element_by_xpath("//h3").text)
            # self.assertEqual("Projects", p.driver.find_element_by_css_selector("div.wrapper.align-items-center > span").text)
            # self.assertEqual("Projects", p.driver.find_element_by_xpath("//span[2]").text)
            # self.assertEqual("Projects", p.driver.find_element_by_xpath("//a[contains(text(),'Go home')]").text)

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