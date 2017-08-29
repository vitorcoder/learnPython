__author__='dev'
ip =  input("Please input ip adress: ")

print("You entered :" + ip)

if ip[-1] != '.':
    ip += '.'

segCount = 1
segSize = 0
c = ""


for c in ip:
    if c == '.':
        print("Segment {} has size: {}".format(segCount, segSize))
        segCount += 1
        segSize = 0
    else:
        segSize += 1

#codigo necessario se nao tivesse o tratamento de adicionar o ponto no inicio
#if c != '.':
#    print("Segment {} has size: {}".format(segCount, segSize))