def count_of_lowercase_and_uppercase_letters(arg_1):
    # Complete this function
    count_of_uppercase=0
    count_of_lowercase=0
    for i in arg_1:
        if i.isupper():
            count_of_uppercase+=1
        else: 
            count_of_lowercase+=1
    print(count_of_uppercase)
    print(count_of_lowercase)


word = input()
# Call the count_of_lowercase_and_uppercase_letters function
count_of_lowercase_and_uppercase_letters(arg_1=word)

"""
input:MasTer
output:
2
4
"""
