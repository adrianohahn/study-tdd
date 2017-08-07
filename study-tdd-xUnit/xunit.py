class TestCase:
    def __init__(self,name):
        self.name = name

class WasRun(TestCase):
    def __init__(self,name):
        TestCase.__init__(self,name)
        self.wasRun = None
    pass

    def run(self):
        method = getattr(self,self.name)
        method()
    def testMethod(self):
        self.wasRun = 1
