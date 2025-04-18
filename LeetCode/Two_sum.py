'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
'''

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print([i, j])
                return [i, j]
        
def twoSum_hash(nums, target):
    dic = {}
    for i, n in enumerate(nums):
        if target - nums[i] in dic:
            print([i, dic[target - n]])
            return [i, dic[target - n]]
        dic[n] = i
# twoSum([2,7,11,15], 9)
twoSum_hash([2,7,11,15], 9)
