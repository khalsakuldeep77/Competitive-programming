class Solution:
    def isValid(self, s: str) -> bool:
        Dict={'[':']','{':'}','(':')'}
        stack=[]
        openn=['(','{','[']
        for i in s:
            if(i in openn):
                stack.append(i)
            elif i not in openn:
                if(len(stack)==0):
                    return 0
                else:
                    close=stack.pop()
                if(Dict[close]!=i):
                    return 0
        if(len(stack)>0):
            return 0
        return 1   