class Flight ():
    def __init__(self , capacity):
        self.cpacity =capacity 
        self.passengers = []

    def add_passengers (self, passenger ) : 
        if not self.open_seats():
            return False 
        self.passengers.append(passenger) 
        return True 

    def open_seats(self): 
        return self.cpacity -len(self.passengers)
F = Flight(3)
people = ["ahmed " , "salah" , "mahmoud" , " wael "]
for i in people : 
    if F.add_passengers(i) :
        print(F"Added {i} to the flight  ")
    else : 
        print(F"No available seats for {i}")

                    