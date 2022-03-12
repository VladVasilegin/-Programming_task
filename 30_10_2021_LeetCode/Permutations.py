class Solution(object):
    def permute(self, nums, result=[], temp=[]):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            result.append(temp)
            return
        for i in nums:
            nums1 = list(nums)
            nums1.pop(nums1.index(i))
            self.permute(nums1, result, temp + [i])
        return result

if __name__ == "__main__":
    nums = [1,2,3,4]
    print(Solution().permute(nums))