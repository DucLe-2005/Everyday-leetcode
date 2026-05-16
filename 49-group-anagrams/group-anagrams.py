class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use the tuple of a sorted order of the letters as the key to the hash map
        # aabab: ["babba", "aabbbb"]

        anagrams = defaultdict(list)
        for s in strs:
            key = tuple(sorted(list(s)))
            anagrams[key].append(s)
        
        return [x for x in anagrams.values()]
    
        # time: O(c log(c) * n), c is the length of the longest word, n is the number of words
        # space: O(n)