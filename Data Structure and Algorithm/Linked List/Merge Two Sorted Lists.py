# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # iteration
#         node = ListNode(0)
#         dummy = node
        
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 print('A')
#                 node.next = l1
#                 l1 = l1.next
#                 print(dummy)
#             else:
#                 node.next = l2
#                 l2 = l2.next
#                 print(dummy)
#             node = node.next
        
#         node.next = l1 if l1 else l2
#         return dummy.next
    
