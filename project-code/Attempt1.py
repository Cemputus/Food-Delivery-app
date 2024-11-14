from abc import ABC, abstractmethod
from datetime import datetime
import random


class OrderingSystem:
    def __init__(self):
        self.__restaurants =[]
        self.__customers =[]
        self.__DeliveryPersons = []

    def set_deliver(self, instance):
        self.__DeliveryPersons.append(instance)

    def get_deliver(self):
        return self.__DeliveryPersons

    def get_restaurants(self):
        return self.__restaurants
    
    def set_restaurants(self,instance):
        self.__restaurants.append(instance)

    def get_customer(self):
        return self.__customers

    def set_customers(self,instance):
        self.__customers.append(instance)

    def display_customers(self):
        instances=self.get_customer()
        for instance in instances:
            print(instance.get_name())

    def display_restaurants(self):
        instances = self.get_restaurants()
        for instance in instances:
            print(instance.get_name())

    def display_Delivery_persons(self):
        instances =self.get_deliver()
        i = 1
        print("Available delivery guys")
        for instance in instances:
            print(f"{i}. {instance.get_name()}")
            i+=1
        


class Members(ABC):
    def __init__(self, name, address, number,password):
        self.__name = name
        self.__address = address
        self.__number = number
        self.__password = password

    def get_name(self):
        return self.__name
    
    def get_password(self):
        return self.__password
    
    def get_address(self):
        return self.__address
    
    def get_number(self):
        return self.__number

    @abstractmethod
    def display(self):
        pass

class Restaurant(Members):
    def __init__(self, name, address,number, OH, CH, password):
        super().__init__(name, address, number, password)
        self.__openingHours = OH
        self.__closingHours = CH
        self.__menu = {}
        self.__orders = []

    def get_orders(self):
        return self.__orders
    
    def set_orders(self,order):
        self.__orders.append(order)

    @property
    def menu(self):
        return self.__menu
    
    @menu.setter
    def menu(self, noItems):
        for i in range (0,noItems):
            item =input(f"Please enter item {i+1}: ").lower()
            from Attempt3 import get_price
            price = get_price(item)
            self.__menu[item]=price



    def display(self):
        if len(self.__orders) == 0:
             print("There are no orders yet")
             return 0
        else:
             for i in range(0,len(self.__orders)):
                print(f"Order {i+1}")
                self.__orders[i].display()

    def update(self, i, status):
        self.__orders[i-1].update_order(status)
        if status == "cancelled":
            self.__orders.pop(i-1)

        elif status == "approved":
            from Atempt2 import assigndeliverer
            deliveryGuy = assigndeliverer()
            deliveryGuy.set_orders(self.__orders[i-1])
            self.__orders[i-1].set_delGuy(deliveryGuy.get_name())
            self.__orders.pop(i-1)



class Customer(Members):
    def __init__(self, name, address, number, password):
        super().__init__(name, address, number, password)
        self.__orderhistory = []
        
    def get_orderHist(self):
        return self.__orderhistory

    def display(self,restaurant):
        print("Menu")
        menu = restaurant.menu
        for item, price in menu.items():
            print(f"- {item}: UGX {price}")

    def order(self,restaurant, noItems):
        from Attempt3 import get_content
        menu = restaurant.menu
        myOrder = Order()
        for i in range(0,noItems):
            get_content(myOrder, menu)
        self.__orderhistory.append(myOrder)
        restaurant.set_orders(myOrder)
        myOrder.set_restaurant(restaurant)
        return myOrder



class Order:
    def __init__(self):
        self.__contents = []
        self.___orderprices = []
        self.__totalprice = 0
        self.__orderStatus = None
        self.__timestamp = datetime.now()
        self.__deliveryGuy = None
        self.__restaurant = None
        self.__paymentmethod =None
        self. __paymentinfo = None

    def set_paymentinfo(self, info):
        self.__paymentinfo = info

    def set_paymentMethod(self, method):
        self.__paymentmethod = method

    def get_total(self):
        return self.__totalprice

    def set_delGuy(self, guy):
        self.__deliveryGuy = guy

    def set_restaurant(self, restaurant):
        self.__restaurant = restaurant

    def set_order(self,item, price):
               self.__contents.append(item)
               self.___orderprices.append(price)
               self.__totalprice += price

    def display(self):
        print(f"Restaurant: {self.__restaurant.get_name()}")
        print(f"Delivery Guy: {self.__deliveryGuy}")
        print(f"Payment Method: {self.__paymentmethod}")
        print(f"Total Price: {self.__totalprice}")
        for i in range(0, len(self.__contents)):
            print(f"{self.__contents[i]}  UGX {self.___orderprices[i]}")

    def update_order(self, status):
        self.__orderStatus = status

    def get_status(self):
        return self.__orderStatus
       
    
class DeliveryPerson(Members):
    def __init__(self, name, address,number,password):
        super().__init__(name, address, number, password)
        self.__Orders =[]

    def set_orders(self, order):
        self.__Orders.append(order)

    def get_orders(self):
        return self.__Orders

    def display(self):
        if len(self.__Orders) == 0:
             print("There are no orders yet")
             return 0
        for i in range(0,len(self.__Orders)):
            print(f"Order {i+1}")
            self.__Orders[i].display()

    def update_order(self):
        from Attempt3 import get_orderno
        orderno = get_orderno()
        newstatus = (input("Please enter status: (delivering / delivered)")).lower()
        status =self.__Orders[orderno-1]
        status.update_order(newstatus)
        if status.get_status() == "delivered":
            self.__Orders.pop(orderno-1)

    
class CashPayment:
    def __init__(self, amount):
        # Encapsulation: Attributes are protected, only accessible through methods in the class
        self._amount = amount
        self._transaction_id = f"TX-{int(datetime.now().timestamp())}"
        self._status = None

    def set_status(self,status):
        self._status = status
    
    def process_payment(self,order):
        total = order.get_total()
        change = self._amount-total
        print(f"Transaction {self._transaction_id} completed with amount UGX {self._amount} \n Your balance is {change}")
        order.update_order("Paid")
        if change >=0:
            self._status = "Complete"

        else:
            self._status = "Pending"

class CreditCardPayment(CashPayment):
    def __init__(self, amount, CVV, CardNo):
        super().__init__(amount)
        self.__CVV = CVV
        self.__cardno = CardNo

    def process_payment(self):
        # 2% fee for credit card payments
        fee = self._amount * 0.02
        self._amount += fee
        print(f"Credit Card processing fee applied. Total amount: UGX {self._amount}")
        self._status = "Complete"

class MobileMoneyPayment(CashPayment):
    def __init__(self, phone_number):
        self._phone_number = phone_number  # Encapsulated attribute for mobile money transactions
        self._otp = None  # Placeholder for OTP

    def process_payment(self,order):
        # Assume a fixed UGX 500 fee for mobile money transactions
        total = order.get_total()
        self._amount =total
        processing_fee = 500
        self._amount += processing_fee
        print(f"Mobile Money processing fee applied. Total amount: UGX {self._amount}")

    def generate_otp(self):
        """Generates an OTP for the transaction."""
        self._otp = random.randint(100000, 999999)
        print(f"OTP sent to {self._phone_number}: {self._otp}")

    def verify_otp(self, entered_otp):
        """Verifies the entered OTP with the generated OTP."""
        return self._otp == entered_otp



