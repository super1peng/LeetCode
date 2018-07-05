#coding:utf-8

'''
    将罗马数字转换成整数
'''

class Solution(object):
    def __init__(self):
        pass
    
    @staticmethod
    def function_1(s):
        map = {
            "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,
            "IV":4, "IX":9, "XL":40, "XC":90, "CD":90, "CM":900,
        }

        i, res = 0, 0
        while i < len(s):
            if i < len(s)-1 and map.get(s[i:i+2]) != None:
                i, res = i+2, res + map[s[i:i+2]]
            else:
                if map.get(s[i]) != None:
                    i, res = i +1, res + map[s[i]]
        return res



    @staticmethod
    def function_2(s):
        '''
            正常的罗马数字中大的在左边，只有在逢 4 9 时 小的数字会在左边 这时候两个字符联合表示一个数字  右边大-左边小
        '''
        romans = {
            "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,
        }

        # prev_value 存储之前一个字的数据
        prev_value = running_total = 0
        for i in range(len(s)-1, -1, -1):
            int_val = romans[s[i]]

            if int_val < prev_value:
                running_total -= int_val
            else:
                running_total += int_val
            prev_value = int_val
        return running_total


if __name__ == '__main__':
    s = "MCMXCIV"
    print(Solution.function_1(s))
    print(Solution.function_2(s))
    