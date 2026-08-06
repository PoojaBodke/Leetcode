class Solution(object):
    def thirdMax(self, nums):
        first=float("-inf")
        second=float("-inf")
        third=float("-inf")
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            if nums[0]>nums[1]:
                return nums[0]
            else:
                return nums[1]
        for num in nums:
            if num == first or num == second or num == third:
                continue
            if num>first:
                third=second
                second=first
                first=num
            elif num>second:
                third=second
                second=num
            elif num>third:
                third=num
            else:
                num
        if third==float("-inf"):
            return first
        else:
            return third
                


        