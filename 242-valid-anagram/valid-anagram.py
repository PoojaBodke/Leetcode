class Solution(object):
    def isAnagram(self, s, t):
        count={}
        for ch in sorted(s):
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        count_t={}
        for ch in sorted(t):
            if ch in count_t:
                count_t[ch]+=1
            else:
                count_t[ch]=1
        if count==count_t:
            return True
        else:
            return False
