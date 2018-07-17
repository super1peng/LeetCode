#coding:utf-8

'''
    加1 
        给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
        最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
        你可以假设除了整数 0 之外，这个整数不会以零开头。

    示例：
        输入: [1,2,3]
        输出: [1,2,4]
        解释: 输入数组表示数字 123。
'''

class Solution(object):
    
    def plusOne_1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = digits[::]
        i = len(digits)-1
        while i >= 0:
            if l[i]+1 <=9:
                l[i]+=1
                return l
            else:           
                if i == 0:
                    l[i] = (l[i]+1)%10
                    l.insert(0,1)
                    return l        
                elif l[i]+1 > 9:
                    l[i]=(l[i]+1)%10
                    if l[i-1]+1 < 10:
                        l[i-1] = l[i-1]+1
                        return l
                    else:
                        i-=1


    def plusOne_2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        for i in range(len(digits)-1, -1, -1):
            if i == len(digits)-1:
                change = (digits[-1] + 1) % 10
                flag = (digits[-1] + 1) / 10
                digits[-1] = change
            else:
                change = (digits[i] + flag) % 10
                flag = (digits[i] + flag) / 10
                digits[i] = change
        return digits
            

if __name__ == '__main__':
    digits = [9]
    a = Solution()
    print(a.plusOne_1(digits))
    