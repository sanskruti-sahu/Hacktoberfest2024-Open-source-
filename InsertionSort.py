def insertionSort(arr):
    n = len(arr)  
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key 
