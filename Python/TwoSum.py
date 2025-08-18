# import ast  as AST
# class Solution: 
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         num_to_index = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_to_index:
#                 return [num_to_index[complement], i]
#             num_to_index[num] = i
#         return []

# # Example usage:
# sol = Solution()
# # take input from user
# nums = AST.literal_eval(input())
# target = int(input())
# print(sol.twoSum(nums, target)) 






from ast import AST


class Solution:
    def twoSum(self, nums: AST.List[int], target: int) -> AST.List[int]:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i
        for i in range(len(nums)):
            y = target - nums[i]
        if y in h and h[y] != i:
            return [i, h[y]]