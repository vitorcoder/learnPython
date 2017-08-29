__author__='dev'
name=input("What's your name?")
age=int(input("{0} , what's your age? ".format(name)))

#if (age >=18) and (age <=65):
if 18 <= age <= 30:
    print("{0}, enjoy your Holiday!".format(name))
else:
    print("Sorry, you got no holiday!")