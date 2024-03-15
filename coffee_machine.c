#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int water;
    int milk;
    int coffee;
    int cups;
    int money;
} CoffeeMachine;

void init(CoffeeMachine *machine) {
    machine->water = 400;
    machine->milk = 540;
    machine->coffee = 120;
    machine->cups = 9;
    machine->money = 550;
}

void remaining(CoffeeMachine machine) {
    printf("The coffee machine has:\n");
    printf("%d of water\n", machine.water);
    printf("%d of milk\n", machine.milk);
    printf("%d of coffee beans\n", machine.coffee);
    printf("%d of disposable cups\n", machine.cups);
    printf("%d of money\n", machine.money);
}

void buy(CoffeeMachine *machine) {
    printf("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n");
    char coffee_type[2];
    scanf("%1s", coffee_type);
    int type = atoi(coffee_type);

    if (type == 1) {
        if (machine->water >= 250 && machine->coffee >= 16 && machine->cups >= 1) {
            machine->water -= 250;
            machine->coffee -= 16;
            machine->cups -= 1;
            machine->money += 4;
            printf("I have enough resources, making you a coffee!\n");
        } else {
            printf("Sorry, not enough resources!\n");
        }
    } else if (type == 2) {
        if (machine->water >= 350 && machine->milk >= 75 && machine->coffee >= 20 && machine->cups >= 1) {
            machine->water -= 350;
            machine->milk -= 75;
            machine->coffee -= 20;
            machine->cups -= 1;
            machine->money += 7;
            printf("I have enough resources, making you a coffee!\n");
        } else {
            printf("Sorry, not enough resources!\n");
        }
    } else if (type == 3) {
        if (machine->water >= 200 && machine->milk >= 100 && machine->coffee >= 12 && machine->cups >= 1) {
            machine->water -= 200;
            machine->milk -= 100;
            machine->coffee -= 12;
            machine->cups -= 1;
            machine->money += 6;
            printf("I have enough resources, making you a coffee!\n");
        } else {
            printf("Sorry, not enough resources!\n");
        }
    } else {
        printf("Unknown coffee type.\n");
    }
}

void fill(CoffeeMachine *machine) {
    printf("Write how many ml of water do you want to add:\n");
    int added_water;
    scanf("%d", &added_water);
    machine->water += added_water;
    printf("Write how many ml of milk do you want to add:\n");
    int added_milk;
    scanf("%d", &added_milk);
    machine->milk += added_milk;
    printf("Write how many grams of coffee beans do you want to add:\n");
    int added_coffee;
    scanf("%d", &added_coffee);
    machine->coffee += added_coffee;
    printf("Write how many disposable cups of coffee do you want to add:\n");
    int added_cups;
    scanf("%d", &added_cups);
    machine->cups += added_cups;
}

void take(CoffeeMachine *machine) {
    printf("I gave you $%d\n", machine->money);
    machine->money = 0;
}

int main() {
    CoffeeMachine coffee_machine;
    init(&coffee_machine);

    while (1) {
        printf("Write action (buy, fill, take, remaining, exit):\n");
        char action[10];
        scanf("%s", action);

        if (strcmp(action, "buy") == 0) {
            buy(&coffee_machine);
        } else if (strcmp(action, "fill") == 0) {
            fill(&coffee_machine);
        } else if (strcmp(action, "take") == 0) {
            take(&coffee_machine);
        } else if (strcmp(action, "remaining") == 0) {
            remaining(coffee_machine);
        } else if (strcmp(action, "exit") == 0) {
            break;
        } else {
            printf("Unknown action.\n");
        }
    }

    return 0;
}
