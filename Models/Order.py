#from Customer import Customer
import datetime

class Order:
    def __init__(self, order_num,pick_up_date,drop_off_date,plate_number,cust_email):  
        # Gæti verið cust_ID frekar 
        ### Hægt að gera þetta á skilvirkari hátt?? ###
        self.order_num = order_num  
        self.pick_up_date = pick_up_date
        self.drop_off_date = drop_off_date
        self.plate_number = plate_number    # Sækir þetta hjá "Car" klasanum með get skipun
        self.cust_email = cust_email

    def __str__(self):
        return ("Customer email: {:20}\tOrder number: {:20}\nPick up date: {:20}\tDrop off date: {:20}".format(self.cust_email,
        self.order_num, self.pick_up_date,self.drop_off_date))
                                            ######################################################
    def __repr__(self):                     # Adda pöntun fyrir ofan með smiðnum ( __init__ )
        return repr([self.pick_up_date,self.drop_off_date,
        self.order_num,self.cust_email])                      

    def get_order_num(self):
        return self.order_num
    
    def get_cust_email(self):
        return self.cust_email

    def get_pick_up_date(self):
        # Format: Year, month, day
        if type(self.pick_up_date) == str: 
            pick_up_list = self.pick_up_date.split("-")
            self.pick_up_date = datetime.date(int(pick_up_list[0]), int(pick_up_list[1]), int(pick_up_list[2]))
        return self.pick_up_date
    
    def get_drop_off_date(self):
        if type(self.drop_off_date) == str: 
            drop_off_list = self.drop_off_date.split("-")
            self.drop_off_date = datetime.date(int(drop_off_list[0]), int(drop_off_list[1]), int(drop_off_list[2]))
        return self.drop_off_date

    def get_plate_number(self):
        return self.plate_number