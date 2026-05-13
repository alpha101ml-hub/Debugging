def divide_list(nums, divisor):
    print(">>> enter divide_list")
    result = []
    for i in range(len(nums)):
        print(f"i = {i}, len(nums) = {len(nums)}")   # shows i becomes 3 when max index is 2
        value = nums[i] / divisor
        result.append(value)
    return result

data = [10, 20, 30]
print(divide_list(data, 2))


# The Crash is at nums[i] when i==3
# Fix: change range(len(nums) + 1) to range(len(nums))