def simple_interest(amount,tenure,interest_rate):
    tenure_months = tenure*12
    interest_of_the_prinicpal_amount = amount * tenure_months * interest_rate /100
    final_amount = str(round(interest_of_the_prinicpal_amount))
    print(final_amount+"\\-") 
def compound_interest(amount,tenure,interest_rate):
    principal_amount = amount
    total_amount = amount
    for i in range(1,tenure+1):
        interest_of_the_prinicpal_amount = total_amount * 12 * interest_rate /100
        total_amount += interest_of_the_prinicpal_amount
    final_amount = str((round(total_amount-principal_amount)))
    print(final_amount+"\\-")
def equated_monthly_installment(amount,years_of_tenure,interest_rate):
    principal_amount = amount
    loan_term_months = years_of_tenure * 12
    monthly_interest_rate = interest_rate/ principal_amount  
    emi = principal_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** - loan_term_months)
    print("EMI: " + str(round(emi))+ "\\-")
    

while True:
    user_input = input("Enter r to excute code, or q to quit:  ")
    if user_input.lower() == "r":
        amount = int(input("Prinicpal amount: "))
        
        print("Enter 's' for  simple interest, 'c' for compound interest, 'emi' for EMI")
        Interest_method = input("Enter the method: ").lower()
        if Interest_method == "s":
            years_of_tenure = float(input("Enter the tenure time in years : "))
            print("If interest in percentage then use this formula 'p/12'. Where p is percentage of interest rate")
            interest_rate = float(input("Enter interest rate in rupees only: "))
            simple_interest(amount,years_of_tenure,interest_rate)
        elif Interest_method == "emi":
            years_of_tenure = float(input("Enter the tenure time in years : "))
            print("If interest in percentage then use this formula 'p/12'. Where p is percentage of interest rate")
            interest_rate = float(input("Enter interest rate in percentage: "))
            equated_monthly_installment(amount,years_of_tenure,interest_rate)
        elif Interest_method == "c":
            years_of_tenure = float(input("Enter the tenure time in years : "))
            compound_interest(amount,years_of_tenure,interest_rate)
            print("If interest in percentage then use this formula 'p/12'. Where p is percentage of interest rate")
            interest_rate = float(input("Enter interest rate in rupees only: "))
    elif user_input.lower() == "q":
        break
    else:
        print("Invaild input. Please enter 'r' or 'q'")
    
        
    
