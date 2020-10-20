#Print and Count
def print_count():
    count = 0
    for i in range(1,256):
       print(i)
print_count()


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

#notAllMultiplesOfThree()


def printAndReturn(arr):
    if len(arr) >2:
        tooBig = "This array is too big. Please input an array of length 2"
        return tooBig

    print(arr[0])
    return arr[1]

#printAndReturn([0,5])


def countdown(n):
    a = 0
    arr = []
    while n>0:
        print(n)
        arr[a] = n
        a += 1
        n -= 1
    return arr

print(countdown(5))