class TestResult:

    def __init__(self):
        self.runCount = 0
        self.errorCount = 0
        self.testsFailed = 'Failed:'

    def testStarted(self):
        self.runCount = self.runCount + 1

    def testFailed(self, testName):
        self.errorCount = self.errorCount + 1
        self.testsFailed += ("\n %s" % testName)

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)

    def failedSummary(self):
        if self.testsFailed == 'Failed:':
            self.testsFailed += ' None'
        return self.testsFailed

class TestCase:
    def __init__(self,name):
        self.name = name

    def run(self, result):
        result.testStarted()
        try:
            self.setUp()
            method = getattr(self,self.name)
            method()
        except AssertionError:
            result.testFailed(self.name)
        finally:
            self.tearDown()
        return result

class TestSuite:

    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)
        return result
