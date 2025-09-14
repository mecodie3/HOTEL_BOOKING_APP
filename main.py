import pandas

#specify which columns should be treated as the strings
df = pandas.read_csv("hotels.csv",dtype={"id" : str})


class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id=hotel_id
        pass
    def book(self):
        """  Book a hotel by changing its availability to no"""
        df.loc[df["id"]== self.hotel_id,"available"]="no"
        df.to_csv("hotels.csv",index=False)

    def available(self):
        """Check if the hotel is available"""
        availability=df.loc[df["id"]==self.hotel_id,"available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationConfirm:
    def __init__(self,customer_name,hotel_object):
        pass

    def generate(self):
        pass

print(df)
hotel_ID = input("Enter the id of the hotel:")
hotel= Hotel(hotel_ID)
if hotel.available():
    hotel.book()
    name = input("Enter your name:")
    reservationConfirm = ReservationConfirm(name,hotel)
    reservationConfirm.generate()
else:
    print("Hotel is not free.")