import unittest
from app import App

class TestSuite(unittest.TestCase):

    def test(self):
        app = App()
        app.calculate()
        self.failIf(app.retrieve1() != 62)
        self.failIf(app.retrieve1() != 66)
        self.failIf(app.retrieve1() != 70)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
