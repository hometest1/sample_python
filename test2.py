import unittest
from app2 import App2

class TestSuite(unittest.TestCase):

    def test(self):
        app2 = App2()
        app2.calculate()
        self.failIf(app2.retrieve() != 61)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
