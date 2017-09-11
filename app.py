class App():
    def __init__(self):
        self.var1 = 15

    def calculate(self):
        self.result1 = self.var1 * 4 + 2

    def retrieve1(self):
        return self.result1
    
    def __init__(self):
        self.var2 = 16

    def calculate(self):
        self.result2 = self.var2 * 4 + 2
    
    def retrieve2(self):
        return self.result2
    
    def __init__(self):
        self.var3 = 17

    def calculate(self):
        self.result3 = self.var3 * 4 + 2
    
    def retrieve1(self):
        return self.result3
    
if __name__ == "__main__":
    app = App()
    app.calculate()
    print(app.retrieve1)
    print(app.retrieve2)
    print(app.retrieve3)
