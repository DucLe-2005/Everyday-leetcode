class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            anagram_map[tuple(sorted(list(s)))].append(s)
        
        return [x for x in anagram_map.values()]