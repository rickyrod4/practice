#Bubble sort

arr = [1,5,3,2,0,8]

def bubbleSort(arr):
    for i in range(len(arr)):
        print('index', i, 'value', arr[i])
        print('comparing', arr[i], arr[i+1])
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]


bubbleSort(arr)