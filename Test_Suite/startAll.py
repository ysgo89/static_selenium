import unittest

def load_tests(loader, tests, pattern):

    suite = unittest.TestSuite()
    for all_test_suite in unittest.defaultTestLoader.discover('../Test_Suite', pattern='C*.py'):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    return suite

if __name__ == '__main__':
    unittest.main()