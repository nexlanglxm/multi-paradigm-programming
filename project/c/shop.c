#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_PRODUCTS 20
#define MAX_CUSTOMERS 10

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

        printf("Welcome, %s! Your budget is %.2f\n", custName, budget);

        printf("Enter your name: ");
        scanf("%s", custName);

        printf("Enter your budget: ");
        scanf("%lf", &budget);

        printf("Welcome, %s!\n", custName);

        // Initialize a new customer
        strcpy(customers->name, custName);
        customers->budget = budget;
        customers->index = 0;

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
        fclose(fp);
        fclose(fp);
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

        fclose(stockFile);
    }
}

/**
 * This function prints the customer's shopping list and calculates the total cost of the order.
 *
 * @param customer Pointer to the Customer structure containing the customer's shopping list.
 * @param shop Pointer to the Shop structure containing shop inventory details.
 */

int main(void)
{
    struct Shop shop;
    createAndStockshop(&shop);
    printShop(shop);

    struct Customer customers[MAX_CUSTOMERS];
    processCustomerOrder(customers, &shop);

    return 0;
}
