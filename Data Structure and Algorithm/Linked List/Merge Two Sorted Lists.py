# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # iteration
#         dummy = ListNode(0)
#         cur = dummy
        
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 cur.next = l1
#                 l1 = l1.next
#              
#             else:
#                 cur.next = l2
#                 l2 = l2.next
#             
#             node = node.next
        
#         cur.next = l1 if l1 else l2
#         return dummy.next
---------------------------------------------------- Another Solution ----------------------------------------------------  
#         if not l1: return l2
#         if not l2: return l1
#         if not l1 and not l2: return None
#         list1 = []
#         cur1 = l1 # create pointer1
#         cur2 = l2 # create pointer2
#         while cur1 and cur2:
#             if cur1.val <= cur2.val:
#                 list1.append(cur1.val)
#                 cur1 = cur1.next
#             else:
#                 list1.append(cur2.val)
#                 cur2 = cur2.next
                
#         # transform list to linked list

#         head = ListNode(list1[0])
#         print("this is {}".format(head))
#         cur = head
#         for x in list1[1:]:
#             new_node = ListNode(x)
#             cur.next = new_node
#             cur = cur.next
        
#         if cur1:
#             cur.next = cur1
        
#         if cur2:
#             cur.next = cur2
#         print(head)
        
#         return head
          
