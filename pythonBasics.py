#a = int(input('Enter number a:'))
#b = int(input('Enter number b:'))
#print('The sum of a and b is:', (a+b))

array = [0,2,4,6,8]

print(array)
#print(array[2])

#for item in array:
 #   print(item)

#for i in range(100,10,-10):
    #print(i)


#Given an integer array return the sum of the values in that array
def sumArray(arr):
    print('This is the Original Array:', arr)
    sum = 0
    for item in arr:
        sum = sum + item

    return sum



print(sumArray([1,2,3,4]))
print('-------------------------')

#Given an array reverse the order
def reverseArray(arr):
    pass

