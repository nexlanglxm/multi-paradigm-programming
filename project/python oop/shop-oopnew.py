import os
import csv

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"NAME: {self.name}, PRICE: {self.price}, QUANTITY: {self.quantity}"

class Shop:
    def __init__(self, stock_file_path="./project/stock.csv", customer_file_path="./project/customer.csv"):
        self.stock = self.read_stock(stock_file_path)
        self.customer_file_path = customer_file_path

    def read_stock(self, stock_file_path):
        stock = {}
        try:
            with open(stock_file_path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                stock["cash"] = float(next(csv_reader)[0])
                stock["products"] = []
                for row in csv_reader:
                    stock["products"].append([
                        "name": row[0].strip(),
                        "price": float(row[1]),
                        "quantity": int(row[2])
                    ])
        except FileNotFoundError:
            print(f"File '{stock_file_path}' not found. Please check the file path.")
        except ValueError as ve:
            print(f"Error: Invalid data within stock.csv - {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return stock

    def process_customer_order_interactively(self):
        existing_names = set()
        try:
            with open(self.customer_file_path, mode='r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    existing_names.add(row[0])
        except FileNotFoundError:
            print("Customer file not found.")

        customer = {}
        customer["name"] = input("Enter your name: ")
        customer["cash"] = float(input("Enter your cash amount: "))
        customer["products"] = []

        if customer["name"] in existing_names:
            print(f"Welcome back, {customer['name']}!")
        else:
            print(f"New customer, {customer['name']}! We are excited to have you.")

        while True:
            product_name = input("Enter the product name (or 'quit' to finish): ")
            if product_name.lower() == 'quit':
                print("Thank you for shopping with us!")
                break
            
            product_quantity = float(input("Enter the quantity: "))

            found = False
            for product in self.stock["products"]:
                if product.name == product_name:
                    found = True
                    if product.quantity < product_quantity:
                        print(f"Error: Insufficient stock for {product_name}. There are only {product.quantity} left. Adjust your expectations, or come back later.")
                        break
                    else:
                        product.quantity -= product_quantity
                        customer["products"].append({"name": product_name, "quantity": product_quantity})
                        print(f"Order placed for {product_quantity} units of {product_name}.")
                        break
            
            if not found:
                print(f"Error: Product '{product_name}' not found in the shop's inventory.")

        # Write customer data to customer.csv
        try:
            with open(self.customer_file_path, mode='a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                if customer["name"] not in existing_names:
                    csv_file.write("\n")  # Add a newline if it's a new customer
                for product in customer["products"]:
                    csv_writer.writerow([customer["name"], customer["cash"], product["name"], product["quantity"]])
        except Exception as e:
            print(f"An error occurred while writing to {self.customer_file_path}: {e}")

# Usage:
shop = Shop()
shop.process_customer_order_interactively()
