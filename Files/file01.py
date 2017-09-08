#jabber = open("test.txt", 'r')

#for line in jabber:
#    print(line)
    
#jabber.close;

#safer way to open files. "with" keyword will close the file when resource is no longer needed

with open("test.txt", 'r') as jabber:
    for line in jabber:
        print(line, end="")
# end parameter allows changing the last char. Default is to append a new line char. 
# In this case, each line in files already has a new line char, so we do this to avoid having double new lines


