# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if(head==None):
            return 
        if(head.next==None):
            return head
        curr=prev=head
        node=head.next
        while(node!=None):
            curr=node
            node=node.next
            curr.next=prev
            prev=curr
        head.next=None
        
        return curr