from xunit import TestCase

class WasRun(TestCase):
    def __init__(self,name):
        TestCase.__init__(self,name)
        self.wasRun = None

    def setUp(self):
        self.wasSetUp = True

    def testMethod(self):
        self.wasRun = True

class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetUp)

    def testRunning(self):
        assert(not self.test.wasRun)
        self.test.run()
        assert(self.test.wasRun)

TestCaseTest("testRunning").run()
