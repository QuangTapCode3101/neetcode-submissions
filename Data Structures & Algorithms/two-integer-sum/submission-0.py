class Solution:
    def twoSum(self, nums :  List[int], target : int) -> List[int] :
        dict = {}
        for i in range(len(nums)) :
            find  = target - nums[i]
            if find in dict :
                return [dict[find], i] 
            dict[nums[i]] = i
        return []

