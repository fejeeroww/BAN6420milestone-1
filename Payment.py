from datetime import datetime, timedelta

class Payment:
    def __init__(self, id, policyholder, product, amount, due_date):
        self.id = id
        self.policyholder = policyholder
        self.product = product
        self.amount = amount
        self.due_date = due_date
        self.status = "Pending"
        self.payment_date = None

    def process_payment(self):
        self.status = "Paid"
        self.payment_date = datetime.now()

    def is_overdue(self):
        return datetime.now() > self.due_date

    def apply_penalty(self, penalty_amount):
        self.amount += penalty_amount

    def send_reminder(self):
        print(f"Reminder: Payment of ${self.amount} for {self.product.name} is due on {self.due_date}")

    def display_details(self):
        print(f"Payment ID: {self.id}")
        print(f"Policyholder: {self.policyholder.name}")
        print(f"Product: {self.product.name}")
        print(f"Amount: ${self.amount}")
        print(f"Due Date: {self.due_date}")
        print(f"Status: {self.status}")
        if self.payment_date:
            print(f"Payment Date: {self.payment_date}")
