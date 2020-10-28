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