import os
import csv
# change the working directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Product:
# initialize the product with a name and a price
    def __init__(self, name, price=0):
        self.name = name
        self.price = price
# return the name & price of the product
    def __repr__(self):
        return f'NAME: {self.name} PRICE: {self.price}'

class ProductStock:
    
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
# return the name of the product
    def name(self):
        return self.product.name;
# return the unit price of the product
    def unit_price(self):
        return self.product.price;
# calculate the cost of the product       
    def cost(self):
        return self.unit_price() * self.quantity
        
    def __repr__(self):
        return f"{self.product} QUANTITY: {self.quantity}"
# initialize the customer with a shopping list
class Customer:

    def __init__(self, path):
        self.shopping_list = []
        try:
            with open(path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                first_row = next(csv_reader)
                self.name = first_row[0]
                self.budget = float(first_row[1])
                for row in csv_reader:
                    if len(row) >= 2:
                        name = row[0]
                        quantity = float(row[1])
                        p = Product(name)
                        ps = ProductStock(p, quantity)
                        self.shopping_list.append(ps)
                    else:
                        print(f"Issue with row: {row}. Skipping...")
        except FileNotFoundError:
            print(f"File {path} not found.")
        except Exception as e:
            print("An error occurred: {e}")
                
    def calculate_costs(self, price_list):
        for shop_item in price_list:
            for list_item in self.shopping_list:
                if (list_item.name() == shop_item.name()):
                    list_item.product.price = shop_item.unit_price()
    
    def order_cost(self):
        cost = 0
        
        for list_item in self.shopping_list:
            cost += list_item.cost()
        
        return cost
    
    def __repr__(self):
        
        str = f"{self.name} wants to buy"
        for item in self.shopping_list:
            cost = item.cost()
            str += f"\n{item}"
            if (cost == 0):
                str += f" {self.name} doesn't know how much that costs :("
            else:
                str += f" COST: {cost}"
                
        str += f"\nThe cost would be: {self.order_cost()}, he would have {self.budget - self.order_cost()} left"
        return str 
        
class Shop:
    
    def __init__(self, path):
        self.stock = []
        try: # try to open the file
            with open(path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                first_row = next(csv_reader)
                self.cash = float(first_row[0])
                for row in csv_reader:
                    if len(row) >= 3:
                        p = Product(row[0], float(row[1]))
                        ps = ProductStock(p, float(row[2]))
                        self.stock.append(ps)
                    else: # if the row is not valid
                        print(f"issue with row: {row}.")
        except FileNotFoundError: # catch the specific exception
            print(f"File {path} not found.")
        except Exception as e: # catch all other exceptions
            print("Something went wrong.")  
    
    def __repr__(self):
        str = ""
        str += f'Shop has {self.cash} in cash\n'
        for item in self.stock:
            str += f"{item}\n"
        return str

s = Shop("../project/stock.csv")
print(s)

c = Customer("../project/customer.csv")
c.calculate_costs(s.stock)
print(c)