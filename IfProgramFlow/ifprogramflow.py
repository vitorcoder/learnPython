__author__='dev'
age =  int(input("How old are you? "))
print(age)

#if (age >=18) and (age <=65):
if 18 <= age <= 65:
    print("Go to work!")
else:
    print("Please come back in {0} years!".format(18 - age))