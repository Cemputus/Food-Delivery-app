from Attempt1 import Restaurant, OrderingSystem, Customer, DeliveryPerson, CashPayment, CreditCardPayment, MobileMoneyPayment, Order
from Attempt3 import get_name, get_phone_number, get_user_time, get_numItems, customer_name, customer_phone_number, get_resChoice, get_orderno, get_delivery, get_otp, get_cardnum, get_cvv
from Atempt2 import *
# Interface loop
app = True
while app:
    print("Welcome to The Restaurant Delivery Service App")
    answer = menu0()
    
    if answer == "restaurant":
        while True:
            choice = menu1()
            if choice == "signup" or choice =="Signup":
                SettingRestaurants()
            elif choice == "login":
                restaurant = Login(Mukono.get_restaurants())
                while restaurant != "exit":
                    choice = menu2()
                    if choice == "d":
                        restaurant.display()
                    elif choice =="u":
                        Orderupdate_Restaurant(restaurant)
                    elif choice == "e":
                        break
                    else:
                        print("Invalid Input\n")
            elif choice == "exit":
                break
            else:
                print("Invalid Input\n")
                
    elif answer == "customer":
        while True:
            choice = menu1()
            if choice == "signup":
                CreatingCustomers()
            elif choice == "login":
                customer = Login(Mukono.get_customer())
                while customer != "exit":
                    choice = menu3()
                    if choice == "order":
                        Ordering(customer)
                    elif choice == "track":
                        myorderlist = customer.get_orderHist()
                        myorder = myorderlist[-1]
                        print(f"Status: {myorder.get_status()}")
                    elif choice == "exit":
                        break
                    else:
                        print("Invalid Input\n")
            elif choice == "exit":
                break
            else:
                print("Invalid Input\n")
                
    elif answer == "delivery":
        while True:
            choice = menu1()
            if choice == "signup":
                CreateDeliveryGuy()
            elif choice == "login":
                delivery_person = Login(Mukono.get_deliver())
                while delivery_person != "exit":
                    choice = menu4()
                    if choice == "view":
                        delivery_person.display()
                    elif choice == "update":
                        delivery_person.update_order()

                    elif choice == "pay":
                        orderno = get_orderno()
                        orders = delivery_person.get_orders()
                        order = orders[orderno-1]
                        cashpayment(order)

                    elif choice == "exit":
                        break
                    else:
                        print("Invalid Input\n")

            elif choice == "exit":
                break

            else:
                print("Invalid Input\n")
    elif answer == "exit":
        break
    else:
        print("Invalid Input \n")