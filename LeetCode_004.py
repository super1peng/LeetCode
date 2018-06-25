#coding:utf-8


'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of two sorted arrays. The overall run time complexity should be O(log(m+n))

给出两个有序的数字列表，长度分别是m，n。找到这两个列表中的中间值

Example:

    总长度为奇数
    nums1 = [1, 3]
    nums2 = [2]
    The median is 2.0
    
    总长度为偶数
    nums1 = [1, 2]
    nums2 = [3, 4]
    The median is (2 + 3)/2 = 2.5

'''

# 对于已经有序的列表，其实有一个比较次数更小的排序：
# 从小到大，依次进行列表元素的比较（为方便表述，小詹称两个列表为A，B），
# 较小值放到一个新列表中，比如A中该位置的值较小，将其放到新的列表C中，
# 同时将A列表下一个值继续与B中当前位置元素进行比较，以此类推。

class findMedianSortedArrays(object):
    
    def __init__(self):
        pass

    @staticmethod
    def function(nums1, nums2):
        
        # 创建新列表，将所有元素置为0
        nums3 = [0] * (len(nums1) + len(nums2))

        # 指定三个列表的索引
        l_i,r_i,i = 0,0,0

        while(l_i < len(nums1)) and (r_i < len(nums2)):
            if nums1[l_i] < nums2[r_i]:
                nums3[i] = nums1[l_i]
                l_i += 1
            else:
                nums3[i] = nums2[r_i]
                r_i += 1
            i = i + 1
        
        if l_i != len(nums1):
            nums3[i:] = nums1[l_i:]
        else:
            nums3[i:] = nums2[r_i:]
        len_3 = len(nums3)
        
        if len_3 %2 != 0:
            return float(nums3[(len_3-1)//2])
        return (nums3[len_3//2 - 1]+nums3[len_3//2])/2

if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(findMedianSortedArrays.function(nums1,nums2))

    