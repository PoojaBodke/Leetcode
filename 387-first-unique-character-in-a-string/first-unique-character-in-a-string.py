class Solution(object):
    def firstUniqChar(self, s):
        count={}
        for ch in s:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        for index,ch in enumerate(s):
            if count[ch]==1:
                return index
        return -1

        