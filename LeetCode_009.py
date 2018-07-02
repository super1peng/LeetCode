#coding:utf-8

'''
    判断一个整数是否是回文数，回文数是指 正序（从左往右）和倒序（从右往左）读都是一样的整数。
'''

class Solution(object):
    
    def __init__(self):
        pass

    @staticmethod
    def function_1(x):
            # 直接领反转整数类似的方法进行判断，判断反转前后结果是否相等即可

            z = x 
            y = 0
            while x > 0:
                y = y * 10 + x % 10
                x //= 10
            return z == y

    @staticmethod
    def function_2(x):
        # 直接强制将其转换成字符串形式，再进行判断，主要是考虑到列表的反转操作很容易

        str_x = str(x)
        str_x_re = list(str_x)[::-1]
        str_x_re = "".join(str_x_re)
        return str_x == str_x_re



if __name__ == '__main__':
    print(Solution.function_1(121))
    print(Solution.function_2(-121))
    