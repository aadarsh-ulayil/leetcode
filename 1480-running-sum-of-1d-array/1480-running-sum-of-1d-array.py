class Solution(object):
    def runningSum(self, nums):
        previous_sum = 0
        mylist = []

        for i in nums:
            previous_sum += i
            mylist.append(previous_sum)

        return mylist
        
            
        