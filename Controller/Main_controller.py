from UI.Print_main_menu import Print_main_menu
from Controller.Rent_controller import Rent_controller
from Controller.Salesman_controller import Salesman_controller
from Controller.Order_controller import Order_controller
from Controller.Information_controller import Information_controller

class Main_controller(object):
    def __init__(self):
        # Menus
        self.__main_menu = Print_main_menu()
        # Controllers
        self.__rent_controller = Rent_controller()
        self.__salesman_controller = Salesman_controller()
        self.__order_controller = Order_controller()
        self.__information_controller = Information_controller()

    def Main_page(self,header,menu,choices,underline):
        choice = ""
        while choice != "x":
            choice = self.__main_menu.main_page(header,menu,choices,underline)
            if choice == "1":
                self.__rent_controller.Rent_page()
            elif choice == "2":
                self.__salesman_controller.sign_in_page()
                self.__salesman_controller.salesman_menu()
            elif choice == "3":
                self.__order_controller.cancel_order_process(page=2)
            elif choice == "i":
                self.__information_controller.information_page()