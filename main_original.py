import pandas

#specify which columns should be treated as the strings
df = pandas.read_csv("hotels.csv",dtype={"id" : str})
df_cards= pandas.read_csv("cards.csv",dtype=str).to_dict(orient="records")
df_cards_security = pandas.read_csv("card_security.csv",dtype=str)

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
class SpaHotel(Hotel):
    def book_spa_package(self):
        pass

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

class SecureCreditCard(CreditCard):
    def authenticate(self,given_password):
        #password = df_cards_security.loc[df_cards_security["number"] == self.number,"password"].squeeze()
        #handle multiple matches
        password_series = df_cards_security.loc[df_cards_security["number"] == self.number, "password"]

        if not password_series.empty:
            password = password_series.iloc[0]  # first match
            return password == given_password
        else:
            return False


class SpaTicket:
    def __init__(self,customer_name,hotel_object):
        self.customer_name=customer_name
        self.hotel =hotel_object

    def generate(self):
        content = f"""
        Thank you for your SPA reservation!
        Here are you SPA booking data:
        Name:{self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content



print(df)
hotel_ID = input("Enter the id of the hotel:")
hotel= SpaHotel(hotel_ID)
if hotel.available():
    card_number = input("Enter the credit card number: ")
    expiration = input("Enter the expiration number: ")
    credit_card=SecureCreditCard(creditcard_number="1234567890123456")
    if credit_card.validate(expr="12/26",holder_name="JOHN SMITH",cvc_number="123"):
        if credit_card.authenticate(given_password = "mypass"):
            hotel.book()
            client_name = input("Enter your name:")
            reservationConfirm = ReservationTicket(customer_name=client_name,hotel_object=hotel)
            print(reservationConfirm.generate())
            spa = input("Do you want to book a spa package?")
            if spa =="yes":
                hotel.book_spa_package()
                spa_ticket =SpaTicket(customer_name=client_name, hotel_object=hotel)
                print(spa_ticket.generate())

        else:
            print("Credit card authentification failed")
    else:
        print(" There was a problem with your payment")
else:
    print("Hotel is not free.")