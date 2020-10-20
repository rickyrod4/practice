#Print and Count
def print_count():
    count = 0
    for i in range(1,256):
       print(i)
#print_count()


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
    a = 1
    arr = []
    while n>0:
        print(n)
        arr[a] = n
        a += 1
        n -= 1
    return arr

#print(countdown(5))

def oddNumbers():
    for i in range(1,1001):
        if i % 2 != 0:
            print(i)

#oddNumbers()

def printSum():
    sum = 0
    for i in range(1,5001):
        if i % 2 != 0:
            sum += i

    print(sum)
#printSum()

def iterateArray(arr):
    for item in arr:
        print(item)

#iterateArray([2,4,6,8])

def findMax(arr):
    max = arr[0]

    for item in arr:
        if item > max:
            max = item
    return max

#print(findMax([2,8,6,14,5]))

def average(arr):
    sum = 0
    for item in arr:
        sum += item
    average = sum / len(arr)
    return average
#print(average([2,4,6,8,10]))

def oddArray():
    array = []
    for i in range(1, 256):
        if i % 2 != 0:
            array.append(i)

    print(array)
#oddArray()

def greaterThanY(arr, num):
    newArray = []
    for item in arr:
        if item > num:
            newArray.append(item)
    print(len(newArray))

#greaterThanY([2,4,6,8,10,12,45,485,212], 8)

