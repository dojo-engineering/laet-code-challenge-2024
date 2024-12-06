class Payment:
    def __init__(self, amount, date, method, status):
        self.amount = amount
        self.date = date
        self.method = method
        self.status = status

payments_data = [
    Payment(100, "2021-01-01", "Paypal", "Success"),
    Payment(100, "2021-01-01", "Paypal", "Failed"),
    Payment(100, "2021-01-01", "Paypal", "Success"),
    Payment(100, "2021-01-01", "Paypal", "Success"),
    Payment(100, "2021-01-01", "Paypal", "Success"),
    Payment(100, "2021-01-01", "Paypal", "Success"),
    Payment(100, "2021-01-01", "Paypal", "Success"),
    Payment(100, "2021-01-01", "Paypal", "Success"),
]