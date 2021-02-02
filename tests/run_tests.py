from unittest import TestLoader, TextTestRunner, TestSuite
from tests.test_questions_types import TestQuestionTypes

if __name__ == '__main__':
    questions_tests = TestLoader().loadTestsFromTestCase(TestQuestionTypes)

    suite = TestSuite([questions_tests])
    TextTestRunner().run(suite)
