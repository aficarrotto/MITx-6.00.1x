"""
--Problem 2 - Paying Debt off in a Year--
Write a program that calculates the minimum fixed monthly payment needed in order pay off a
credit card balance within 12 months. By a fixed monthly payment, we mean a single number
which does not change each month, but instead is a constant amount that will be paid each
month.

Pre-defined Variables:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal


The program should print out one line: the lowest monthly payment that will pay off all debt
in under 1 year.

"""
#Code
monthlyInterestRate = annualInterestRate / 12.0
minFixedMonthlyPayment = 10

def calculate(balance, monthlyInterestRate):
    month = 1
    while month <= 12:
        unpaidBalance = balance - minFixedMonthlyPayment
        updatedBalance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        balance = updatedBalance
        month += 1
    return balance

while calculate(balance,monthlyInterestRate) > 0:
    minFixedMonthlyPayment += 10
    calculate(balance,monthlyInterestRate)
    
print ("The lowest monthly payment is: " + str(round(minFixedMonthlyPayment,2)))