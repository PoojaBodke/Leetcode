class Solution(object):
    def sortArrayByParity(self, nums):
        result=[]
        for num in nums:
            if num%2==0:
                result.append(num)
        for num in nums:
            if num%2!=0:
                result.append(num)
        return result     