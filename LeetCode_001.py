#coding:utf-8
import time

'''
Given an array of integers, return indices of the two numbers such that they add up a specific target,
You may assume that each input would have wxactly one solution, and you may not use the element twice.

给出一个数字列表和一个目标值(target),假设列表中有且仅有两个数相加等于目标值，我们要做的就是找到这两个数，并且返回他们的索引。
'''
class twoSum(object):
        

    def twoSum_1(self, nums, target):
        result = []

        '''
        使用两层循环
        '''

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result
    
    def twoSum_2(self, nums, target):
        '''
        使用一层循环
        '''
        result = []
        for i in range(len(nums)):
            oneNum = nums[i]
            twoNum = target - oneNum
            if twoNum in nums:
                j = nums.index(twoNum)

                if i != j :
                    result.append(i)
                    result.append(j)
                    return result
            
    def twoSum_3(self, nums, target):
        
        # 创建一个字典，存储输入列表的元素值和对应索引
        num_dict = {nums[i]:i for i in range(len(nums))}
        print(num_dict)

        # 创建另外一个字典，存储target-列表中元素的值
        num_dict2 = {i:target-nums[i] for i in range(len(nums))}
        print(num_dict2)

        result = []

        for i in range(len(nums)):
            j = num_dict.get(num_dict2.get(i))

            if (j is not None ) and (j!=i):
                result = [i,j]
                break
        return result

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    test = twoSum()

    start = time.time()
    res_1 = test.twoSum_1(nums, target)
    end = time.time()
    print(res_1,end-start)
    
    start = time.time()
    res_2 = test.twoSum_2(nums, target)
    end = time.time()
    print(res_2,end-start)

    start = time.time()
    res_3 = test.twoSum_3(nums, target)
    end = time.time()
    print(res_3,end-start)