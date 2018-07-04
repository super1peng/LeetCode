#coding:utf-8



'''
    给定n个非负数 a1,a2,a3...，an, 每个数代表坐标中的一个点 (i,ai)。
    画n条垂线，使得垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)
    找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

    注意 容器不能倾斜，n至少为2
'''

class Solution(object):
    def __init__(self):
        pass
    
    @staticmethod
    def function_1(height):
        '''
            暴力法，遍历出所有结果最终找到最大值
            超时！！
        '''
        
        max_area = 0
        n =len(height)

        for i in range(n):
            for j in range(i, n):
                area = (j-i) * min(height[i],height[j])
                if area >= max_area:
                    max_area = area
        return max_area
    
    @staticmethod
    def function_2(height):
        '''
            有一种新的遍历方法，双指针法
            分别指向列表的两端，逐步向中间逼近，最后返回最大值
            逼近的方式是：
                较高的那头不动，较低的那头向高的那头移动
        '''
        max_area = left = 0
        right = len(height)-1

        while left < right:
            max_area = max(max_area, (right-left)*min(height[left],height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
        


if __name__ == '__main__':
    height = [2,3,9,1,5,4]
    print(Solution.function_1(height))
    print(Solution.function_2(height))
    