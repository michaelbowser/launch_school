print("Welcome to The Loan Calculator!") 
print("Please enter the dollar amount of the loan")

loan_amount_entry = input ()
loan_amount = int(loan_amount_entry)

print(f' Your loan amount is ${loan_amount}')
print("Now, please enter your APR. You can enter as a decimal,such as 12.5")

apr_entry = input()
apr = (float(apr_entry)/ 100)

monthly_interest_rate = (apr/12)


print(f' Your interest rate is {apr}%')

print (f' Finally, How many years will your loan be for?')

loan_duration_entry = input()
loan_duration = (int(loan_duration_entry)*12)

monthly_payment = loan_amount * (monthly_interest_rate/(1 -(1 +
monthly_interest_rate) ** (-loan_duration)))
    
print(f' Your payment will be ${monthly_payment} per month.')
