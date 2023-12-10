"""
Given an array of integers nums and an integer target, return indices of the two numbers such
that they add up to target.You may assume that each input would have exactly one solution, and
 you may not use the same element twice.You can return the answer in any order.
"""
def twoSum(array,target):
    map={}
    for i,number in enumerate(array):
        find=target-number
        if find in map:
            return [i,map[find]]
        map[number]=i
    return []
