# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.


nums = [2, 7, 11, 15]
target = 9
solution = []

for i in range(len(nums)):
    try:
        num2 = nums.index(target - nums[i], i)
        if num2 != i:
            solution.append(i)
            solution.append(num2)
            break
        else:
            continue
    except ValueError:
        continue
