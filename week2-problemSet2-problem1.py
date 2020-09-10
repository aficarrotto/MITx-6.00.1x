"""
--Problem 1 - Paying Debt off in a Year--
Write a program to calculate the credit card balance after one year if a
person only pays the minimum monthly payment required by the credit card
company each month.

Pre-defined Variables:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining
balance. At the end of 12 months, print out the remaining balance. Be sure
to print out no more than two decimal digits of accuracy.

"""
#Code
month = 1

while month <= 12:
    monthlyInterestRate = annualInterestRate / 12.0
    minMonthlyPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minMonthlyPayment
    updatedBalance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
    balance = updatedBalance
    month += 1

print ("The remaining balance is: " + str(round(balance,2)))
