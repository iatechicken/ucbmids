from sys import exit
from datetime import date

class Market:
    """dictionary of 4 items from the BBQ shop with prices.
    Prices stored and updated in this dictionary will be used
    to calculate the balance of the Cashier() when restocking the fridge"""

    def __init__(self):

        self.inventory = {1:22.25, 2:15.99, 3:14.99, 4:14.99}
        self.inventory_date = {1:date(2018, 7,2), 2:date(2018, 7,2), 3:date(2018, 7,2), 4:date(2018, 7,2)}

    #price or amount will never be negative
    def update_item(self, item, amt):
        if amt >= 0:
            self.inventory[item] = amt
        else:
            print("Please check your quantity")

    def update_date(self, item, day):
        self.inventory_date[item] = day

    def calc_date(self, item):
        meats = {1:"short ribs", 2:"pork belly", 3: "pork stir fry", 4:"beef stir fry"}
        a = self.inventory_date[item]
        today = date.today()
        delta_date = today - a
        print("It's been " + str(delta_date.days) + " days since the last purchase of "
         + meats[item])

    #using meats dictionary, user input will be used as key to identify the
    #names associated with each input key
    def __str__(self):
        meats = {1:"short ribs", 2:"pork belly", 3: "pork stir fry", 4:"beef stir fry"}
        temp_string = "\n"
        for key in meats:
            temp_string += meats[key] + ": $" + str(self.inventory[key]) + "\n"
        return temp_string

class Menu:
    """Serves as the menu, which will hold prices for each items in the restaurant"""
    def __init__(self):
       self.menulist = {1:31.25, 2:22.99, 3:19.99, 4:24.99}
    #price or amount will never be negative
    def update_item(self, item, amt):
        if amt >= 0:
            self.menulist[item] = amt
        else:
            print("Please check your quantity")
    #using meats dictionary, user input will be used as key to identify the
    #names associated with each input key
    def __str__(self):
        meats = {1:"short ribs", 2:"pork belly", 3: "pork stir fry", 4:"beef stir fry"}
        temp_string = "\n"
        for key in meats:
            temp_string += meats[key] + ": $" + str(self.menulist[key]) + "\n"
        return temp_string

class Cashier:
    """starts off with initial balance of $2500 and will look up prices
    from the Market() class and then multiply with the qty of the items to
    correctly update the balance of the cashier"""
    def __init__(self, market, menu):
        self.balance = 2500.00
        self.market = market
        self.menu = menu

    #qty comes from the main while amt comes from the Market()
    def sell_meat(self, item, qty):
        menu = Menu()
        amt = qty * self.menu.menulist[item]
        self.balance += amt
    #qty comes from the main while amt comes from the Market()
    def buy_meat(self, item, qty):
        market = Market()
        amt = qty * self.market.inventory[item]
        self.balance -= amt

    def __str__(self):
        final_balance = "Balance: $" + str(self.balance)
        return final_balance



class Fridge:
    """Serves as the inventory of YJ's Korean BBQ. It starts off with initial
    inventory of the 4 items and the qty of these items will change depending
    on the sales or purchase of the items"""
    def __init__(self):
       self.inventory = {1:30, 2:40, 3:65, 4:23}

    def stock_item(self, item, qty):

        if qty >= 0:
            self.inventory[item] += qty
        else:
            print("Please check your quantity")

    def sell_item(self, item, qty):
        if self.inventory[item] > 0:
            self.inventory[item] -= qty
        else:
            print("There are no more of these items in stock!")

    #using meats dictionary, user input will be used as key to identify the
    #names associated with each input key
    def __str__(self):
        meats = {1:"short ribs", 2:"pork belly", 3: "pork stir fry", 4:"beef stir fry"}
        temp_string = "\n"
        for key in meats:
            temp_string += meats[key] + ": " + str(self.inventory[key]) + "\n"

        return temp_string

class Shop:
    """Main engine of the BBQ Management program"""

    #error handling for user input options
    def get_num(self, question, max_number):
        valid = False
        while not valid:
            result = input(question)
            if result.isdigit() and int(result) < max_number and int(result) > 0:
                return int(result)
            print("Please enter a valid option")

    #error handling for user input options of the qty
    def get_qty(self, question, max_number):
        valid = False
        while not valid:
            result = input(question)
            if result.isdigit() and int(result) < max_number and int(result) > 0:
                return int(result)
            print("Please enter a valid quantity")

    #error handling for user input options of the prices
    def get_amt(self, question, max_number):
        valid = False
        result = 0
        while not valid:
            try:
                result = float(input(question))
                valid = True
            except ValueError:
                print("Please enter a valid amount")
                valid = False
            except:
                print("Please enter a valid amount")
                valid = False
            if valid and result < 0:
                print("Do not enter negative amount, please try again")
                valid = False
            elif valid and max_number > result > 0.0:
                return float(result)
            elif valid and result > max_number:
                print("That is an unrealistic price, please try again")
                valid = False

    #main engine
    def meatshop(self):
        #initialization
        fridge = Fridge()
        market = Market()
        menu = Menu()
        cashier = Cashier(market, menu)

        #main menu
        done = False
        while not done:
            print("\nYJ's Korean BBQ Management System\n\n")
            print("Press 1 to update records")
            print("Press 2 to check your fridge")
            print("Press 3 to check your cashier")
            print("Press 4 to check the market")
            print("Press 5 to check the menu")
            print("Press 6 to check the date of last purchase")
            print("Press 7 to quit\n")
            prompt = self.get_num("What can we do today?\t",8)

            #record keeping menu
            if prompt == 1:
                print("\nPress 1 for sales")
                print("Press 2 for restock")
                print("Press 3 to update the market")
                print("Press 4 to update the menu ")
                print("Press 5 to go back\n")
                west = self.get_num("Choose the options listed above\t", 6)

                #workflow when an item is sold
                if west == 1:
                    print("\nPress 1 for short ribs")
                    print("Press 2 for pork belly")
                    print("Press 3 for pork stir fry")
                    print("Press 4 for beef stir fry\n")
                    sale_item = self.get_num("Choose the item that you've sold\t", 5)
                    sale_qty = self.get_qty("Enter the qty:\t", 1000)
                    fridge.sell_item(sale_item, sale_qty)
                    cashier.sell_meat(sale_item, sale_qty)
                    print("Update complete!")

                #workflow when an item is stocked
                elif west == 2:
                    print("\nPress 1 for short ribs")
                    print("Press 2 for pork belly")
                    print("Press 3 for pork stir fry")
                    print("Press 4 for beef stir fry\n")
                    restock_item = self.get_num("Choose the item that you're restocking\t", 5)
                    restock_qty = self.get_qty("Enter the qty:\t", 1000)
                    fridge.stock_item(restock_item, restock_qty)
                    cashier.buy_meat(restock_item, restock_qty)
                    market.update_date(restock_item, date.today())
                    print("Update complete!")

                #workflow to update the prices of the items in the market
                elif west == 3:
                    print("\nPress 1 for short ribs")
                    print("Press 2 for pork belly")
                    print("Press 3 for pork stir fry")
                    print("Press 4 for beef stir fry\n")
                    market_item = self.get_num("Choose the item that you want to update\t", 5)
                    market_amount = self.get_amt("Enter the amount:\t", 5000.00)
                    market.update_item(market_item, market_amount)
                    print("Update complete!")

                #workflow to update the prices of the items in the menu
                elif west == 4:
                    print("\nPress 1 for short ribs")
                    print("Press 2 for pork belly")
                    print("Press 3 for pork stir fry")
                    print("Press 4 for beef stir fry\n")
                    menu_item = self.get_num("Choose the item that you want to update\t", 5)
                    menu_amount = self.get_amt("Enter the amount:\t", 5000.00)
                    menu.update_item(menu_item, menu_amount)
                    print("Update complete!")

                #option to go back to the main menu
                elif west == 5:
                    continue

            #inventory status from Fridge()
            elif prompt == 2:
                print("\nThis is what you have in the fridge: ", fridge)

            #current balance from Cashier()
            elif prompt == 3:
                print("\nYour balance is: ", cashier)

            #displays current prices for the items
            elif prompt == 4:
                print("\nThis is what the market looks like: ", market)

            #displays the current menu
            elif prompt == 5:
                print("\nThis is what the menu looks like: ", menu)

            #option to check for last purchase date of each item
            elif prompt == 6:
                print("\nPress 1 for short ribs")
                print("Press 2 for pork belly")
                print("Press 3 for pork stir fry")
                print("Press 4 for beef stir fry\n")
                date_check = self.get_num("Choose the item that you want to check last purchase date\t", 5)
                market.calc_date(date_check)

            #end
            elif prompt == 7:
                print("\nSee you later!")
                done = True






run = Shop()
run.meatshop()
