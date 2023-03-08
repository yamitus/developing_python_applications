class Complex():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.i = "i"
        self.the_number = str(self.a) + "+" + str(self.b) + "*" + self.i

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b
    
    def get_a(self):
        return self.a

    def get_b(self):
        return self.b
    
    def __str__(self):
        return self.the_number
    
def main():
    a = Complex(3, 6)
    print(a)

main()