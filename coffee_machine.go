package main

import (
	"fmt"
)

type CoffeeMachine struct {
	water  int
	milk   int
	coffee int
	cups   int
	money  int
}

func NewCoffeeMachine() *CoffeeMachine {
	return &CoffeeMachine{
		water:  400,
		milk:   540,
		coffee: 120,
		cups:   9,
		money:  550,
	}
}

func (c *CoffeeMachine) remaining() {
	fmt.Println("The coffee machine has:")
	fmt.Printf("%d of water\n", c.water)
	fmt.Printf("%d of milk\n", c.milk)
	fmt.Printf("%d of coffee beans\n", c.coffee)
	fmt.Printf("%d of disposable cups\n", c.cups)
	fmt.Printf("%d of money\n", c.money)
}

func (c *CoffeeMachine) buy() {
	var coffeeType string
	fmt.Println("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
	fmt.Scanln(&coffeeType)

	switch coffeeType {
	case "1":
		if c.water >= 250 && c.coffee >= 16 && c.cups >= 1 {
			c.water -= 250
			c.coffee -= 16
			c.cups -= 1
			c.money += 4
			fmt.Println("I have enough resources, making you a coffee!")
		} else if c.water < 250 {
			fmt.Println("Sorry, not enough water!")
		} else if c.coffee < 16 {
			fmt.Println("Sorry, not enough coffee beans!")
		} else if c.cups < 1 {
			fmt.Println("Sorry, not enough disposable cups!")
		}
	case "2":
		if c.water >= 350 && c.milk >= 75 && c.coffee >= 20 && c.cups >= 1 {
			c.water -= 350
			c.milk -= 75
			c.coffee -= 20
			c.cups -= 1
			c.money += 7
			fmt.Println("I have enough resources, making you a coffee!")
		} else if c.water < 350 {
			fmt.Println("Sorry, not enough water!")
		} else if c.milk < 75 {
			fmt.Println("Sorry, not enough milk!")
		} else if c.coffee < 20 {
			fmt.Println("Sorry, not enough coffee beans!")
		} else if c.cups < 1 {
			fmt.Println("Sorry, not enough disposable cups!")
		}
	case "3":
		if c.water >= 200 && c.milk >= 100 && c.coffee >= 12 && c.cups >= 1 {
			c.water -= 200
			c.milk -= 100
			c.coffee -= 12
			c.cups -= 1
			c.money += 6
			fmt.Println("I have enough resources, making you a coffee!")
		} else if c.water < 200 {
			fmt.Println("Sorry, not enough water!")
		} else if c.milk < 100 {
			fmt.Println("Sorry, not enough milk!")
		} else if c.coffee < 12 {
			fmt.Println("Sorry, not enough coffee beans!")
		} else if c.cups < 1 {
			fmt.Println("Sorry, not enough disposable cups!")
		}
	default:
		fmt.Println("Please, write 1, 2 or 3 for a coffee!")
	}
}

func (c *CoffeeMachine) fill() {
	var waterFill, milkFill, coffeeFill, cupsFill int
	fmt.Println("Write how many ml of water do you want to add:")
	fmt.Scanln(&waterFill)
	c.water += waterFill
	fmt.Println("Write how many ml of milk do you want to add:")
	fmt.Scanln(&milkFill)
	c.milk += milkFill
	fmt.Println("Write how many grams of coffee beans do you want to add:")
	fmt.Scanln(&coffeeFill)
	c.coffee += coffeeFill
	fmt.Println("Write how many disposable cups of coffee do you want to add:")
	fmt.Scanln(&cupsFill)
	c.cups += cupsFill
}

func (c *CoffeeMachine) take() {
	fmt.Printf("I gave you $%d\n", c.money)
	c.money = 0
}

func main() {
	coffeeMachine := NewCoffeeMachine()
	for {
		var action string
		fmt.Println("Write action (buy, fill, take, remaining, exit):")
		fmt.Scanln(&action)

		switch action {
		case "buy":
			coffeeMachine.buy()
		case "fill":
			coffeeMachine.fill()
		case "take":
			coffeeMachine.take()
		case "remaining":
			coffeeMachine.remaining()
		case "exit":
			return
		default:
			fmt.Println("Unknown action.")
		}
	}
}
