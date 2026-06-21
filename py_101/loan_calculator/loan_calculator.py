def prompt(message):
    print(f"{message}")

def invalid_number(number_str):
    try:
        int(number_str)
        float(number_str)
    except ValueError:
            return True

    return False 

prompt("Welcome to The Loan Calculator!")

prompt("Please enter the amount of the loan:")
loan_entry = input()

while invalid_number(loan_entry):
    prompt(" Hmm.. that doesn't look like a valid number. Please try again.")
    loan_entry = input()

loan_amount = int(loan_entry)

 # print(type(loan_amount))

prompt(f' Your loan amount is ${loan_amount}')

prompt("Now, please enter your APR. You can enter as a decimal,such as 12.5")
apr_entry = (float(input())

while invalid_number(apr_entry):
    prompt("Hmm.. that doesn't look like a mumber. Please try again.")
    apr_entry = input()

apr = (float(apr_entry)/ 100)

monthly_interest_rate = (apr/12)


prompt(f' Your interest rate is {apr:.1%}')

prompt(f' Finally, How many years will your loan be for?')

loan_duration_entry = input()

while invalid_number(loan_duration_entry):
    prompt("Hmm.. that doesn't look like a mumber. Please try again.")
    loan_duration_entry = input()

loan_duration = (int(loan_duration_entry)*12)

monthly_payment = loan_amount * (monthly_interest_rate/(1 -(1 +
monthly_interest_rate) ** (-loan_duration)))
    
prompt(f' Your payment will be ${monthly_payment:.3} per month.')
