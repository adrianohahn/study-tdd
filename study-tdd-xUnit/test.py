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
        pass

    def tearDown(self):
        pass

    def testTemplateMethod(self):
        result = TestResult()
        test = WasRun("testMethod")
        test.run(result)
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        result = TestResult()
        test = WasRun("testMethod")
        test.run(result)
        assert("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        result = TestResult()
        test = WasRun("testBrokenMethod")
        test.run(result)
        assert("1 run, 1 failed" == result.summary())

    def testFailedSetUp(self):
        result = TestResult()
        test = WasRunFailedSetup("testMethod")
        test.run(result)
        assert("1 run, 1 failed" ==  result.summary())

    def testSuite(self):
        result = TestResult()
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(result)
        assert("2 run, 1 failed" == result.summary())


suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedSetUp"))
suite.add(TestCaseTest("testSuite"))
result = TestResult()
suite.run(result)
print result.summary()
