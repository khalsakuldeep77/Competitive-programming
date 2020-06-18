#leetcode problem 160
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ## RC ##
        ## APPROACH : 2 POINTER ##
        
        ## LOGIC ##
        # 1) Find the length of both lists;
        # 2) In the biggest list, advance its head N times where N is the length difference between the two lists.
        # 3) Now both lists have the same length, just iterate them and check for node equality.
        
		## TIME COMPLEXITY : O(M+N) ##
		## SPACE COMPLEXITY : O(1) ##

        la= lb = 0
        a , b = headA, headB
        
        while(headA):
            la += 1
            headA = headA.next
        while(headB):
            lb += 1
            headB = headB.next
                
        if( la > lb ):
            diff = la - lb
            while(diff):
                a = a.next
                diff -= 1
        elif( lb > la ):
            diff = lb - la
            while(diff):
                b = b.next
                diff -= 1
        
        while(a and b):
            if(a == b): return a
            a = a.next
            b = b.next
        return None      