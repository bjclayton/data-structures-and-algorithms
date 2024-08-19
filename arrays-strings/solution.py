class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest_num = float('inf')
        for num in nums:
            if abs(num) < abs(closest_num):
                closest_num = num
            elif abs(num) == abs(closest_num):
                if num > closest_num:
                    closest_num = num 
        return closest_num

    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = []
        for i , j in zip(word1,word2):
            res.append(i)
            res.append(j)
        
        if len(word1) > len(word2):
            res.append(word1[len(word2):])
        elif len(word2) > len(word1):
            res.append(word2[len(word1):])

        return "".join(res)

    def romanToInt(self, s):
            """
            :type s: str
            :rtype: int
            """
            res = 0
            dic = {'I': 1,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'CM': 1000}
            i = 0
            while i < len(s):
                if i < (len(s) - 1) and dic[s[i]] < dic[s[i+1]]:
                    res += dic[s[i+1]] - dic[s[i]]
                    i += 2
                else:
                    res += dic[s[i]]
                    i += 1
            return res

