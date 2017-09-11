class App():
    def __init__(self):
        self.var1 = 15

    def calculate(self):
        self.result = self.var1 * 4 + 2

    def retrieve(self):
        return self.result

class App2():
    def __init__(self2):
        self.var2 = 16

    def calculate(self):
        self2.result = self2.var2 * 4 + 2
    
    def retrieve(self2):
        return self2.result

class App3():
    def __init__(self):
        self.var3 = 17

    def calculate(self):
        self.result = self.var3 * 4 + 2
    
    def retrieve(self):
        return self.result
    
if __name__ == "__main__":
    app = App()
    app.calculate()
    print(app.retrieve)
    app2 = App2()
    app.calculate()
    print(app.retrieve)
    app3 = App3()
    app.calculate()
    print(app.retrieve)
