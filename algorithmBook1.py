#Print and Count
def print_count():
    count = 0
    for i in range(512,4096):
        if i % 5 == 0:
            print(i)
            count += 1
            print('Current Count:', count)

def multiplesOfSix():
    #print multiples of 6 using a WHILE loop
    i = 0
    while i < 60000:
        if i % 6 == 0:
            print(i)

        i += 1

def notAllMultiplesOfThree():
    for i in range(-300,1):
        if i % 3 == 0:
            if i == -3 or i == -6:
                pass
            else:
                print(i)

notAllMultiplesOfThree()