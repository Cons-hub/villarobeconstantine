class Person:
    def __init__(self, person_id, name, age, address, contact_number, email):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.address = address
        self.contact_number = contact_number
        self.email = email

    def display_info(self):
        print(f"ID       : {self.person_id}")
        print(f"Name     : {self.name}")
        print(f"Age      : {self.age}")
        print(f"Address  : {self.address}")
        print(f"Contact  : {self.contact_number}")
        print(f"Email    : {self.email}")