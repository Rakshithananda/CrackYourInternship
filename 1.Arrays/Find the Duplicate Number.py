class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_dict = {}
        for index,value in enumerate(nums):
            if value not in num_dict:
                num_dict[value] = 1
            else:
                num_dict[value] += 1
                return value