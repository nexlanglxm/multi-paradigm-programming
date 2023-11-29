import os
import csv
# change the working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))



class Product: 
    def __init__(self, name, price, quantity): 
        self.name = name 
        self.price = price 
        self.quantity = quantity

    def __str__(self): 
       return f'NAME: {self.name}, PRICE: {self.price}, QUANTITY: {self.quantity}'
    
class Shop: 
    def __init__(self, cash, products): 
        self.cash = cash 
        self.products = products
        
    def add_product(self, product): 
        self.products.append(product)
        
    def __str__(self): 
        result = f'INITIAL CASH: {self.cash}\n' 
        for product in self.products: 
            result += str(product) + '\n' 
        return result
    
class Customer: 
    def __init__(self, name, cash, products): 
        self.name = name 
        self.cash = cash 
        self.products = products

    def add_product(self, product): 
        self.products.append(product)

    def __str__(self): 
        result = f'NAME: {self.name}, CASH: {self.cash}\n' 
        for product in self.products: 
            result += f'NAME: {product.name}, QUANTITY: {product.quantity}\n' 
        return result
    
def create_shop_and_stock(): 
    products = [] 
    with open("stock.csv") as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter=',') 
        cash = float(next(csv_reader)[0]) 
        for row in csv_reader: 
            product = Product(row[0], float(row[1]), int(row[2])) 
            products.append(product) 
        return Shop(cash, products)

def read_customer(file_path): 
    products = [] 
    with open(file_path) as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter=',') 
        name, cash = next(csv_reader) 
        for row in csv_reader: 
            product = Product(row[0], float(row[1]), 0) # Initialize quantity to 0 for customer 
            products.append(product) 
        return Customer(name, float(cash), products)
# Create the shop and customer
shop = create_shop_and_stock()
customer = read_customer("customer.csv")
# Print the shop and customer details
print(shop)
print(customer)