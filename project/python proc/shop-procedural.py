import os
import csv

# Change the working directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

def create_and_stock_shop():
    """
    Creates a shop dictionary and populates it with data from a stock.csv file.
    
    Returns:
    - shop (dict): A dictionary representing the shop, containing the following keys:
        - cash (float): The amount of cash available in the shop.
        - products (list): A list of dictionaries representing the products in the shop, with each dictionary containing the following keys:
            - name (str): The name of the product.
            - price (float): The price of the product.
            - quantity (int): The quantity of the product in stock.
    
    Raises:
    - FileNotFoundError: If the stock.csv file is not found.
    - ValueError: If there is invalid data within the stock.csv file.
    - Exception: If an unexpected error occurs.
    """
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

def process_customer_order_interactively(shop):
    """
    Process a customer order interactively.

    This function prompts the user to enter their name, cash amount, and the products they want to purchase.
    It checks if the customer is a new or existing customer and displays a welcome message accordingly.
    The function continues to prompt the user for product names and quantities until the user enters 'quit'.
    It validates the product name and quantity, checks if there is sufficient stock, and updates the shop's inventory.
    Finally, it writes the customer's order details to a customer.csv file.

    Parameters:
    - shop (dict): The shop's information including products and cash amount.

    Returns:
    - customer (dict): The customer's information including name, cash amount, and products purchased.
    """
    customer = {}
    customer["name"] = input("Enter your name: ")
    customer["cash"] = float(input("Enter your cash amount: "))
    customer["products"] = []

    existing_names = set()

    # Check existing names in customer.csv
    try:
        with open("./project/customer.csv", mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                existing_names.add(row[0])
    except FileNotFoundError:
        print("Customer file not found. Proceeding with a new customer.")

    # Check if the name already exists
    if customer["name"] in existing_names:
        print(f"Welcome back, {customer['name']}!")
    else:
        print(f"New customer, {customer['name']}! We are excited to have you.")

    while True:
        product_name = input("Enter the product name (or 'quit' to finish): ")
        if product_name.lower() == 'quit':
            total_cost = sum(product["price"] * product["quantity"] for product in customer["products"])
            print("Order Summary:")
            for product in customer["products"]:
                print(f"Product: {product['name']}, Quantity: {product['quantity']}")
            print(f"Total Cost: {total_cost}")
            confirmation = input("Is this order summary correct? (yes/no): ")
            if confirmation.lower() == 'yes':
                print("Thank you for shopping with us!")
                break
            elif confirmation.lower() == 'no':
                print("Order canceled.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        product_quantity = float(input("Enter the quantity: "))

        found = False
        for shop_product in shop["products"]:
            if shop_product["name"] == product_name:
                found = True
                if float(shop_product["quantity"]) < product_quantity:
                    print(f"Error: Insufficient stock for {product_name}. There are only {shop_product['quantity']} left. Adjust your expectations, or come back later.")
                    break
                else:
                    shop_product["quantity"] = str(float(shop_product["quantity"]) - product_quantity)  # Update to string
                    customer["products"].append({"name": product_name, "quantity": product_quantity})
                    print(f"Order placed for {product_quantity} units of {product_name}.")
                    # update stock.csv
                    try:
                        with open("./project/stock.csv", mode='w', newline='') as stock_file:
                            stock_writer = csv.writer(stock_file)
                            stock_writer.writerow(["Cash"])  # Writing the header
                            stock_writer.writerow([shop["cash"]])  # Writing the shop's cash
                            for product in shop["products"]:
                                stock_writer.writerow([product["name"], product["price"], product["quantity"]])
                    except Exception as e:
                        print(f"An error occurred while writing to stock.csv: {e}")
                    break
        if not found:
            print(f"Error: Product '{product_name}' not found in the shop's inventory.")
    # Write customer data to customer.csv
    try:
        with open("./project/customer.csv", mode='a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            if customer["name"] not in existing_names:
                csv_file.write("\n")  # Add a newline if it's a new customer
            for product in customer["products"]:
                csv_writer.writerow([customer["name"], customer["cash"], product["name"], product["quantity"]])
    except Exception as e:
        print(f"An error occurred while writing to customer.csv: {e}")

    return customer

#def read_customer():
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
print_shop(shop)
customer = process_customer_order_interactively(shop)