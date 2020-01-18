"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# using hashtable
# time complexity is O(n) we use while twice to traverse the linked list
# space complexity is O(n) we copy
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # if head is empty
        if not head:
            return None
        
        hashtable = {}
        # loop 1 copy all the nodes
        cur = head # create a pointer
        while cur:
            hashtable[cur] = Node(cur.val, None, None)
            cur = cur.next
        
        # loop 2 assign next and random pointers
        cur = head # create a pointer
 
        while cur:
            # Python does allow key to be error, just skip it
         
            if cur.next:
                hashtable[cur].next = hashtable[cur.next]
            
            if cur.random:
                hashtable[cur].random = hashtable[cur.random]
            
            cur = cur.next
            
            
        
        return hashtable[head]
