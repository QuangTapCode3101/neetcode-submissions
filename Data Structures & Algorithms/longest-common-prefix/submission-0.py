class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        if strs[0] == "" : return ""
        result = ""
        i = 0
        while i < len(strs[0]) and strs[0][i] == strs[-1][i] :
            result += strs[0][i]
            i+=1
        return result 
