#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_PRODUCTS 50
#define MAX_CUSTOMERS 25

struct Product
{
    char name[50];
    double price;
};

struct ProductStock
{
    struct Product product;
    int quantity;
};

struct Shop
{
    double shopfloat;
    struct ProductStock stock[20];
    int index;
};

struct Customer
{
    char name[50];
    double budget;
    struct ProductStock shoppingList[MAX_PRODUCTS];
    int index;
};

// function to print product details
void printProduct(struct Product p)
{
    printf("--------------------\n");
    printf("PRODUCT NAME: %s\n PRODUCT PRICE: %.2f\n", p.name, p.price);
    printf("--------------------\n");
}

// function to print shop details
void printShop(struct Shop s)
{
    printf("Shop has %.2f in cash\n", s.shopfloat);
    for (int i = 0; i < s.index; i++)
    {
        printProduct(s.stock[i].product);
        printf("The shop has %d of the above\n", s.stock[i].quantity);
    }
}

/**
 * This function creates a shop and stocks it with products from a CSV file.
 *
 * @param shop Pointer to the Shop structure where the shop details will be stored.
 */
void createAndStockshop(struct Shop *shop)
{
    shop->shopfloat = 200.0;
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("../project/stock.csv", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, fp)) != -1)
    {
        char *n = strtok(line, ",");
        char *p = strtok(NULL, ",");
        char *q = strtok(NULL, ",");
        char *name = malloc(sizeof(char) * 50);
        strcpy(name, n);
        int quantity = atoi(q);
        double price = atof(p);
        struct Product product;
        strcpy(product.name, name);
        product.price = price;
        struct ProductStock stockItem = {product, quantity};
        shop->stock[shop->index++] = stockItem;
    }

    fclose(fp);
    if (line)
        free(line);
}

void welcomeReturningCustomer(const char *name, double budget)
{
    printf("Welcome back, %s! Your budget is %.2f\n", name, budget);
}

void initializeNewCustomer(struct Customer *customer)
{
    printf("Enter your name: ");
    scanf("%s", customer->name);

    printf("Enter your budget: ");
    scanf("%lf", &customer->budget);

    printf("Welcome, %s!\n", customer->name);
    customer->index = 0;
}

/**
 * This function processes customer orders by taking user input for the customer's name, budget,
 * and product orders. It validates the product orders against the shop's inventory.
 *
 * @param customers Pointer to an array of Customer structures where the processed customer information will be stored.
 * @param shop Pointer to the Shop structure containing shop inventory details.
 */
void processCustomerOrder(struct Customer *customers, struct Shop *shop)
{
    FILE *fp;
    fp = fopen("../project/customer.csv", "r");
    if (fp == NULL)
    {
        printf("Error opening file.\n");
        exit(EXIT_FAILURE);
    }

    char line[100]; // Adjust the size according to your CSV lines

    while (fgets(line, sizeof(line), fp) != NULL)
    {
        char custName[50];
        double budget;
        sscanf(line, "%49[^,],%lf", custName, &budget); // Read name and cash

        int existingCustomer = 0;
        for (int i = 0; i < MAX_CUSTOMERS; i++)
        {
            if (strcmp(customers[i].name, custName) == 0)
            {
                existingCustomer = 1;
                welcomeReturningCustomer(custName, budget);
                break;
            }
        }

        if (!existingCustomer)
        {
            initializeNewCustomer(&customers[0]);
        }
        {
            shop->stock = (struct ProductStock *)realloc(shop->stock, sizeof(struct ProductStock) * (shop->index + 1));
        }

        // Process product orders
        printf("Enter your product orders (name quantity), type 'quit' to finish:\n");
        char prodName[50];
        int quantity;

        while (1)
        {
            scanf("%s", prodName);
            if (strcmp(prodName, "quit") == 0)
                break;

            scanf("%d", &quantity);

            // Check if the entered product exists in the shop's inventory
            int productIndex;
            for (productIndex = 0; productIndex < shop->index; productIndex++)
            {
                if (strcmp(shop->stock[productIndex].product.name, prodName) == 0)
                {
                    if (quantity > shop->stock[productIndex].quantity)
                    {
                        printf("Error: Insufficient stock for %s. Please try again later.\n", prodName);
                        break;
                    }
                }
            }

            // If the product doesn't exist in the inventory, display an error
            if (productIndex == shop->index)
            {
                printf("Error: Product %s not found in the shop's inventory.\n", prodName);
                continue;
            }

            // Add the ordered product to the customer's shopping list
            strcpy(customers->shoppingList[customers->index].product.name, prodName);
            customers->shoppingList[customers->index].product.price = 0.0;
            customers->shoppingList[customers->index].quantity = quantity;
            customers->index++;
        }
    }

    // Close the customer.csv file after processing all customers
    fclose(fp);

    // Update stock.csv after processing all customers
    FILE *stockFile = fopen("../project/stock.csv", "w");
    if (stockFile == NULL)
    {
        printf("Error opening stock file.\n");
        exit(EXIT_FAILURE);
    }

    // Write shop's cash to the stock.csv file
    fprintf(stockFile, "%.2f\n", shop->shopfloat);

    // Write updated stock quantities to the stock.csv file
    for (int i = 0; i < shop->index; i++)
    {
        fprintf(stockFile, "%s,%.2f,%d\n",
                shop->stock[i].product.name,
                shop->stock[i].product.price,
                shop->stock[i].quantity);
    }
}

int main(void)
{
    struct Shop shop;
    createAndStockshop(&shop);
    printShop(shop);

    // Dynamic allocation for customers
    struct Customer *customers = malloc(sizeof(struct Customer) * MAX_CUSTOMERS);
    if (customers == NULL) {
        printf("Memory allocation failed for customers.\n");
        return EXIT_FAILURE;
    }

    processCustomerOrder(customers, &shop);

    // Free dynamically allocated memory
    free(customers);
    return 0;
}