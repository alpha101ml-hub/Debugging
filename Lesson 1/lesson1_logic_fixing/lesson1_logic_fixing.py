def divide_list(nums, divisor):
    result = []
    for i in range(len(nums) + 1):
        value = nums[i] / divisor
        result.append(value)
    return result

data = [10,20,30]
print(divide_list(data, 2))

'''
What does len(nums) return when nums=[10,20,30] ?
len(nums) == 3

What is the sequence of numbers produced by range(len(nums) + 1) ? Write them out.
range(4) produces 0,1,2,3

Inside the loop, nums[i] tries to access an element. What is the largest valid index nums ?
Largest valid index = 2 (because indices: 0,1,2)

At which iteration does i became equal to the largest valid index + 1 ?
When i==3, nums[3] does not exist -> IndexError

'''
