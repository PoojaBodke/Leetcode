class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count={}
        for ch in sorted(ransomNote): 
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        count_1={}
        for ch in sorted(magazine): 
            if ch in count_1:
                count_1[ch]+=1
            else:
                count_1[ch]=1
        for ch in count:
            if ch not in count_1:
                return False
            if count[ch]>count_1[ch]:
                return False
        return True