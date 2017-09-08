with open("test.txt", 'a') as jabber:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i*j), file=jabber)
        print("-"*20, file=jabber)