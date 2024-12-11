from typing import List
from .payments_data import Payment

# This function calculates the total amount of a list of payments
# Hold the command key and click on "[Payment]" below to see the properties available on payment objects
# Think about whether you want to include all payments in this sum or only certain ones
def calculateTotalTakings(payments: List[Payment]):
    # Return a number
    return 0

# This function calculates the total amount of all payments with a refunded status
def calculateRefunds(payments: List[Payment]):
    # Return a number
    return 0

# This function returns a list of payments that were made today
# Payment dates are in ISO date format and you can turn this into a Python date using `date.fromisoformat`
def todaysPayments(payments: List[Payment]):
    # Return a list of payments
    return payments

# This function returns a list of payments that were made yesterday
def yesterdaysPayments(payments: List[Payment]):
    # Return a list of payments
    return payments

# This function returns a list of payments that were made in the past seven days
def thisWeeksPayments(payments: List[Payment]):
    # Return a list of payments
    return payments

# This function returns a list of payments that match the search input and the status filter
# The 'search' parameter is a string
# The 'status' parameter is a string
def searchPayments(payments: List[Payment], search: str, status: str):
    # Return a list of payments
    return payments

# This function returns a new list of payments that are sorted by the payment date
def sortPaymentsByDate(payments: List[Payment]):
    # Return a list of payments
    return payments

# This function changes the status of a payment with an id matching the 'id' parameter to "Refunded"
def refundPayment(payments: List[Payment], id: str):
    # Don't return anything
    return