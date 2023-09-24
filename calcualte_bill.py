def calculate_bill(amount):
    # Complete this function
    if amount<500:
        return (amount-(amount*0.05))
    elif amount>=500 and amount<=2500:
        return (amount-(amount*0.10))
    else:
        return (amount-(amount*0.20))

amount = int(input())
# Call the calculate_bill function
print(calculate_bill(amount))

"""
input:250
output:237.5

"""
