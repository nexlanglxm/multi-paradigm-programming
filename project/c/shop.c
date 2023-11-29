#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Product {
    char* name;
    double price;
};

struct ProductStock {
    struct Product product;
    int quantity;
    double weight;
};

struct Shop {
    double shopfloat;
    struct ProductStock stock[20]; 
    int index;
};

struct Customer {
    char* name;
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

void printCustomer(struct Customer c)
{
    printf("--------------------\n");
    printf("CUSTOMER NAME: %s\n CUSTOMER BUDGET: %.2f\n", c.name, c.budget);
    printf("--------------------\n");
    for(int i = 0; i < c.index; i++)     //a low level problem here, c does not keep track of array length, so we added in index
    {
        printProduct(c.shoppingList[i].product);
        printf("%s ORDERS %d of ABOVE PRODUCT\n", c.name, c.shoppingList[i].quantity); //this is a chain of access
        double cost = c.shoppingList[i].quantity * c.shoppingList[i].product.price;
        printf("The cost to %s will be %.2feuro\n", c.name, cost);
    }
}

void createAndStockshop()
{
    struct Shop shop = {200};
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("stock.csv", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, fp)) != -1) {
        //printf("Retrieved line of length %zu:\n", read);
        //printf("%s is a line", line);
        char *n = strtok(line, ",");
        char *p = strtok(NULL, ",");
        char *q= strtok(NULL, ",");
        char *name = malloc(sizeof(char) * 25);
        strcpy(name, n);
        int quantity = atoi(q);
        double price = atof(p);
        struct Product product = { name, price };
        struct ProductStock stockItem = { product, quantity }
        shop.stock[shop.index++] = stockItem
        // printf("NAME OF PRODUCT %s PRICE %s QUANTITY %s \n", name, price, quantity);
    }

    return shop;
}

void printShop(struct Shop s)
{
    printf("Shop has %.2f in cash\n s.cash");
    for (int i = 0; i < s.index; i ++)
    {
        printProduct(s.stock[i].product);
        printf("The shop has %d of the above\n", s.stock[i].quantity);
    }
}

int main(void)
{
    // struct Customer neil = {"Neil", 100.0};
   
    // struct Product fanta = { "Can Fanta", 1.30};
    // struct Product bread = { "Bread", 0.7};
    // // printProduct(fanta);

    // struct ProductStock fantaStock = { fanta, 30 };
    // struct ProductStock breadStock = { bread, 3 };


    // neil.shoppingList[neil.index++]] = fantaStock;
    // //neil.shoppingList[neil.index++]] = breadStock;

    // //printCustomer(neil);

    struct Shop shop = createAndStockshop();
    printShop(s);

    //printf("The shop has %d of the product %s\n", fantaStock.quantity, fantaStock.product.name)

    return 0;
}