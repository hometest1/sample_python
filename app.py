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
        self.result = self.var2 * 4 + 1

    def retrieve(self):
        return self.result
    
if __name__ == "__main__":
    app = App()
    app.calculate()
    print(app.retrieve)
    
    app = App2()
    app.calculate()
    print(app.retrieve)
