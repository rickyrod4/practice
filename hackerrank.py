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