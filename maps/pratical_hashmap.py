class Solution(object):    
    def twoSum(nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            hashmap = {}
            for i, n in enumerate(nums):
                num = target - n
                if num in hashmap:
                    return [hashmap[num], i]
                hashmap[n] = i 

    def isIsomorphic(self,  s, t):
            """
            :type s: str
            :type t: str
            :rtype: bool
            """
            smap, tmap = {}, {}
            for i in range(len(s)):
                schar, tchar = s[i], t[i]
                if ((schar in smap and smap[schar] != tchar) or (tchar in tmap and tmap[tchar] != schar)):
                    return False
                
                smap[schar] = tchar
                tmap[tchar] = schar
            return True

    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_map = {element: index for index, element in enumerate(list1)}
        result = {}
        for i in range(len(list2)):
            if list2[i] in index_map:
                result[list2[i]] = i + index_map[list2[i]]
        
        result = [element for element in result if result[element] == min(result.values())]
        return result

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {index: char for index, char in enumerate(s)}
        seen = set()
        for index, char in enumerate(s):
            seen.add(hashmap.pop(index))
            if char not in seen and char not in hashmap.values():
                return index
        return -1

    def intersect(self, nums1, nums2):
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
            """
            result = []
            hashmap = {index: num for index, num in enumerate(nums1)}
            for index in range(len(nums2)):
                if nums2[index] in hashmap.values():
                    for i in hashmap:
                        if hashmap[i] == nums2[index]:
                            hashmap.pop(i)
                            break
                    result.append(nums2[index])
            return result

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_indices = {}
        for index, num in enumerate(nums):
            if num in num_indices:
                if index - num_indices[num] <= k:
                    return True
                    
            num_indices[num] = index
        return False
