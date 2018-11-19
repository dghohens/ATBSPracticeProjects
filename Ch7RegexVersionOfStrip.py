'''Write a function that takes a string and does the same thing as the strip() string method.
If no other arguments are passed other than the string to strip, then whitespace characters will be removed
from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function
will be removed from the string.
'''

import re

def re_strip(target_string, re_pattern = r'\S.*\S'):
    if re_pattern == r'\S.*\S':
        re_regex = re.compile(r'\S.*\S')
    else:
        re_regex = re.compile('[^%s]' % re_pattern)

    out_list = re_regex.findall(target_string)
    out_string = ''
    for i in out_list:
        out_string += i
    return out_string

print('Enter your string:')
test_string = input()

print('Enter the strip characters, or just hit enter to strip whitespace:')
test_strip = input()

if test_strip == '':
    print(re_strip(test_string))
else:
    print(re_strip(test_string, test_strip))
