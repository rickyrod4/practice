#Bubble sort

arr = [70,1,61,55,32,22,24,29,20,28]

def bubbleSort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr
#print(bubbleSort(arr))
#-----------------------------------------------------------------------------------------
#selection Sort
def selectionSort(arr):
    print(arr)
    for j in range(len(arr)-1):
        min = arr[j]
        for i in range(j+1,len(arr)):
            if arr[i] < min:
                min = arr[i]
                min_index = i
        if arr[j] != min:
            arr[j], arr[min_index] = arr[min_index], arr[j]
    print('Final Array:', arr)
#selectionSort(arr)

#--------------------------------------------------------------------------------------------------------------------

#insertion sort
# iterate a for loop
# iterate a reverse for loop
def insertionSort(arr):
    pass