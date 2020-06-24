class Coffee:
    water = 400
    milk = 540
    coffee = 120
    cups = 9
    money = 550

    def remaining():
        print('The coffee machine has:')
        print(f'{Coffee.water} of water')
        print(f'{Coffee.milk} of milk')
        print(f'{Coffee.coffee} of coffee beans')
        print(f'{Coffee.cups} of disposable cups')
        print(f'{Coffee.money} of money')

    def buy():
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        coffee_type = input()
        if coffee_type == '1':
            if Coffee.water >= 250 and Coffee.coffee >= 16 and Coffee.cups >= 1:
                Coffee.water -= 250
                Coffee.coffee -= 16
                Coffee.cups -= 1
                Coffee.money += 4
                print('I have enough resources, making you a coffee!')
            elif Coffee.water < 250:
                print('Sorry, not enough water!')
            elif Coffee.coffee < 16:
                print('Sorry, not enough coffee beans!')
            elif Coffee.cups < 1:
                print('Sorry, not enough disposable cups!')

        elif coffee_type == '2':
            if Coffee.water >= 350 and Coffee.milk >= 75 and Coffee.coffee >= 20 and Coffee.cups >= 1:
                Coffee.water -= 350
                Coffee.milk -= 75
                Coffee.coffee -= 20
                Coffee.cups -= 1
                Coffee.money += 7
                print('I have enough resources, making you a coffee!')
            elif Coffee.water < 350:
                print('Sorry, not enough water!')
            elif Coffee.milk < 75:
                print('Sorry, not enough milk!')
            elif Coffee.coffee < 20:
                print('Sorry, not enough coffee beans!')
            elif Coffee.cups < 1:
                print('Sorry, not enough disposable cups!')

        elif coffee_type == '3':
            if Coffee.water >= 200 and Coffee.milk >= 100 and Coffee.coffee >= 12 and Coffee.cups >= 1:
                Coffee.water -= 200
                Coffee.milk -= 100
                Coffee.coffee -= 12
                Coffee.cups -= 1
                Coffee.money += 6
                print('I have enough resources, making you a coffee!')
            elif Coffee.water < 200:
                print('Sorry, not enough water!')
            elif Coffee.milk < 100:
                print('Sorry, not enough milk!')
            elif Coffee.coffee < 12:
                print('Sorry, not enough coffee beans!')
            elif Coffee.cups < 1:
                print('Sorry, not enough disposable cups!')
        else:
            print('Please, write 1, 2 or 3 for a coffee!')

    def fill():
        print('Write how many ml of water do you want to add:')
        water_fill = int(input())
        Coffee.water += water_fill
        print('Write how many ml of milk do you want to add:')
        milk_fill = int(input())
        Coffee.milk += milk_fill
        print('Write how many grams of coffee beans do you want to add:')
        coffee_fill = int(input())
        Coffee.coffee += coffee_fill
        print('Write how many disposable cups of coffee do you want to add:')
        cups_fill = int(input())
        Coffee.cups += cups_fill

    def take():
        print(f'I gave you ${Coffee.money}')
        Coffee.money = 0


while True:
    print('Write action (buy, fill, take, remaining, exit):')
    action = input()
    if action == 'buy':
        Coffee.buy()

    elif action == 'fill':
        Coffee.fill()

    elif action == 'take':
        Coffee.take()

    elif action == 'remaining':
        Coffee.remaining()

    elif action == 'exit':
        break

    else:
        print('Unknown action.')
