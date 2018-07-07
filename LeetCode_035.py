#coding:utf-8

'''
    搜索插入的位置
        给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引，如果目标值不存在于数组中，
        返回它将会被按顺序插入的位置。

    示例：
        输入: [1,3,5,6], 5
        输出: 2

        输入: [1,3,5,6], 2
        输出: 1

        输入: [1,3,5,6], 7
        输出: 4
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            
            if target < nums[i]:
                return i

            if target == nums[i]:
                return i

            else:
                continue
            
        return len(nums)

if __name__ == '__main__':
    nums = [1]
    target = 0
    a = Solution()
    print(a.searchInsert(nums, target))
    