class Car:
    def __init__(self, make, model, mileage, price, color, max_load, trunk_size, owner, importer):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.price = price
        self.color = color
        self.max_load = max_load
        self.trunk_size  = trunk_size
        self.owner = owner
        self.importer = importer

    def set_make(self, make):
        self.make = make
    
    def set_model(self, model):
        self.model = model

    def set_mileage(self, mileage):
        self.mileage = mileage

    def set_price(self, price):
        self.price = price
    
    def set_color(self, color):
        self.color = color

    def set_max_load(self, load):
        self.max_load = load

    def set_trunk_size(self, trunk):
        self.trunk_size = trunk
    
    def set_owner(self, owner):
        self.owner = owner

    def set_importer(self, importer):
        self.importer = importer
    
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def get_mileage(self):
        return self.mileage
    
    def get_price(self):
        return self.price
    
    def get_color(self):
        return self.color
    
    def get_max_load(self):
        return self.max_load
    
    def get_trunk_size(self):
        return self.trunk_size
    
    def get_owner(self):
        return self.owner
    
    def get_importer(self):
        return self.importer
    
    def __str__(self):
        return f"{self.make}, {self.model}"