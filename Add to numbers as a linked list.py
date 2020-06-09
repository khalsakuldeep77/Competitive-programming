# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode(0)
        res = head
        
        carry = 0 
        while l1 or l2:
            l1_val = 0 
            l2_val = 0 
            
            if l1:
                l1_val = l1.val
            if l2:
                l2_val = l2.val
            
            cur_sum = l1_val + l2_val +carry
            
            carry = cur_sum//10
            
            res.next = ListNode(cur_sum%10)
            
            if l1:
                l1 = l1.next 
            
            if l2:
                l2 = l2.next 
            res = res.next
        
        if carry:
            
            res.next = ListNode(carry)
        
        return head.next