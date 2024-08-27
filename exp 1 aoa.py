def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for k in range(i+1, n):
            if arr[k] < arr[min_index]:
                min_index = k
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Take user input for the array
arr = [int(input("Enter the elements: ")) for _ in range(int(input("Enter the number of elements in the array: ")))]
print("Unsorted Array",arr)

# Call selection sort function
selection_sort(arr)

# Print the sorted array
print("Sorted array is:", arr)
