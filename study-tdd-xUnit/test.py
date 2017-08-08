from xunit import TestCase

class WasRun(TestCase):
    def __init__(self,name):
        TestCase.__init__(self,name)

    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log = self.log + "testMethod "

    def testBrokenMethod(self):
        assert(1 == 0)

    def tearDown(self):
        self.log = self.log + "tearDown "

class WasRunFailedSetup(WasRun):

    def __init__(self,name):
        TestCase.__init__(self,name)

    def setUp(self):
        WasRun.setUp(self)
        assert(0)

class TestCaseTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())

    def testFailedSetUp(self):
        test = WasRunFailedSetup("testMethod")
        result = test.run()
        assert("1 run, 1 failed" ==  result.summary())


print("testTemplateMethod: " + TestCaseTest("testTemplateMethod").run().summary())
print("testResult: " + TestCaseTest("testResult").run().summary())
print("testFailedResult: " + TestCaseTest("testFailedResult").run().summary())
print("testFailedSetUp: " + TestCaseTest("testFailedSetUp").run().summary())
