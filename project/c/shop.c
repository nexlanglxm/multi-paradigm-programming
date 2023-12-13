#include <stdio.h>
#include <string.h>
#include <stdlib.h>

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
    struct ProductStock shoppingList[10];
    int index;
};

void printProduct(struct Product p)
{
    printf("--------------------\n");
    printf("PRODUCT NAME: %s\n PRODUCT PRICE: %.2f\n", p.name, p.price);
    printf("--------------------\n");
}

void printShop(struct Shop s)
{
    printf("Shop has %.2f in cash\n", s.shopfloat);
    for (int i = 0; i < s.index; i++)
    {
        printProduct(s.stock[i].product);
        printf("The shop has %d of the above\n", s.stock[i].quantity);
    }
}

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

void processCustomerOrder(struct Customer *customers, struct Shop *shop)
{
    printf("Enter your name: ");
    char custName[50];
    scanf("%s", custName);

    double budget;
    printf("Enter your budget: ");
    scanf("%lf", &budget);

    printf("Welcome, %s!\n", custName);

    struct Customer customer;
    strcpy(customer.name, custName);
    customer.budget = budget;

    int customerIndex = 0;
    customers[customerIndex++] = customer;

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

        if (productIndex == shop->index)
        {
            printf("Error: Product %s not found in the shop's inventory.\n", prodName);
            continue;
        }

        struct Product orderedProduct;
        strcpy(orderedProduct.name, prodName);
        orderedProduct.price = 0.0;
        struct ProductStock stockItem = {orderedProduct, quantity};
        customer.shoppingList[customer.index++] = stockItem;
    }
}

int main(void)
{
    struct Shop shop;
    createAndStockshop(&shop);
    printShop(shop);

    struct Customer customers[10];
    processCustomerOrder(customers, &shop);

    return 0;
}
