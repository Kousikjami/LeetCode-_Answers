# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy=tail=ListNode()
        # cur=head
        # cur=cur.next
        # res=0
        # while cur:
        #     if cur.val==0:
        #         tail.next=dummy
        #         res=0
        #     else:
        #         res=res+cur.val
        #         dummy.val=res
        #         dummy.next=None
        #     cur=cur.next
        # return tail.next
        # brute force approach
        res=[]
        x=0
        cur=head.next 
        while cur:
            if cur.val==0:
                res.append(x)
                x=0
            else:
                x+=cur.val
            #res.append(cur.val)
            cur=cur.next
        dummy=ListNode(0)
        cur=dummy
        for i in res:
            cur.next=ListNode(i)
            cur=cur.next 
        return dummy.next
        #print(res)
        