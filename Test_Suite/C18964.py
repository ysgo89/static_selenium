from Test_Suite.default_setting import *
from testrail import *

# TestRail 접속 정보
client = APIClient('http://211.116.223.42/testrail')
client.user = 'goyoseb@suresofttech.com'
client.password = 'dudcks123!'

# TestRail run_id, Testcase_id, Message 정보
run_id = 240
case_id = 30722
msg = 'Test Auto Checking'

class C18964(unittest.TestCase):
    def test_C18964(self):
        p: default = default()
        p.setUp()
        p.test_static_access()



        # TestRail 결과 입력
        # try :
        #     assert "STATIC11" in driver.title
        #     status_id = 1
        # except :
        #     status_id = 5
        #
        # client.send_post(
        #     'add_result_for_case/%s/%s' % (run_id, case_id),
        #     {'status_id': status_id, 'comment': msg,})
        # print('\n Run ID : %s\n Test Case ID: %s\n Message : %s\n' % (run_id, case_id, msg))

if __name__ == "__main__":
    unittest.main()