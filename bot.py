from main import User

class Talaba(User):
    def __init__(self, id, name, age, address, group):
        self.address = address
        self.group = group
        super().__init__(id, name, age)

    def year_info(self):
        return 2024 - self.age

    def get_info(self, id,name, age, address, group):
        return f"""
ID: {id}
Name: {name}
Yoshi: {age}
Manzil: {address}
Gurux: {group}
"""


talaba = Talaba(1,'Odil', 22,'yngiyol',44)
print(talaba.year_info())
print(talaba.get_info(talaba.id, talaba.name, talaba.age,
                      talaba.address,talaba.group))
