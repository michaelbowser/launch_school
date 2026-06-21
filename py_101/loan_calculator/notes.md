
### Build a loan calculator. It will have three inputs 
### and two outputs.

### Inputs:
#### loan amount
#### the annual percentage rate (APR)
#### the loan duration

### Outputs:
#### Internal monthly interest rate (apr/12)
####  Internal loan duration in months 
####  External monthly payment in dollar and cents format ie. $20.42 

### Formula

#### m = p * (j / (1 - (1 + j) ** (-n)))

### Questions:
#### Should interest rate be in ints or floats
#### 

### Pseudocode:
Start 

Print Welcome to Loan calculator! Please enter the loan amount:
loan_amount = get user input 

Print Now, what is your Annual Percentage Rate (APR):
apr = get user input

Print Finally, how many years will this be for?:
loan_duration = get user input

monthly_interest_rate = apr/12

loan_duration_in_months = (loan_duration/12)

monthly_payment = loan_amount * (monthly_interest_rate/(1- (1 + monthly_interest_rate) ** (-loan_duration_in_months)))

print Your monthly payment will be {monthly_payment}

 
### Notes 


