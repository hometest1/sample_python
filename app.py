class App():
    def __init__(self):
        self.var1 = 15

    def calculate(self):
        self.result = self.var1 * 4 + 2

    def retrieve(self):
        return self.result

class App2():
    def __init__(self):
        self.var2 = 15

    def calculate(self):
        self.result = self.var2 * 4 
    
    def retrieve(self):
        return self.result

class App3():
    def __init__(self):
        self.var3 = 15

    def calculate(self):
        self.result = self.var3 * 5
    
    def retrieve(self):
        return self.result
    
if __name__ == "__main__":
    app = App()
    app.calculate()
    print(app.retrieve)
    app2 = App2()
    app2.calculate()
    print(app2.retrieve)
    app3 = App3()
    app3.calculate()
    print(app3.retrieve)
