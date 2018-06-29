#coding:utf-8

'''
    1、在找到第一个非空字符之前，需要移除掉字符串中的空格字符。如果第一个非空字符是正号或者负号，
    选取该符号，并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值。
    如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
    2、字符串可以在形成整数的字符后面包括多余的字符，这些字符可以忽略，它对于函数没有影响。
    3、当字符串的第一个飞空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。
    4、若函数不能执行有效转换时，返回0.

    例子：
        输入: "42"
        输出: 42
    
        输入: "   -42"
        输出: -42
        解释: 第一个非空白字符为 '-', 它是一个负号。我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

        输入: "4193 with words"
        输出: 4193
        解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。

        输入: "words and 987"
        输出: 0
        解释: 第一个非空字符是 'w', 但它不是数字或正、负号。因此无法执行有效的转换。

        输入: "-91283472332"
        输出: -2147483648
        解释: 数字 "-91283472332" 超过 32 位有符号整数范围。因此返回 INT_MIN (−231) 。
'''

class Solution(object):
    def __init__(self):
        pass
    
    @staticmethod
    def function(s):
        sign = 1
        result = 0
        found = False
        
        for char in s:
            if not found and char == " ":
                continue

            elif not found and char == "-":
                found = True
                sign = -1
            elif not found and char == "+":
                found = True
            
            elif char.isdigit():
                found = True
                result = result * 10 + int(char)

                if result > 2147483647 and sign == 1:
                    return 2147483647
                if result > 2147483648 and sign == -1:
                    return -2147483648
            else:
                break
        return sign * result   

if __name__ == '__main__':
    print(Solution.function(' -42'))
    