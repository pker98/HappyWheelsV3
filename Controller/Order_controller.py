from Repository.Orders_repo import Orders_repo
from UI.Print_cancel_order_menu import Print_cancel_order_menu
from Services.Cancel_order_service import Cancel_order_service
from Utilizations.Salesman_validation import Salesman_validation
from Utilizations.Salesman_validation import Salesman_validation


class Order_controller:
    def __init__(self):
        # UI's
        self.__menu = Print_cancel_order_menu()
        # Services
        self.__cancel_service = Cancel_order_service()
        # Validations
        self.__Salesman_valid = Salesman_validation()
    
    def cancel_order_process(self, page):
        """ Finds order from user's input and deletes it from the database """
        order_num = self.__menu.find_by_num()
        Page = self.__Salesman_valid.Check_navigation(order_num, page)

        if Page == 2:
            order = self.__cancel_service.get_order(order_num)
            if order != None:
                self.__menu.print_order(order)
                choice = self.__menu.choice()
                if choice == "d":
                    self.__cancel_service.delete_order(order_num)
                    self.__menu.confirmation()
            else:
                self.__menu.No_match(order_num)
            return Page
        else: 
            return Page





