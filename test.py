import unittest
from app import App

class TestSuite(unittest.TestCase):

    def test(self):
        app = App()
        app.calculate()
        self.failIf(app.retrieve() != 62)
        app2 = App2()
        app2.calculate()
        self.failIf(app2.retrieve() != 66)
        app3 = App3()
        app3.calculate()
        self.failIf(app3.retrieve() != 70)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
