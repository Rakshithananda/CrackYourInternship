class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        list_num = []
        dict_num = {}
        for i in nums:
            if i not in dict_num:
                dict_num[i] = 1
            else:
                dict_num[i] += 1
                list_num.append(i)
        return list_num