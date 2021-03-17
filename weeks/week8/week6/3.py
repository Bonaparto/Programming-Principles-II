a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
a, b = sorted(a), sorted(b)

x = zip(a, b)

#use the tuple() function to display a readable version of the result:

for i in x:
    print(i)