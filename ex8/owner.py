class Owner():
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_phone_number(self):
        return self.phone_number
    
    def __str__(self):
        return f"{self.name}"