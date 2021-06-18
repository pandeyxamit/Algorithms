def selectionSort(arr):
    sortedArray = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        sortedArray.append(arr.pop(smallest))
    return sortedArray

def findSmallest(arr):
    smallestIndex = 0
    for i in range(1, len(arr)):
        if arr[smallestIndex] > arr[i]:
            smallestIndex = i
    return smallestIndex    
        