# Quick Task - Binary Search in Action
# Copy this buggy version of merge_sort (a bug exist)

def merge_sort(a, b):
    result = []
    i = 0
    j=0
    while i < len(a) and j < len(b):
        if a[i] < b[j]: # Bug: should be <= (stability not needed but order break)
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result

# Test
print(merge_sort([1, 3, 5], [2, 4, 6]))   # Expected [1,2,3,4,5,6] but gets [1,2,3,4,5,6]?

# The bug doesn't break the merge because 1<2, 2<3 etc. 

def merge_sorted(a,b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    # Bug: missing the remaining elements from the other list!
    # The two while loops below are missing
    return result

print(merge_sorted([1, 3, 5], [2, 4, 6]))   #Output: [1,2,3] - wrong!

#    1. Comment out the second half of the function (the two while loops). Run – bug still there.

#   2.  Uncomment them. Comment out the first while loop. Run – bug disappears (result is empty). So bug is in first loop.

#  3.   Narrow down to the if/else block. You’ll see the issue: missing the remaining elements after one list is exhausted.

# Your task: Do this in your head or on paper. Write in your notes how many steps it took.