from datetime import datetime

def get_content(myOrder, menu):
    from Attempt1 import Order, Customer
    content =input("Enter Item: ").lower()
    if content in menu:
            price = menu[content]
            myOrder.set_order(content,price)
    else:
            print("Invalid input")
            get_content(myOrder,menu)

def get_name():
    from Atempt2 import Mukono
    from Attempt1 import Restaurant, Members
    restaurant_name =input("Please Enter the restaurant Name: ").lower()
    for restaurant in Mukono.get_restaurants():
        if restaurant_name == restaurant.get_name():
            print("Restaurant already exists")
            get_name()
    return restaurant_name
   

def get_user_time():
    while True:
        user_input = input("Enter the time (HH:MM) in 24hr notation: ")
        try:
            # Convert input to a time object
            user_time = datetime.strptime(user_input, "%H:%M").time()
            return user_time
        except ValueError:
            print("Invalid format. Please enter time in HH:MM format.")

def get_phone_number():
    while True:
        phone_number = input("Enter your phone number start with 256: ")
        
        # Check if the input is all digits and has the correct length
        if phone_number.isdigit() and len(phone_number) == 12:  # Assuming a 10-digit phone number
            return phone_number
        else:
            print("Invalid phone number. Please enter a 12-digit number.")


def get_numItems():
    try:
        num_items = int(input("Enter number of items: "))
        if num_items <= 0:
            print("Please enter a positive integer greater than zero.")
            return get_numItems()
        else:
            return num_items
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_numItems()

def get_price(item):    
    try:    
            price = round(float(input(f"Input price for {item}: ")), 2)
            # Check if the price is non-negative
            if price < 0:
                print("Price cannot be negative. Please enter a valid price.")
                get_price(item)
            else:
                return price  # Exit the loop if the input is valid

    except ValueError:
            print("Invalid input. Please enter a numeric value.")
            get_price(item)

def customer_name():
    from Atempt2 import Mukono
    from Attempt1 import Customer,Members
    customer_name =input("Please Enter your Name: ").lower()
    for customer in Mukono.get_customer():
        if customer_name == customer.get_name():
            print("Restaurant already exists")
            customer_name()
    return customer_name

def customer_phone_number():
    while True:
        phone_number = input("Enter your phone number start with 256: ")
        
        # Check if the input is all digits and has the correct length
        if phone_number.isdigit() and len(phone_number) == 12:  # Assuming a 10-digit phone number
            return phone_number
        else:
            print("Invalid phone number. Please enter a 12-digit number.")

def get_resChoice():
    from Atempt2 import Mukono
    from Attempt1 import Restaurant, Members
    print("Restaurants Available")
    Mukono.display_restaurants()
    from Atempt2 import Mukono
    restaurants = Mukono.get_restaurants()
    choice = (input("Please enter the Restaurant of your choice: ")).lower()
    for restaurant in restaurants:
        if choice == restaurant.get_name():
            return restaurant
    print("Invalid Input")
    return get_resChoice()

def get_orderno():
    try:
        orderno = int(input("Please enter Order Number"))
        if orderno <= 0:
            print("Please enter a positive integer greater than zero.")
            return get_orderno()
        else:
            return orderno
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_orderno()


def get_delivery():
    try:
        orderno = int(input("Please enter index of delivery guy: "))
        if orderno <= 0:
            print("Please enter a positive integer greater than zero.")
            return get_delivery()
        else:
            return orderno
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_delivery()

def get_otp(payment):
    # Step 2: Prompt user to enter the OTP
    from Attempt1 import MobileMoneyPayment
    try:
            entered_otp = int(input("Enter the OTP sent to your phone: "))
            return payment.verify_otp(entered_otp)
    except ValueError:
            print("Invalid OTP format. Transaction failed.")
            payment._status = "Failed"
            return get_otp(payment)
    
def get_cardnum():
    try:
        cardno = int(input("Please Enter Card Number: "))
        if len(str(cardno)) < 16:
             print("Invalid Card Number")
             return get_cardnum()
    except ValueError:
            print("Invalid card number.")
            return get_cardnum()
    
def get_cvv():
    try:
        cvv = int(input("Please Enter Card Number: "))
        if len(str(cvv)) < 3:
             print("Invalid Card Number")
             return get_cvv()
    except ValueError:
            print("Invalid card number.")
            return get_cvv()
    
def get_amount():
    try:
          amount = round(float(input("Please enter paid amount (UGX): ")),2)
          if amount<=0:
               print("Invalid Amount")
               return get_amount()
          else: 
               return amount
          
    except ValueError:
         print("Invalid input, Enter Integer or Floating Point Number")
         return get_amount()
