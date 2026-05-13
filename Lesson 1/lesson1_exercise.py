def divide_list(nums, divisor):
    print(nums, divisor)
    result = []
    for i in range(len(nums) + 1):   # intentional off-by-one
        print(f"i = {i}")
        value = nums[i] / divisor
        result.append(value)
        print(value)
    print("return result")
    return result

data = [10, 20, 30]
print(divide_list(data, 2))



