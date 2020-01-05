import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        The run time is O(log(m+n)), then it must use merge sort? The time complex is O(m+n) and the space complex is O(m+n). This is linear search
        """
        
#         k = len(nums1) + len(nums2)
#         array = self.mergeTwoSortedArrays(nums1, nums2)
        
        
#         return (array[(k-1)//2] + array[k//2])/2
     
    
#     def mergeTwoSortedArrays(self, nums1, nums2):
#         """
#         help function to merge two sorted arrays
#         """
#         mergedArray = [0]*(len(nums1)+len(nums2))
#         i = 0
#         j = 0
#         k = 0
#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] <= nums2[j]:
#                 mergedArray[k] = nums1[i]
#                 i += 1
#                 k += 1
#             else:
#                 mergedArray[k] = nums2[j]
#                 j += 1
#                 k += 1
#         if i < len(nums1):
#             while i < len(nums1):
#                 mergedArray[k] = nums1[i]
#                 k += 1
#                 i += 1
        
#         if j < len(nums2):
#             while j < len(nums2):
#                 mergedArray[k] = nums2[j]
#                 k += 1
#                 j += 1
        
#         return mergedArray
        """
        Use binary search
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # else:
        #     A, B = nums1, nums2
        print(len(nums1))
        # print(len(A))
        # print(len(B))
        if len(nums1) == 0:
            return (nums2[(len(nums2)-1)//2] + nums2[(len(nums2))//2])/2
                
        start = 0
        end = len(nums1)
        
        while start <= end:
            partionx = (start+end)//2 # number of elements in x        
            
            partiony = (len(nums1)+len(nums2)+1)//2-partionx
            
            if partionx == 0:
                xl = float('-inf')
            else:
                xl = nums1[partionx-1]
            
            if partionx == len(nums1):
                xr = float('inf')
            else:
                xr = nums1[partionx]

            if partiony == 0:
                yl = float('-inf')
            else:
                yl = nums2[partiony-1]
            
            if partiony == len(nums2):
                yr = float('inf')
            else:
                yr = nums2[partiony]

            if xl > yr:
                end = partionx - 1

            elif yl > xr:
                start = partionx + 1

            else:
                if (len(nums1) + len(nums2))%2==0:
                    return (max(xl,yl)+min(xr,yr))/2
                else:
                    return (max(xl,yl))
