#https://www.youtube.com/watch?v=W40mpZP9xQQ&ab_channel=ContinuousDelivery

import unittest

class Calculator:

    def __init__(self) -> None:
        self.__list = list()

    def percentage(self, percentage:float, number:int):
        return percentage * number

    def add_to_list(self, number:int):
        self.__list.append(number)

    def sum_list(self)->int:
        return sum(self.__list)


class PercentageTestCase(unittest.TestCase):

    def test_should_return_percentage(self):
        self.assertEqual(10, Calculator().percentage(10,100))

    def test_mistake_repeated_test_with_different_inputs(self):
        '''
            "The time for testing for different input is when either the new test demands 
            new behavior - so changing our implementation - or when we are not quite sure of the result, for some reason.
            -- Dave Farley
        '''
        self.assertEqual(5, Calculator().percentage(5,100))


    def test_mistake_duplicate_logic(self):
        '''"Your test is simply saying "the code I wrote is the code I wrote
            Make your assertion definitive and distinct from the code you're testing."
            -- Dave Farley
        '''
        self.assertEqual(5*100, Calculator().percentage(5,100))
    
    def test_mistake_iterate_through_test(self):
        sut = Calculator()

        #"TTD expert John Jagger says that cyclomathic complex of a test should be 1."
        for i in range(5):
            sut.add_to_list(i)
        self.assertEqual(10, sut.sum_list())


    

'''
Stub vs Fake vs Spies 

Stub is done, it has fixes returns and returns the same value every time
Fake is a little smarter, you can change its return

'''
class AccountService:

    def __init__(self, registration_function) -> None:
        self.__registration_function = registration_function

    def register(self, name:str):
        result = self.__registration_function(name)
        #logic
        return result

'''
    STUB
    
    Definition:
    "Stub - a dumb piec of software that simply replies the same way every time.
    -- Dave Farley

    Problems:
    They are pretty simple and don't usually cause too much problem.
    Except people sometimes don't think of using them when they should.

'''
def _stub_accept_registration(name):
    return True
    
def _stub_reject_registration(name):
    return False

class RegistrationTestCase(unittest.TestCase):

    def test_should_accept_registration(self):
        sut = AccountService(_stub_accept_registration)
        self.assertTrue(sut.register("name"))
    
    def test_should_reject_registration(self):
        sut = AccountService(_stub_reject_registration)
        self.assertFalse(sut.register("name"))


''' 
    FAKE

    Definition:
    "A stub is done, it will return the same value every time   
    A Fake is a little smarter, it has some behavior coded into."
    -- Dave Farley

    Problem:
    Peolple try to make fakes horribly complex.
    Specially when they are trying some simulation and imagine simulators nearly complex as the original system.
'''
def _fake_registration_function(name):
    return name == "Bruno"


class RegistrationTestCase(unittest.TestCase):

    def test_should_accept_registration(self):
        sut = AccountService(_fake_registration_function)
        self.assertTrue(sut.register("Bruno"))
    
    def test_should_reject_registration(self):
        sut = AccountService(_fake_registration_function)
        self.assertFalse(sut.register("other_name"))


'''
    SPY / Mock
    Definition:
    " A way to figure out what happened. We can use some code to record what happens while it's happening
    and then afterwards it allows us to query it and make assertions on whatever it is that we find."

    Problems:
    - "People end up writing up test using mocks that are so complex that there are actually no real code
    being tested, it's all mocks. If you find your selff ever returning a mock from a mock, I recomend that you
    stop and think about your design for a moment."
    - "If you find yourself writing code to simulate some behavior in a mock -  and I know library mocks let you do 
    this - but should? should you really?"
    - "If you find yourself validating that your code calls some dependency 17x, with one set of parameters and three more with
    another, then you have a problem - and it's not the mock's fault. 
'''
class RegistrationTestCase(unittest.TestCase):

    '''
        In this example we are interested in whether the core was made correctly or not.
    '''
    def test_should_accept_registration(self):
        sut = AccountService(self._spy_registration_function)
        self.assertTrue(sut.register("Bruno"))
        self.assertEqual("Bruno", self.name)
    
    def _spy_registration_function(self, name):
        self.name = name
        return True