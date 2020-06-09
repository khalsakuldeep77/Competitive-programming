class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(s==" "):
            return 1
        if(len(s)==1):
            return 1
        if(len(s)<=0):
            return 0
        else:
            ls=[s[0]]
            maxx=0
            for i in range(1,len(s)):

                if(s[i] not in ls):
                    ls.append(s[i])
                else:
                    maxx=max(maxx,len(ls))
                    ls=[s[i]]
            return(maxx)       