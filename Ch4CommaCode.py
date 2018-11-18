'''Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns a string with all the items separated by a comma
and a space, with and inserted before the last item. For example, passing the previous spam list to the function would
return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.
'''

def list_to_string(inlist):
    outstring = ''
    for i in range(len(inlist)):
        if i == len(inlist) - 1:
            outstring += 'and ' + str(inlist[i])
        else:
            outstring += str(inlist[i]) + ', '
    return outstring

test_list = [1, 'a', 1.001, 'spam']
print(list_to_string(test_list))