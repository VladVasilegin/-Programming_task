class Solution:
    def arrayPairSum(self, nums) -> int:
        nums.sort()
        return sum(nums[::2])


if __name__ == "__main__":
    x = [6,2,6,5,1,2]
    print(Solution().arrayPairSum(x))