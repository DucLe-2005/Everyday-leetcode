class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list = s.split()
        word = list[-1]
        return len(word)
    


