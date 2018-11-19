'''Write a function that uses regular expressions to make sure the password string it is passed is strong.
A strong password is defined as one that is at least eight characters long, contains both uppercase
and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns
to validate its strength.
'''

import re

def strength_check(password):
    upper_regex = re.compile(r'[A-Z]')
    lower_regex = re.compile(r'[a-z]')
    num_regex = re.compile(r'\d')

    check_upper = upper_regex.search(password)
    check_lower = lower_regex.search(password)
    check_num = num_regex.search(password)

    if len(password) < 8:
        print('Your password is too short! Please enter a password 8 characters or longer.')
    if check_upper == None or check_lower == None:
        print('Your password must contain both upper and lower case letters! Please try again.')
    if check_num == None:
        print('Your password must contain ast least one number! Please try again.')
    else:
        print("Your password passed all the checks! Now you won't get hacked!")
    pass

print('Please enter a password:')
passwd = input()
strength_check(passwd)