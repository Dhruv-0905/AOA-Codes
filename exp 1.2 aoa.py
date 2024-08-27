def insertion_sort(arr):
    n = len(arr)
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key

# Take user input for the array
arr = [int(input("Enter element {}: ".format(i+1))) for i in range(int(input("Enter the number of elements in the array: ")))]

# Call insertion sort function
insertion_sort(arr)

# Print the sorted array
print("Sorted array is:", arr)
