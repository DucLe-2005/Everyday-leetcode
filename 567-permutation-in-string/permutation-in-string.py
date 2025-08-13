class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count1 = {}
        count2 = {}
        for s in s1:
            count1[s] = count1.get(s, 0) + 1
        
        need = len(count1)
        have = 0
        for i in range(len(s1)):
            count2[s2[i]] = count2.get(s2[i], 0) + 1

            if s2[i] in count1 and count1[s2[i]] == count2[s2[i]]:
                have += 1
            
            if have == need:
                return True

        l = 0
        for r in range(len(s1), len(s2)):
            # move right pointer
            count2[s2[r]] = count2.get(s2[r], 0) + 1

            if s2[r] in count1 and count1[s2[r]] == count2[s2[r]]:
                have += 1
            
            # move left pointer
            if s2[l] in count1 and count1[s2[l]] == count2[s2[l]]:
                have -= 1
            count2[s2[l]] -= 1
            l += 1

            if have == need:
                return True
        
        return False
