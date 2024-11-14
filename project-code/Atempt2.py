from Attempt1 import Restaurant, OrderingSystem, Customer, DeliveryPerson, CashPayment, CreditCardPayment, MobileMoneyPayment, Order
from Attempt3 import get_name, get_phone_number, get_user_time, get_numItems, customer_name, customer_phone_number, get_resChoice, get_orderno, get_delivery, get_otp, get_cardnum, get_cvv

Mukono = OrderingSystem()

def SettingRestaurants():
    name = get_name()
    address = input("Input address of the restaurant: ")
    number = get_phone_number()
    print("Opening Time")
    openingHours = get_user_time()
    print("Closing Time")
    closingHours = get_user_time()
    password = input("Please input password: ")

    dummyRestaurant = Restaurant(name, address, number, openingHours, closingHours, password)
    print("Step 2: Set your Restaurant Menu")
    num_items = get_numItems()
    dummyRestaurant.menu = num_items
    Mukono.set_restaurants(dummyRestaurant)

def Orderupdate_Restaurant(restaurant):
    value = restaurant.display()
    if value != 0:
        orderno = get_orderno()
        status = input("Please Enter Status: (Approved, Cancelled): ")
        restaurant.update(orderno, status)

def assigndeliverer():
    Mukono.display_Delivery_persons()
    delguyindex = get_delivery()
    delList = Mukono.get_deliver()
    return delList[delguyindex - 1]

def CreatingCustomers():
    name = customer_name()
    address = input("Input your address: ")
    number = customer_phone_number()
    password = input("Please input password: ")
    dummyCustomer = Customer(name, address, number, password)
    Mukono.set_customers(dummyCustomer)
    return dummyCustomer

def Ordering(customer):
    restaurantChoice = get_resChoice()
    customer.display(restaurantChoice)
    noItems = get_numItems()
    order = customer.order(restaurantChoice, noItems)
    paymentmethod = input("Please enter payment method (cash, mobile, card): ").lower()
    order.set_paymentMethod(paymentmethod)

    if paymentmethod == "mobile":
        paymentinfo = process_payment(order)
    elif paymentmethod == "card":
        paymentinfo = card_payment(order)
    elif paymentmethod == "cash":
        paymentinfo = "Pending"
        
    order.set_paymentinfo(paymentinfo)
    restaurantChoice.display()

def process_payment(order):
    number = customer_phone_number()
    dummypayment = MobileMoneyPayment(number)
    dummypayment.process_payment(order)
    dummypayment.generate_otp()
    otpValidation = get_otp(dummypayment)
    
    if otpValidation:
        print("OTP verified successfully.")
        dummypayment.set_status("Paid")
    else:
        print("Incorrect OTP. Transaction failed.")
        dummypayment.set_status("Failed")
        
    return dummypayment

def card_payment(order):
    cardno = get_cardnum()
    cvv = get_cvv()
    amount = order.get_total()
    dummypayment = CreditCardPayment(amount, cvv, cardno)
    dummypayment.process_payment()
    dummypayment.set_status("Paid")
    return dummypayment

def cashpayment(order):
    from Attempt3 import get_amount
    amount = get_amount()
    dummypayment = CashPayment(amount)
    dummypayment.process_payment(order)

def CreateDeliveryGuy():
    name = customer_name()
    address = input("Input your address: ")
    number = customer_phone_number()
    password = input("Please input password: ")
    dummyDeliver = DeliveryPerson(name, address, number, password)
    Mukono.set_deliver(dummyDeliver)

def menu0():
    print("Which are you? \n- Restaurant\n- Customer\n- Delivery")
    print("enter 'exit' to exit")
    answer = (input("Please enter your choice: ")).lower()
    return answer

def menu1():
    print("Menu \n- Login\n- Signup\n- Exit")
    answer = (input("Please enter your choice: ")).lower()
    return answer

def menu2():
    print("Menu \n- D to display Orders\n-U to update order status\n- E to exit")
    answer = (input("Please enter your choice: ")).lower()
    return answer

def menu3():
    print("Menu \n- order to Make an order\n- track to Track an order\n- exit to exit")
    answer = (input("Please enter your choice: ")).lower()
    return answer

def menu4():
    print("Menu \n- view to view orders\n- update to update orders\n- pay to record cash payment \n- exit to exit")
    answer = (input("Please enter your choice: ")).lower()
    return answer

def Login(memberlist):
    
    name = input("Please enter your Name: ").lower()
    password = input("Please enter your password: ")
    
    for i in range(len(memberlist)):
        resName = memberlist[i].get_name()
        if resName == name:
            resPass = memberlist[i].get_password()
            if resPass == password:
                print("You have Successfully logged in")
                return memberlist[i]
            else:
                print("Invalid password")
                answer=input("If you want to exit enter 'exit' else enter any key: ")
                if answer == "exit":
                    return exit
                else:
                    return Login(memberlist)
            
    print("The name entered is invalid\n")
    answer=(input("If you want to exit enter 'exit' else enter any key: ")).lower()
    if answer == "exit":
        return "exit"
    else:
        return Login(memberlist)