"""
--Problem 3 - Using Bisection Search to Make the Program Faster--
How can we calculate a more accurate fixed monthly payment than we did in Problem 2? We can
make this program run faster using a technique introduced in lecture - bisection search!

To recap: we are searching for the smallest monthly payment such that we can pay off the
entire balance within a year. What is a reasonable lower bound for this payment value ? $0 is
the obvious answer, but you can do better than that. If there was no interest, the debt can be
paid off by monthly payments of one-twelfth of the original balance, so we must pay at least
this much every month. One-twelfth of the original balance is a good lower bound.

What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire
balance at the end of the year. What we ultimately pay must be greater than what we would have
paid in monthly installments, because the interest was compounded on the balance we didn't pay
off each month. A good upper bound for the monthly payment would be one-twelfth of the balance,
after having its interest compounded monthly for an entire year.

Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search to find the smallest monthly payment,
to the cent, to pay off the debt within a year. Produce the same return value as you did in
Problem 2.

Pre-defined Variables:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt
in under 1 year.

"""
#Code
initBalance = balance
monthlyInterestRate = annualInterestRate / 12.0
lowerBound = balance / 12
upperBound = (balance * ((1 + monthlyInterestRate) ** 12)) / 12.0
minMonthlyPayment = (lowerBound + upperBound) / 2.0
epsilon = .01

def calculate(balance, monthlyInterestRate, minMonthyPayment, month):
    month = 0
    while month < 12:
        unpaidBalance = balance - minMonthlyPayment
        updatedBalance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        balance = updatedBalance
        month += 1
    return balance

while abs(balance) >= epsilon:
    month = 0
    balance = initBalance
    balance = calculate(balance, monthlyInterestRate, minMonthlyPayment, month)
    if balance > 0:
        lowerBound = minMonthlyPayment
    else:
        upperBound = minMonthlyPayment
    minMonthlyPayment = (lowerBound + upperBound) / 2.0   
    
minMonthlyPayment = round(minMonthlyPayment,2)

print ("The lowest monthly payment is: " + str(minMonthlyPayment))