import os
import csv

# Change the working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def create_and_stock_shop():
    shop = {}
    try:
        with open("stock.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            shop["cash"] = float(first_row[0])
            shop["products"] = []
            for row in csv_reader:
                if len(row) >= 3: #check if the row has at least 3 columns
                    product = {}
                    product["name"] = row[0]
                    product["price"] = row[1]
                    product["quantity"] = row[2]
                    shop["products"].append(product)
                else:
                    print(f"Issue with row: {row}. Skipping...")
    except FileNotFoundError:
        print("File 'stock.csv' not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return shop


def read_customer():
    customer = {}
    try:
        with open("customer.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            customer["name"] = first_row[0]
            customer["cash"] = float(first_row[1])
            customer["products"] = []
            for row in csv_reader:
                if len(row) >= 2:
                    product = {}
                    product["name"] = row[0]
                    product["quantity"] = row[1]
                    customer["products"].append(product)
                else:
                    print(f"Issue with row: {row}. Skipping...")
    except FileNotFoundError:
        print("File 'customer.csv' not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return customer


def print_product(product):
    print(f'NAME: {product["name"]}, PRICE: {product["price"]}, QUANTITY: {product["quantity"]}')


def print_customer(customer):
    print(f'NAME: {customer["name"]}, CASH: {customer["cash"]}')
    for product in customer["products"]:
        print(f'NAME: {product["name"]}, QUANTITY: {product["quantity"]}')


def print_shop(shop):
    print(f'INITIAL CASH: {shop["cash"]}')
    for product in shop["products"]:
        print_product(product)


shop = create_and_stock_shop()
print_shop(shop)

customer = read_customer()
print_customer(customer)
