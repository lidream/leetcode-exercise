class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print(len(nums))
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    print (nums[i],nums[j])
                    return(i.j)
                    break
                else:
                    pass

if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    A=Solution()
    print(A.twoSum(nums,target))
    