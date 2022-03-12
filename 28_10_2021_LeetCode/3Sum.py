class Solution:
    def threeSum(self, nums):
        out = []
        nums.sort()
        added = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    a, b, c = nums[i], nums[j], nums[k]
                    if a + b + c == 0 and (a, b, c) not in added:
                        out.append([a, b, c])
                        added.add((a, b, c))
        return out


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))