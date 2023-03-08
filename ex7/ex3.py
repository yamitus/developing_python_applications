class Bird():
    def __init__(self, name):
        self.name = name
        self.eggs = 0
        self.migratory = [0,0]
    
    def set_name(self, name):
        self.name = name

    def set_eggs(self, eggs):
        self.eggs = eggs

    def set_migratory(self, destination, month):
        result_dest = self.check_destination(destination)
        result_month = self.check_month(month)
        if result_dest and result_month:
            self.migratory[0] = destination
            self.migratory[1] = month
        else:
            print("Error within declaration!")

    def check_destination(self, destination):
        result = destination[0].isupper()
        if result:
            return True
        else:
            return False
        
    def check_month(self, month):
        if 0 < month < 13:
            return True
        else:
            return False
    
    def get_name(self):
        return self.name
    
    def get_eggs(self):
        return self.eggs
    
    def get_migratory(self):
        return self.migratory
    
def main():
    p = Bird("Västäräkki")
    p.set_migratory("Suomi", 12)

main()