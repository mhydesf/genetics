from unittest import TestLoader, TestSuite, TextTestRunner

def all_tests_suite():
    test_loader = TestLoader()
    test_suite = TestSuite()
    test_suite.addTests(test_loader.discover('.', pattern='test_*.py'))

    return test_suite

if __name__ == '__main__':
    runner = TextTestRunner()
    runner.run(all_tests_suite())
