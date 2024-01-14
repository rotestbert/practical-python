# mortgage.py
#
# Exercise 1.7

# base payment scheme
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
# extra payment
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month = month + 1
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    if principal < 0:
        negative_principal = principal
        print("In the last month overpaid by / pay less with", negative_principal)
        total_paid = total_paid + negative_principal
        principal = 0

    print("Month: ", month, end='  '), print("Total paid: ", round(total_paid, 2), end='  '), \
        print("Remaining principal: ", round(principal, 2))

print('Total paid', round(total_paid, 8)), print("Total months: ", month)
