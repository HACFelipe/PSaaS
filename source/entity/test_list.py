from typing import List, Type

from entity.test import Test

class TestList():
    """Model of TestList"""

    def __init__(self, tests: List[Test] = []):
        self.__tests = tests

    
    def add_test(self, test : Test):
        test.id = self.generate_id()
        self.__tests.append(test)


    def remove_test(self, test : Test):
        self.__tests.remove(test)


    def generate_id(self) -> str:
        prefix = "TC"
        count = 0
        for test in self.__tests:
            if prefix in test.id:
                count += 1
        return "%s%d" % (prefix, count)


    def print_tests(self):
        if self.__tests:
            Test.print_test_headers()
            for test in self.__tests:
                test.print_test()
        else:
            print("No Test Components defined!")


    def all_tests_passed(self):
        for test in self.__tests:
            if not test.success:
                return False
        return True


    @property
    def items(self):
        return self.__tests