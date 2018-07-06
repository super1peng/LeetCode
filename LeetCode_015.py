#coding:utf-8

'''
    三数之和：
        给定一个包含n个整数的数组 nums ， 判断nums中是否存在三个元素 a,b,c 使得 a + b + c = 0
        找出所有满足条件且不重复的三元组。

    
    示例：
        给定数组 nums = [-1, 0, 1, 2, -1, -4]，
        满足要求的三元组集合为：
            [
            [-1, 0, 1],
            [-1, -1, 2]
            ]
'''

class Solution(object):
    def __init__(self):
        pass

    def threeSum(self, nums):
        
        '''
            超过时间限制
        '''
        res = []
        # nums = list(set(nums))
        length = len(nums)
        for i in range(length):
            xixi = []
            target = -1 * nums[i]
            xixi = nums[:i] + nums[i+1:]
            result = Solution.twoSum_2(self, xixi, target)

            for k in result:
                if k == []:
                    continue
                else:
                    k.append(nums[i])
                    k.sort()
                if k not in res:
                    res.append(k)    
        return res


    def twoSum_2(self,nums, target):
        res = []
        for i in range(len(nums)):
            result = []
            oneNum = nums[i]
            twoNum = target - oneNum
            if twoNum in nums:
                j = nums.index(twoNum)

                if i != j :
                    result.append(nums[i])
                    result.append(nums[j])
                    result.sort()
                if result not in res:
                    res.append(result)
        return res

    def best_threeSum(self, nums):
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                left = i+1
                right = len(nums)-1
                while left < right:
                    ident = nums[left] + nums[right] + nums[i]
                    if ident == 0:
                        ans.append([nums[i], nums[left], nums[right]])
                        left += 1; right -= 1
                        while left < right and nums[left] == nums[left-1]:    # skip duplicates
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif ident < 0:
                        left += 1
                    else:
                        right -= 1
        return ans
        

if __name__ == '__main__':
    nums = [0,0,0]
    a = Solution()
    
    print(a.threeSum(nums))
    
    