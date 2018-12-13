from Controller.Main_controller import Main_controller
from Repository.Cars_repo import Cars_repo
from Controller.Rent_controller import Rent_controller
from Utilizations.Arts import Arts
from Utilizations.Format_text import Format_text
import os

def main():
    os.system("cls||clear")
    print_art_page = Arts()
    print_art_page.get_happy_wheels()
    print_art_page.get_car()
    get_format = Format_text()
    start_program = Main_controller()
    header, main_menu, choices, underline = get_format.main_menu_format()
    start_program.Main_page(header, main_menu, choices, underline)

main()

