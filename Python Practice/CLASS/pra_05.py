# WRITE A CLASS TRAIN WHICH HAS METHODS
# TO BOOK A TICKET, GET STATUS [no of seats]
# AND GET FARE INFORMATION OF TARIN RUNNIG UNDER INDIAN RAILWAYS

class Train:
    def __init__(self,name, fare, seats):
        self.name= name
        self.fare= fare
        self.seats= seats

    def getStatus(self):
        print(f"The name pf the tarin is {self.name}")
        print(f"The seats avialable in this tarin are {self.seats}")
        print("**************************")
    def fareInfo(self):
        print(f"The price of the ticket RS is {self.fare}")
    
    def bookTicket(self):
        if(self.seats>0):
            print(f"Your tivket has been booked! And seat number is {self.seats}")
            self.seats = self.seats - 1 
            
        else:
            print("The train is full! Kindly try in tatkal.")

    def cancelTicket(self,seatNo):
        pass

    
intercity = Train("Karnataka Express: 20899", 90, 2)
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
