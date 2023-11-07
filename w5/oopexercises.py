class Person:
    def __init__(self, name, age, addresses=None):
        self.name = name
        self.age = age
        #modify this to be a list and add if statement to deal with null values
        if addresses is None: 
            addresses = []
        self.addresses = addresses

    def __repr__(self):
        addresses_str = "\n".join([str(address) for address in self.addresses])
                 #new line added to display all addresses associated with the Person class
        return f'Person("{self.name}", {self.age})\nADDRESSES:\n{addresses_str}' #changed ADDRESS to ADDRESSES
    
    def add_address(self, address):
        self.addresses.append(address)

class Student(Person):
    def __init__(self, name, age, addresses, college_course):
        Person.__init__(self, name, age, addresses)
        self.college_course = college_course
    def __repr__(self):
        return f'Student("{self.name}", {self.age}, {self.college_course})'


class Address:
    def __init__(self, house_number, street, town, county, eircode, country="Ireland"):
        self.house_number = house_number
        self.street = street
        self.town = town
        self.county = county
        self.eircode = eircode
        self.country = country

    def __repr__(self):
        string = "\n"
        string += f'{self.house_number} {self.street},\n{self.town},\n{self.county},\n{self.eircode},\n{self.country}'
        return string
        
address1 = Address("94", "Frenchcourt", "Orandale", "Galway", "H91K7P1")
address2 = Address("123", "Main Street", "Renmore", "Clare", "H85QPR7") #new address
p1 = Person("John", 36, [address1, address2])
p1 = Student("John", 36, address1, "Data")
print(p1)