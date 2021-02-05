def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        smaller = [i for i in arr[1:] if i <= pivot]
        larger = [i for i in arr[1:] if i > pivot]
        return quickSort(smaller) + [pivot] + quickSort(larger)