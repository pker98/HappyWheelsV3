class Arts(object):
    def __init__(self):
        pass
    
    def get_happy_wheels(self):
        happy_wheels = [(" _    _          _____  _______     __   __          ___    _ ______ ______ _       _____"), 
        ("| |  | |   /\   |   _ \|  __ \ \   / /   \ \        / / |  | |  ____|  ____| |     / ____|"),
        ("| |__| |  /  \  | |__) | |__) \ \_/ /     \ \  /\  / /| |__| | |__  | |__  | |    | (___  "),
        ("|  __  | / /\ \ |  ___/|  ___/ \   /       \ \/  \/ / |  __  |  __| |  __| | |     \___ \ "),
        ("| |  | |/ ____ \| |    | |      | |         \  /\  /  | |  | | |____| |____| |____ ____) |"),
        ("|_|  |_/_/    \_\_|    |_|      |_|          \/  \/   |_|  |_|______|______|______|_____/ ")]

        for line in happy_wheels:
            print(line)
        print("\n")


    def get_car(self):
        car = [("\t\t\t\t          ,-----,     "),
        ("\t\t\t\t        ,--'---:---`--,"),
        ("\t\t\t\t ~ ~ ~ ==(o)-----(o)==J")]

        for line in car:
            print(line)
            
        input("\n\t\t\t\tPress enter to continue")
