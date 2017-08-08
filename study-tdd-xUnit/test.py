from xunit import *

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
        self.result = TestResult()

    def tearDown(self):
        pass

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def testFailedSetUp(self):
        test = WasRunFailedSetup("testMethod")
        test.run(self.result)
        assert("1 run, 1 failed" ==  self.result.summary())

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())

    def testFailedTest(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert("Failed:\n testBrokenMethod" == self.result.failedSummary())


suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedSetUp"))
suite.add(TestCaseTest("testSuite"))
suite.add(TestCaseTest("testFailedTest"))
result = TestResult()
suite.run(result)
print result.summary()
print result.failedSummary()
