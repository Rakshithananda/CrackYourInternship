class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)/2
        nums.sort(reverse = True)
        if len(nums) > 1:
            for i in range(len(nums)-1):
                if nums[i] == nums[i+1]:
                    count = nums.count(nums[i])
                    if count > l:
                        return nums[i]
        else:
            return nums[0]
        