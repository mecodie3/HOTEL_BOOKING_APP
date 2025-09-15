import pandas

#specify which columns should be treated as the strings
df = pandas.read_csv("hotels.csv",dtype={"id" : str})
df_cards= pandas.read_csv("cards.csv",dtype=str).to_dict(orient="records")

class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id=hotel_id
        self.name=df.loc[df["id"]==self.hotel_id,"name"].squeeze()

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


class ReservationTicket:
    def __init__(self,customer_name,hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content=f"""
        Thank you for your reservation!
        Here are your booking data:
        Name:{self.customer_name}
        Hotel name:{self.hotel.name}"""
        return content

class CreditCard:
    def __init__(self,creditcard_number):
        self.number=creditcard_number


    def validate(self,expr,holder_name,cvc_number):
        card_data = {"number":self.number,"expiration":expr,"cvc":cvc_number,
                     "holder":holder_name}
        if card_data in df_cards:
            return True
        else:
            return False

print(df)
hotel_ID = input("Enter the id of the hotel:")
hotel= Hotel(hotel_ID)
if hotel.available():
    card_number = input("Enter the credit card number: ")
    expiration = input("Enter the expiration number: ")
    credit_card=CreditCard(creditcard_number="1234")
    if credit_card.validate(expr="12/26",holder_name="JOHN SMITH",cvc_number="123"):
        hotel.book()
        client_name = input("Enter your name:")
        reservationConfirm = ReservationTicket(customer_name=client_name,hotel_object=hotel)
        print(reservationConfirm.generate())
    else:
        print(" There was a problem with your payment")
else:
    print("Hotel is not free.")