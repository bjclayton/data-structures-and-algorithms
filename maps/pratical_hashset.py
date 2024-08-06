class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result
    
    def intersection(self, nums1, nums2):
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
            """
            result = set()
            hashset = set(nums2)
            for num in nums1:
                if num in hashset:
                    result.add(num)
            return result

    def sumOfSquare(self, number):
        total = 0
        while number > 0:
            digit = number % 10
            total += digit ** 2
            number //= 10
        return total

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hashset = set()
        while n != 1 and n not in hashset:
            hashset.add(n)
            n = self.sumOfSquare(n)
        return n == 1
