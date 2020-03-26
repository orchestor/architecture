# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

def three_sum(nums):
    res = []
    nums.sort()

    for i in range(len(nums) - 2):
        a = nums[i] 
        start = nums[i - 1]
        end = nums[len(nums) - 1]
        while start < end: 
            if (a + start + end) = 0:
                res.append([a, start, end])
                end = end - 1
            elif (a + start + end) > 0:
                end = end - 1
            else:
                start = start + 1
        return res
# structure programming is a programming paradigm that uses the combination of sequence, iteration and selection structure to express any functions. 
