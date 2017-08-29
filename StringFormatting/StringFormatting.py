__author__='dev'
age = 34
print ("My age is " + str(age) + " years")

print ("My age is {0} years".format(age))

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))