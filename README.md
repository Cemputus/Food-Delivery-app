
# Food Delivery Service App

The **Food Delivery Service App** is a Python-based command-line application that facilitates restaurant management, customer ordering, and delivery tracking. With three main user roles—**Restaurant**, **Customer**, and **Delivery Person**—the app provides an interactive platform for placing and managing food orders seamlessly.

## Features

- **Restaurant Functionality**:
  - Restaurant registration and login.
  - Set up a custom menu with item prices.
  - Manage order status and track incoming orders.

- **Customer Functionality**:
  - Customer registration and login.
  - Browse available restaurants and menus.
  - Place orders and select payment methods (Cash, Mobile Money, Credit Card).
  - Track order status in real-time.

- **Delivery Person Functionality**:
  - Delivery person registration and login.
  - View assigned orders and update delivery status.
  - Record cash payments upon order delivery.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Cemputus/Food-Delivery-app.git
   cd - Food-Delivery-app
   ```

2. **Dependencies**:
   The app only requires Python 3.6+; it uses the standard library and does not rely on external dependencies.

## Usage

1. **Start the App**:
   Run the app from the command line:
   ```bash
   python main.py
   ```

2. **Choose a User Role**:
   When prompted, select your role as **Restaurant**, **Customer**, or **Delivery Person** to begin interacting with the app.

## Example Scenario

Here’s a typical flow demonstrating how the app can be used:

1. **Restaurant** registers and sets up their menu.
2. **Customer** registers, browses the menu, places an order, and selects a payment method.
3. **Delivery Person** views the order, delivers the items, and updates the order status.
4. **Customer** can track their order status from pending to delivered.

For a detailed scenario, please refer to the [Detailed Scenario](https://github.com/Cemputus/Food-Delivery-app/blob/main/Food_Delivery_System_Scenario.pdf) section below.

---

## Detailed Example Scenario

### 1. Restaurant Setup
   - **Signup** and enter details (e.g., name, address, hours).
   - Create a menu with items like `Spaghetti Carbonara` and `Lasagna`.

### 2. Customer Ordering
   - **Signup**, browse restaurants, select items, and choose a payment method.
   - Enter an OTP for mobile payment or card details for card payments.

### 3. Delivery Process
   - View assigned orders, mark the status, and confirm cash payments if applicable.

---

## Functions and Code Structure

- **`SettingRestaurants`**: Allows restaurants to register and set up their menu.
- **`CreatingCustomers`**: Allows customers to register.
- **`Ordering`**: Allows customers to browse menus, place orders, and choose payment methods.
- **`Orderupdate_Restaurant`**: Lets restaurants update order statuses.
- **`process_payment`, `card_payment`, `cashpayment`**: Process payments via different methods.
- **`Login`**: Common login function for all roles.
- **Menus**: `menu0`, `menu1`, `menu2`, `menu3`, `menu4` control the interface for each user role.

For full code usage, see the `Attempt1.py`, `Attempt2.py`, and `Attempt3.py` modules containing core functions and helper methods.

---

## Project Structure

```
restaurant-delivery-app/
│
├── Attempt1.py             # Core classes and models (e.g., Customer, Order, Payment)
├── Attempt2.py             # OrderingSystem and supporting methods
├── Attempt3.py             # Helper functions for user input validation
├── main.py                 # Main script to run the app interface
└── README.md               # Documentation
```

---




## Contact

For any questions, please reach out to **[Emmanuel Nsubuga](mailto:ensubuga019@gmail.com.com)**.

---
