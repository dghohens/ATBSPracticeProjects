'''Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table
with each column right-justified. Assume that all the inner lists will contain the same number of strings.
For example, the value could look like this:


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
Your printTable() function would print the following:


  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
Hint: Your code will first have to find the longest string in each of the inner lists so that the whole column
can be wide enough to fit all the strings. You can store the maximum width of each column as a list of integers.
The printTable() function can begin with colWidths = [0] * len(tableData), which will create a list containing
the same number of 0 values as the number of inner lists in tableData. That way, colWidths[0] can store the width
of the longest string in tableData[0], colWidths[1] can store the width of the longest string in tableData[1],
and so on. You can then find the largest value in the colWidths list to find out what integer width
 to pass to the rjust() string method.
'''

def printTable(list_of_lists):
    z = 0
    for i in list_of_lists:
        for j in i:
            if len(j) > z:
                z = len(j)
    for x in list_of_lists:
        print()
        for y in x:
            if len(y) < z:
                print((' ' * (z - len(y))) + y, end=' ')
            else:
                print(y, end=' ')
    pass


def printTable2(list_of_lists):
    z = 0
    for i in list_of_lists:
        for j in i:
            if len(j) > z:
                z = len(j)
    for x in list_of_lists:
        print()
        for y in x:
            print(y.rjust(z), end = ' ')
    pass


def printTable3(list_of_lists):
    z = 0
    for i in list_of_lists:
        for j in i:
            if len(j) > z:
                z = len(j)
    for i in range(len(list_of_lists[0])):
        print()
        for j in range(len(list_of_lists)):
            print(list_of_lists[j][i].rjust(z), end = ' ')
    pass

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
print()
printTable2(tableData)
print()
printTable3(tableData)