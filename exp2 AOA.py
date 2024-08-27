def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left_half = A[:mid]
        right_half = A[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
            
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                A[k] = left_half[i]
                i += 1
            else:
                A[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            A[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            A[k] = right_half[j]
            j += 1
            k += 1

def merge_sort_main():
    user_input = input("Enter the elements separated by spaces: ")
    arr = list(map(int, user_input.split()))
    merge_sort(arr)
    print("Sorted array:", arr)

# Example usage:
merge_sort_main()
