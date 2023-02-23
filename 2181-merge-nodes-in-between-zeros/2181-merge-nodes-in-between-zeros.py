# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        tail=dummy
        #cur=head
        cur=head.next
        res=0
        while cur:
            if cur.val==0:
                tail.next=ListNode(res)
                tail=tail.next
                res=0
            else:
                res+=cur.val
            cur=cur.next
        return dummy.next