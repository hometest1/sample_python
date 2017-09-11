import unittest
from app import App

class TestSuite1(unittest.TestCase):

    def test(self):
        app = App()
        app.calculate()
        self.failIf(app.retrieve() != 62)
        
from app2 import App2

class TestSuite2(unittest.TestCase):
    def test(self):
        app2 = App2()
        app2.calculate()
        self.failIf(app2.retrieve() != 63)
        
#from app3 import App3

#class TestSuite3(unittest.TestCase):
  #  def test(self):
  #      app3 = App3()
  #      app3.calculate()
  #      self.failIf(app3.retrieve() != 64)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
