# Coffee Machine Project

This is a simple coffee machine program that applies Object-Oriented Programming (OOP) principles. It allows users to order coffee, check available resources, and process payments.

## Features
- Displays menu options for available drinks
- Checks resource availability before making coffee
- Processes payments and ensures sufficient funds
- Provides reports on machine resources and earnings
- Allows the machine to be turned off

## How It Works
1. The program initializes instances of the following classes:
   - `Menu`: Handles available drink options.
   - `CoffeeMaker`: Manages resources and prepares drinks.
   - `MoneyMachine`: Handles payments.
2. It enters a loop where users can:
   - Order a drink
   - Request a report of machine resources and money
   - Turn off the machine
3. If the selected drink is available and the user provides sufficient payment, the coffee is prepared.

## Prerequisites
- Python 3 installed

## Running the Program
1. Clone or download the repository.
2. Ensure the required modules (`menu.py`, `coffee_maker.py`, and `money_machine.py`) are in the same directory as the main script.
3. Run the script:
   ```bash
   python main.py
   ```
4. Follow the on-screen prompts to order coffee.

## Example Usage
```
What would you like? espresso/latte/cappuccino: latte
Please insert coins.
Total inserted: $2.50
Enjoy your latte!
```

## Class Breakdown
- **`Menu`**: Handles the drink options and their attributes.
- **`MenuItem`**: Represents individual drinks.
- **`CoffeeMaker`**: Checks resources and brews coffee.
- **`MoneyMachine`**: Manages transactions and tracks earnings.

## Exiting the Program
- Type `off` to turn off the coffee machine.
- Type `report` to see the current status of resources and money.

## Author
Created by Jose Victor Carpena.
