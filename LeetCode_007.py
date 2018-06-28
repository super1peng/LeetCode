#coding:utf-8


'''
给定一个32位有符号数，将整数中的数字进行反转
'''

class reserse(object):
    
    def __init__(self):
        pass

    @staticmethod
    def solution_1(x):  
        '''
            这个算法有三点问题：
                未考虑正负号的情况
                未考虑超出32位的情况
                超出时间限制
        '''
        s = ''
        while x // 10 != 0:
            num = x % 10
            s = s + str(num)
            x //= 10 
        s = s + str(x)

        return int(s)

    @staticmethod
    def solution_2( x):
        """
        :type x: int
        :rtype: int
        """
        #先记录正负
        sign = [1,-1][x < 0]
        #利用正负反转后符号不变，并利用绝对值函数进行反转，添加原有符号即可
        rst = sign * int(str(abs(x))[::-1])
        #返回反转值，超出32位为0
        return rst if -(2**31)-1 < rst < 2**31 else 0


if __name__ == '__main__':
    
    print(reserse.solution_2(33636))
    