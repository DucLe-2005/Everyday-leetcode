class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        # a -> y = 24
        # c -> a = 26 - 2 = 24

        # hasp map: (diff_1, diff_2, ..., diff_n): []

        diff_map = defaultdict(list)
        
        for string in strings:
            diffs = []
            for i in range(1, len(string)):
                a, b = ord(string[i - 1]), ord(string[i])
                diff = 0
                if b < a:
                    diff = 26 + b - a  # do a circle
                else:
                    diff = b - a
                diffs.append(diff)
            diff_map[tuple(diffs)].append(string)
        
        res = []
        for strings in diff_map.values():
            res.append(strings)
        
        return res
                



