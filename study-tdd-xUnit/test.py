from xunit import TestCase

class WasRun(TestCase):
    def __init__(self,name):
        TestCase.__init__(self,name)

    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log = self.log + "testMethod "

    def tearDown(self):
        self.log = self.log + "tearDown "

class TestCaseTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)


TestCaseTest("testTemplateMethod").run()
