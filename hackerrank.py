def sockMerchant(n, arr):
    #iterate thru the array
    pairs = 0
    #Sort The Array
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    i = 0 
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            pairs += 1
            i += 1
        i += 1

    return pairs
sockMerchant(9,[10,20,20,10,10,30,50,10,20])

def jumpingOnClouds(c):
    i = 0
    jumps = 0 
    while i < len(c):
        if i == len(c)-1:
            break
        elif i+1 == len(c)-1 or i+2 == len(c)-1:
            jumps += 1
            break
        if c[i+1] == 1:
            jumps += 1
            i += 2
        elif c[i+1] == 0:
            jumps += 1
            if c[i+2] == 0:
                i+=2
            else:
                i+=1
    return jumps
jumpingOnClouds([0,0,1,0,0,1,0])

import math
def repeatedString(s, n):
    #I must create the infinite string to the number n
        #divide n by len(s) multiply
    mult = math.floor(n/len(s))
    remainder = n % len(s)
    a_count = s.count('a')
    a_count = a_count * mult
    if remainder != 0:
        for i in range(remainder):
            if s[i] == 'a':
                a_count += 1
    #make an 'a' count variable
    #loop thru the string
    #if 'a' is in the string add 1 to the count
    return a_count


repeatedString('abab', 10)

word = 'hello'
for letter in word:
    print(letter)