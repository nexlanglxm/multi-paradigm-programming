import os
import csv

# Change the working directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

def create_and_stock_shop():
    shop = {}
    try:
        with open("./project/stock.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            shop["cash"] = float(first_row[0])
            shop["products"] = []
            for row in csv_reader:
                if len(row) >= 3:  # check if the row has at least 3 columns
                    product = {}
                    product["name"] = row[0].strip()  # Remove whitespace
                    product["price"] = float(row[1])
                    product["quantity"] = int(row[2])
                    shop["products"].append(product)
                else:
                    print(f"Issue with row: {row}. Skipping...")
    except FileNotFoundError:
        print("File 'stock.csv' not found. Please check the file path.")
    except ValueError as ve:
        print(f"Error: Invalid data within stock.csv - {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return shop

def process_customer_orders(customer, shop):
    total_cost = 0
    for product in customer["products"]:
        product_name = product["name"]
        product_quantity = float(product["quantity"])  # Change int() to float()
        found = False

        for shop_product in shop["products"]:
            if shop_product["name"] == product_name:
                found = True
                if float(shop_product["quantity"]) < product_quantity:
                    print(f"Error: Insufficient stock for {product_name}. There are only {shop_product['quantity']} left. Adjust your expectations, or come back later.")
                    break
                else:
                    shop_product["quantity"] = str(float(shop_product["quantity"]) - product_quantity)  # Update to string
                    total_cost += product_quantity * shop_product["price"]  # Add the cost of each product to the total cost
                    print(f"Order placed for {product_quantity} units of {product_name}.")
                    break
        
        if not found:
            print(f"Error: Product '{product_name}' not found in the shop's inventory.")

    shop["cash"] += total_cost  # Increase the shop's cash by the total cost from the purchase
    customer["cash"] -= total_cost  # Deduct the total cost from the customer's cash

    print(f"Customer's total cost: {total_cost}")
    print(f"Updated Shop's cash: {shop['cash']}")
    print(f"Updated Customer's cash: {customer['cash']}")
    print("Updated shop inventory: ")
    for product in shop["products"]:
        print(f'NAME: {product["name"]}, PRICE: {product["price"]}, QUANTITY: {product["quantity"]}')
        
def read_customer():
    customers = []
    try:
        with open("./project/customer.csv") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                customer = {}
                customer["name"] = row[0]
                customer["cash"] = float(row[1])
                customer["products"] = []
                
                # Process products and quantities for each customer
                for i in range(2, len(row), 2):
                    product = {}
                    product["name"] = row[i].strip() # Remove whitespace
                    product["quantity"] = int(row[i + 1])
                    customer["products"].append(product)

                customers.append(customer)  # Add the processed customer to the list

    except FileNotFoundError:
        print("File 'customer.csv' not found. Please check the file path.")
    except ValueError as ve:
        print(f"Error: Invalid data within cutomer.csv - {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return customers # Return the list of customers


def print_product(product):
    print(f'NAME: {product["name"]}, PRICE: {product["price"]}, QUANTITY: {product["quantity"]}')

def print_customer(customer):
    print(f'NAME: {customer["name"]}, CASH: {customer["cash"]}')
    for product in customer["products"]:
        print(f'NAME: {product["name"]}, QUANTITY: {product["quantity"]}')

def print_shop(shop):
    print(f'INITIAL CASH: {shop["cash"]}')
    print("Updated shop inventory: ")
    for product in shop["products"]:
        print(f'NAME: {product["name"]}, PRICE: {product["price"]}, QUANTITY: {product["quantity"]}')

shop = create_and_stock_shop()
print(shop)

customers = read_customer()
for customer in customers:
    process_customer_orders(customer, shop)