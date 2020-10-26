#Bubble sort

arr = [7,1,6,5,3,2,4,9,0,8]

def bubbleSort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr
#print(bubbleSort(arr))

#selection Sort

def selectionSort(arr):
    print(arr)
    for j in range(len(arr)-1):
        min = arr[j]
        print('----------------', 'iteration', j)
        print('min = ', min)
        for i in range(j+1,len(arr)):
            print('checking', arr[i], 'at index:', i)
            if arr[i] < min:
                min = arr[i]
                min_index = i
            print('new Minimum:', min)
        if arr[j] != min:
            arr[j], arr[min_index] = arr[min_index], arr[j]
            print('swapped', arr[j], 'and', arr[min_index])
            print(arr)
        else:
            print('Next value in the correct spot')
    print('Final Array:', arr)
selectionSort(arr)