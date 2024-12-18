def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        
        # Find the minimum element in remaining unsorted array
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element of the unsorted array
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Example usage
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)
