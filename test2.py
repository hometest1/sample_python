import unittest
from app import App2

class TestSuite(unittest.TestCase):

    def test(self):
        app = App2()
        app.calculate()
        self.failIf(app.retrieve() != 61)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
