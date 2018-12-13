import os
class Print_cancel_order_menu:
    def __init__(self):
        pass

    def find_by_num(self):
        os.system('cls||clear')
        print("~~Cancel order~~\n")
        order_num = input("Enter order number: ")

        return order_num

    def confirmation(self):
        print("Order successfully canceled!")
        input("Press enter to continue ")

    def print_order(self, order):
        print("\n"+str(order))

    def choice(self):
        choice = input("Press d to delete order or enter to continue.").lower()

        return choice

    def No_match(self, order_num):
        print("There is no order number {} ".format(order_num))
        input("Press enter to continue ")
