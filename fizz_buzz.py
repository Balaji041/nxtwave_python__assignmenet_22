def fizz_buzz(number):
    # Complete this function

    if number%3==0:
        return "Fizz"
    elif number%5==0:
        return "Buzz"
    elif number%5==0 and number%3==0:
        return "FizzBuzz"
    else:
        return number
number = int(input())
# Call the fizz_buzz function
print(fizz_buzz(number))

"""
input:20
output:Buzz

"""
