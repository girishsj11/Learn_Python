'''
Leetcode :- First Program 
Given an array of integers nums and and integer target, return the indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
 
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''



'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output=list()
        for i in nums:
            temp = target - i
            if (temp in nums):
                output.append(nums.index(i))
                output.append(nums.index(temp))
                break
            else:
                continue
        return output
'''

def twoSum(num_array, target):
        temp = dict()
        for index, value in enumerate(num_array):
            remaining = target - value
            if remaining in temp:
                return [temp[remaining], index]
            temp[value] = index
        return (list(temp.values()))   
