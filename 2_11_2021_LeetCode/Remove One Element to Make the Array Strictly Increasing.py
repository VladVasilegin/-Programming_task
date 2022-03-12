class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(1,len(nums)-2):
            if not nums[i-1]<nums[i]<nums[i+1]:

        return True

if __name__ == "__main__":
    nums = [1, 2, 10, 5, 7]
    print(Solution().canBeIncreasing(nums))