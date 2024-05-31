from collections import defaultdict
from typing import List

class Solution:
   
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for str in strs:
            sorted_tuple = tuple(sorted(str))
            anagrams[sorted_tuple].append(str)
        return list(anagrams.values())

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(solution.groupAnagrams([""]))
print(solution.groupAnagrams(["a"]))