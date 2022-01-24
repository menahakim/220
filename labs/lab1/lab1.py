
def calc_monthly_interest():

    annual = eval(input("Enter Annual Interest Rate"))
    numberofdays = eval(input("Enter the number of days in the billing cycle"))
    previousnet = eval(input("Enter the previous net balance"))
    paymentamount = eval(input("Enter the payment amount"))
    daypaymentmade = eval(input("Enter the day of the billing cycle in which the payment was made"))

    stepone = numberofdays * previousnet

    steptwo = paymentamount * (numberofdays - daypaymentmade)

    stepthree = stepone - steptwo

    avgdaily = stepthree / numberofdays

    monthlyrate = annual / 12 / 100

    monthlycharge = avgdaily * monthlyrate

    print("Total monthly charge is", monthlycharge)
