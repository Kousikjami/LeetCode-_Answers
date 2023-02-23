# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur=head
        x=[]
        res=[]
        while cur:
            x.append(cur.val)
            cur=cur.next
        i=0
        j=len(x)-1
        while i<j:
            res.append(x[i]+x[j])
            i+=1
            j-=1
        return max(res)