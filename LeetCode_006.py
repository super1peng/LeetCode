#coding:utf-8


'''
将字符串 "PAYPALISHIRING" 以 Z字形排列成给定的行数，之后从左往右，逐行读取字符

    输入: s = "PAYPALISHIRING", numRows = 4
    
    输出: "PINALSIGYAHRPI"
    解释:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
'''

class Convert(object):
    def __init__(self, s, numRows):
        self.s = s
        self.numRows = numRows

    def cal_col(self):
        
        num_lie = 0
        num_median = self.numRows - 2
        res = len(self.s)
        result = []

        num_lie += 1
        res = res - self.numRows
        
        if res > 0:
            result.append( list(self.s[:-1*res]) )
            origin = -1*res
        else:
            result.append(list(self.s[:]))
            print(result)
            return 0

        while res > 0:
            
            for i in range(num_median):
                c = []
                num_lie += 1
                res = res -1
                d = ' ' * (self.numRows - i -2)
                for k in range(len(d)):
                    c.append(d[k])
                c = c + list(self.s[origin:-1*int(res)])
                e = ' ' * (i + 1)
                for k in range(len(e)):
                    c.append(e[k])
                result.append(c)
                origin = -1*res
                if res <= 0:
                    break
            num_lie += 1
            res = res - self.numRows

            if res <= 0:
                c = list(self.s[origin:])
                while len(c) < self.numRows:
                    c.append(' ')
                result.append(c)
                break
            result.append(list(self.s[origin:-1*int(res)]))
            origin = -1*res
        print(result)        
           
        tutu = ''
        for j in range(self.numRows):
            haha = []
            for i in range(num_lie):
                haha.append(result[i][j])
            for k in haha:
                if k != ' ':
                    tutu += k
        print(tutu) 
            
        
    @staticmethod
    def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_length = len(s)
        node_length = 2*numRows - 2  # 两列之间的差
        #其实并不需要第一种方法那样列表字符串来回折腾。。。
        result = ""
        #极端特殊情况，直接返回原字符串
        if str_length == 0 or numRows == 0 or numRows == 1:
            return s
        # 从第一行遍历到最后一行
        for i in range(numRows): 
            #大的改进在这里！！！不再逐一遍历，而相当于j += node_length
            for j in range(i, str_length, node_length):
                # 第一行和最后一行  还有普通行的整列数字
                result += s[j]  
                #不是第一行和最后一行，且不说普通垂直的时，j-*i+node_length得到第i行斜着的那部分需输出的字符
                if i != 0 and i != numRows-1 and j - 2*i + node_length < str_length:
                    result += s[j-2*i+node_length]  # 单列行的数字
        return result

if __name__ == '__main__':
    s = 'PAYPALISHIRING'
    ceshi = Convert(s,4)
    ceshi.cal_col()
    