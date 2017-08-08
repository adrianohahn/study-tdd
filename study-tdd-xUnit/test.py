from xunit import TestCase

class WasRun(TestCase):
    def __init__(self,name):
        TestCase.__init__(self,name)
        self.wasRun = None

    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.wasRun = True
        self.log = self.log + "testMethod "

class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert("setUp testMethod " == self.test.log)


TestCaseTest("testRunning").run()
