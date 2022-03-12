class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(set(nums)) < len(nums)-1:
            return False

        k = 0
        i = 0
        while i < len(nums):
            if nums[i] >= nums[i+1]:
                nums.pop(i)
                k+=1
                i-=1
                continue
            i+=1

        return k<2

if __name__ == "__main__":
    nums  = [2,3,1,2]
    print(Solution().canBeIncreasing(nums))