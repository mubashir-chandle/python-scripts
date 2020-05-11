# 2020-05-11


'''Calculate the number of months required to pay off a loan.'''


loan_amount = 10_000
interest_rate = 0.12    # 12% interest rate.
monthly_payment = 500

balance = loan_amount   # Remaining loan amount
months_required = 0

while balance > 0:
    # Calculate monthly interest amount
    interest_amount = (interest_rate * balance) / 12

    balance += interest_amount
    balance -= monthly_payment

    balance = round(balance, 2)
    if balance < 0:
        balance = 0

    months_required += 1
    print(f'Month {months_required}: {balance}')

print(f'Total months required to pay off loan: {months_required}')
