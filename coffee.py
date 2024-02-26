class CoffeeMachine:
    def __init__(self, water=400, milk=540, coffee=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def remaining(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        coffee_type = input()
        if coffee_type == '1':
            if self.water >= 250 and self.coffee >= 16 and self.cups >= 1:
                self.water -= 250
                self.coffee -= 16
                self.cups -= 1
                self.money += 4
                print('I have enough resources, making you a coffee!')
            else:
                print('Sorry, not enough resources!')
        elif coffee_type == '2':
            if self.water >= 350 and self.milk >= 75 and self.coffee >= 20 and self.cups >= 1:
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.cups -= 1
                self.money += 7
                print('I have enough resources, making you a coffee!')
            else:
                print('Sorry, not enough resources!')
        elif coffee_type == '3':
            if self.water >= 200 and self.milk >= 100 and self.coffee >= 12 and self.cups >= 1:
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.cups -= 1
                self.money += 6
                print('I have enough resources, making you a coffee!')
            else:
                print('Sorry, not enough resources!')
        else:
            print('Unknown coffee type.')

    def fill(self):
        print('Write how many ml of water do you want to add:')
        self.water += int(input())
        print('Write how many ml of milk do you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.coffee += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.cups += int(input())

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0


coffee_machine = CoffeeMachine()

while True:
    print('Write action (buy, fill, take, remaining, exit):')
    action = input()
    if action == 'buy':
        coffee_machine.buy()
    elif action == 'fill':
        coffee_machine.fill()
    elif action == 'take':
        coffee_machine.take()
    elif action == 'remaining':
        coffee_machine.remaining()
    elif action == 'exit':
        break
    else:
        print('Unknown action.')
