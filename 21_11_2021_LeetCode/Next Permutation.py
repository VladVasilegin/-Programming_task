class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        tempList = []
        for i in range(len(nums)-1,-1,-1):
            if len(tempList) == 0:
                tempList.append(nums[i])
            elif nums[i]>=max(tempList):
                tempList.append(nums[i])
            else:
                swapNum = None
                tempList = sorted(tempList)
                for j in range(len(tempList)):
                    if tempList[j] > nums[i]:
                        swapNum = tempList[j]
                        tempList.pop(j)
                        tempList.append(nums[i])
                        break;
                nums[:] = nums[:i]+[swapNum]+sorted(tempList)
                break;
        else:
            nums[:] = sorted(nums)

if __name__ == "__main__":
    nums = [1,1]
    Solution().nextPermutation(nums)
    print(nums)
