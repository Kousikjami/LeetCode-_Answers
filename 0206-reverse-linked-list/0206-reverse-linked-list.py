# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        cur=head 
        while cur:
            res.append(cur.val)
            cur=cur.next
        res.reverse()
        dummy=ListNode(0)
        p=dummy 
        for i in res:
            p.next=ListNode(i)
            p=p.next 
        return dummy.next
        
        