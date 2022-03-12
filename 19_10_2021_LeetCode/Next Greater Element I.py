class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in nums1:
            buff = nums2[nums2.index(i)+1:]
            for j in buff:
                if j>i:
                    result.append(j)
                    break
                    continum
            else:
                result.append(-1)
        return result

if __name__ == "__main__":
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(Solution().nextGreaterElement(nums1,nums2))