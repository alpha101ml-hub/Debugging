def merge_sorted(a, b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:   #<=
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
print(merge_sorted([1, 3, 5], [2, 4, 6]))   # Expected [1,2,3,4,5,6] but gets [1,2,3,4,5,6]? Actually it's fine. Let's plant a bug.