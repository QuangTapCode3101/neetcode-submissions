class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0] * length
        suffix = [0] * length
        res = [0] * length
        for i in range(length):
            if i == 0 : prefix[i] = 1
            else :
                prefix[i] = nums[i-1] * prefix[i-1]

        for i in range(length - 1, -1, -1) :
            if i  == length -1 : suffix[i] = 1
            else :
                suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(length) :
            res[i] = prefix[i] * suffix[i]
        return res

