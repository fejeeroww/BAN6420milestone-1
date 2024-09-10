# BAN6420milestone-1
# Insurance Policy Management System

A simple Python-based insurance policy management system that allows policy managers to manage policyholders, products, and payments.

## Features of this python based system

- Create and manage policyholders
- Create and manage insurance products
- Process payments and send reminders
- Suspend and reactivate policyholders
- Update product details

## File Structure

- `policyholder.py`: Contains the Policyholder class
- `product.py`: Contains the Product class
- `payment.py`: Contains the Payment class
- `main.py`: Demonstrates the functionality of the system

## Classes

### Policyholder

- Attributes: id, name, email, phone, status, registration_date, products
- Methods: suspend(), reactivate(), add_product(), remove_product(), display_details()

### Product

- Attributes: id, name, description, price, status
- Methods: update(), suspend(), reactivate(), display_details()

### Payment

- Attributes: id, policyholder, product, amount, due_date, status, payment_date
- Methods: process_payment(), is_overdue(), apply_penalty(), send_reminder(), display_details()

## Using the system

1. Ensure you have Python 3.x installed on your system.
2. Run the `main.py` file to display the system's functionality
