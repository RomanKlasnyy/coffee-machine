import java.util.Scanner;

public class CoffeeMachine {
    private static int water = 400;
    private static int milk = 540;
    private static int coffee = 120;
    private static int cups = 9;
    private static int money = 550;

    public static void remaining() {
        System.out.println("The coffee machine has:");
        System.out.println(water + " of water");
        System.out.println(milk + " of milk");
        System.out.println(coffee + " of coffee beans");
        System.out.println(cups + " of disposable cups");
        System.out.println(money + " of money");
    }

    public static void buy() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:");
        String coffeeType = scanner.nextLine();
        switch (coffeeType) {
            case "1":
                if (water >= 250 && coffee >= 16 && cups >= 1) {
                    water -= 250;
                    coffee -= 16;
                    cups -= 1;
                    money += 4;
                    System.out.println("I have enough resources, making you a coffee!");
                } else if (water < 250) {
                    System.out.println("Sorry, not enough water!");
                } else if (coffee < 16) {
                    System.out.println("Sorry, not enough coffee beans!");
                } else if (cups < 1) {
                    System.out.println("Sorry, not enough disposable cups!");
                }
                break;
            case "2":
                if (water >= 350 && milk >= 75 && coffee >= 20 && cups >= 1) {
                    water -= 350;
                    milk -= 75;
                    coffee -= 20;
                    cups -= 1;
                    money += 7;
                    System.out.println("I have enough resources, making you a coffee!");
                } else if (water < 350) {
                    System.out.println("Sorry, not enough water!");
                } else if (milk < 75) {
                    System.out.println("Sorry, not enough milk!");
                } else if (coffee < 20) {
                    System.out.println("Sorry, not enough coffee beans!");
                } else if (cups < 1) {
                    System.out.println("Sorry, not enough disposable cups!");
                }
                break;
            case "3":
                if (water >= 200 && milk >= 100 && coffee >= 12 && cups >= 1) {
                    water -= 200;
                    milk -= 100;
                    coffee -= 12;
                    cups -= 1;
                    money += 6;
                    System.out.println("I have enough resources, making you a coffee!");
                } else if (water < 200) {
                    System.out.println("Sorry, not enough water!");
                } else if (milk < 100) {
                    System.out.println("Sorry, not enough milk!");
                } else if (coffee < 12) {
                    System.out.println("Sorry, not enough coffee beans!");
                } else if (cups < 1) {
                    System.out.println("Sorry, not enough disposable cups!");
                }
                break;
            default:
                System.out.println("Please, write 1, 2 or 3 for a coffee!");
                break;
        }
    }

    public static void fill() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Write how many ml of water do you want to add:");
        int waterFill = scanner.nextInt();
        water += waterFill;
        System.out.println("Write how many ml of milk do you want to add:");
        int milkFill = scanner.nextInt();
        milk += milkFill;
        System.out.println("Write how many grams of coffee beans do you want to add:");
        int coffeeFill = scanner.nextInt();
        coffee += coffeeFill;
        System.out.println("Write how many disposable cups of coffee do you want to add:");
        int cupsFill = scanner.nextInt();
        cups += cupsFill;
    }

    public static void take() {
        System.out.println("I gave you $" + money);
        money = 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Write action (buy, fill, take, remaining, exit):");
            String action = scanner.nextLine();
            switch (action) {
                case "buy":
                    buy();
                    break;
                case "fill":
                    fill();
                    break;
                case "take":
                    take();
                    break;
                case "remaining":
                    remaining();
                    break;
                case "exit":
                    return;
                default:
                    System.out.println("Unknown action.");
                    break;
            }
        }
    }
}
