#coding:utf-8

'''
    整数转罗马数字

    字符          数值
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000


    输入: 1994

    输出: "MCMXCIV"

    解释: M = 1000, CM = 900, XC = 90, IV = 4.
'''

class Solution(object):
    def __init__(self):
        pass

    @staticmethod
    def function_1(num):
        
        '''
            暴力法
            考虑所有可能的情况
        '''
        result = ''
        while num > 0:
            if num >= 1000:
                result += 'M'
                num -= 1000
            elif num >= 900:
                result += 'CM'
                num -= 900
            elif num >= 500:
                result += 'D'
                num -= 500
            elif num >= 400:
                result += 'CD'
                num -= 400
            elif num >= 100:
                result += 'C'
                num -= 100
            elif num >= 90:
                result += 'XC'
                num -= 90
            elif num >= 50:
                result += 'L'
                num -= 50
            elif num >= 40:
                result += 'XL'
                num -= 40
            elif num >= 10:
                result += 'X'
                num -= 10
            elif num >= 9:
                result += 'IX'
                num -= 9
            elif num >= 5:
                result += 'V'
                num -= 5
            elif num >= 4:
                result += 'IV'
                num -= 4
            elif num >= 1:
                result += 'I'
                num -= 1
        return result
    
    @staticmethod
    def function_2(num):
        
        '''
            通过构建字典和列表，从高位到低位进行转换输出
        '''

        ans = ''
        values = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        literals = ["M","D","C","L","X","V","I"]

        for idx in [0, 2, 4]:
            k = num // values[literals[idx]]

            re = (num % values[literals[idx]]) // values[literals[idx+ 2]]

            ans += k * literals[idx]
            if re >= 9:
                ans += literals[idx + 2] + literals[idx]
            elif re >= 5:
                ans += literals[idx + 1] + (re - 5) * literals[idx + 2]
            elif re == 4:
                ans += literals[idx + 2] + literals[idx + 1]
            else:
                ans += re * literals[idx + 2]
            
            num %= values[literals[idx + 2]]

        return ans


if __name__ == '__main__':
    num = 1994
    print(Solution.function_1(num))
    print(Solution.function_2(num))
    