def binary_search_iter(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:    
        mid = low + (high - low) // 2
        guess = arr[mid]
        if guess == item:
            return "Item {} found at index {} in the array after {} iteration.\n".format(item, mid, iteration)
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return "Item not present in the array.\n"
