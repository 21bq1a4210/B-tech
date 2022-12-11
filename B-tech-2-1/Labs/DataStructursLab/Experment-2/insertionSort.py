def insertion_sort(arr):
    # Loop through the list, starting at index 1 (the second element).
    # We consider the element at index 0 to be already sorted.
    for i in range(1, len(arr)):
        # Store the value of the element at the current index.
        current_value = arr[i]

        # Keep track of the index of the previous element.
        prev_index = i - 1

        # Loop backwards through the list, as long as the element
        # at the current index is smaller than the previous element.
        # This means that the current element is not in the correct position.
        while prev_index >= 0 and arr[prev_index] > current_value:
            # Shift the element at the previous index to the current index.
            arr[prev_index + 1] = arr[prev_index]

            # Update the previous index to be the index before it.
            prev_index -= 1

        # Once we have found the correct position for the current element,
        # we can insert it into the list by putting it at the index
        # of the previous element + 1 (since we shifted all the elements
        # after the previous index one position to the right).
        arr[prev_index + 1] = current_value

    # Return the sorted list.
    return arr

    
arr = [5, 4, 3, 2, 1]
sorted_arr = insertion_sort(arr)
print(sorted_arr)  # [1, 2, 3, 4, 5]
