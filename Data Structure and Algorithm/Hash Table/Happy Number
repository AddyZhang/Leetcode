class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Use hashtable due to repetition
        """
        dict1 = {}
        
        while n != 1:
            list1 = list(map(int, list(str(n))))
            if n not in dict1:
                dict1[n] = 1
                val = sum([x** 2 for x in list1])
                n = val
            else:
                break
                
        if n == 1:
            return True
        else:
            return False
