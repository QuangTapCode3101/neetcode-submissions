class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for x in strs :
            count = [0] * 26
            for c in x : 
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(x)
        return list(res.values())