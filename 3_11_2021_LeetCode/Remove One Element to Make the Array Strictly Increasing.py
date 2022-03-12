class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        k = 0

        for i in range(1,len(nums)):
            k += nums[i]<nums[i-1]

        if len(set(nums))<len(nums)-1 :
            return False

        if len(set(nums)) == len(nums)-1 and k == 1 :
            return False

        return k<2



if __name__ == "__main__":
    nums = [1, 2, 10, 5, 7]
    nums1 = [2,3,1,2]
    print(Solution().canBeIncreasing(nums1))