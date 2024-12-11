from typing import List
from .payments_data import Payment

# Hold the command key and click on "[Payment]" below to see the properties available on payment objects
Payment

# This function takes a list of payments and returns a number to show for the Total Takings on the website
def calculateTotalTakings(payments: List[Payment]):
    # Return a number
    return 0

# This function takes a list of payments and returns a number to show for the Total Refunds on the website
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