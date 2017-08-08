from xunit import *

class WasRun(TestCase):
    def __init__(self,name):
        TestCase.__init__(self,name)
        self.wasRun = None
    pass

    def testMethod(self):
        self.wasRun = 1

class TestCaseTest(TestCase):

    def testSetUp(self):
        test = WasRun("testMethod")
        test.run()
        assert test.wasSetUp

    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

TestCaseTest("testRunning").run()
