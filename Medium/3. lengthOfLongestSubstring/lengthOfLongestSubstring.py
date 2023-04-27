class Solution(object):
    from copy import deepcopy
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lhistory = []
        ihistory = []
        max_length = 0
        i = 0
        j = 0
        while i < len(s):
            if s[i] not in lhistory:
                lhistory.append(s[i])
                ihistory.append(i)
                j+=1
            else:
                if j > max_length: max_length = int(j)
                start_index = lhistory.index(s[i])
                i = ihistory[start_index]
                lhistory = []
                ihistory = []
                j = 0
            i+=1

        if j> max_length:
            max_length = j
        
        return max_length