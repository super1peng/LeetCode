#coding:utf-8

'''
    解数独
        编写一个程序，通过已填充的空格来解决数独问题。
        
        一个数独的解法需遵循如下规则：

        数字 1-9 在每一行只能出现一次。
        数字 1-9 在每一列只能出现一次。
        数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
        空白格用 '.' 表示。
'''

'''
    采用回溯法递归实现，基本思路是 首先找到一个待填写的小方格，9个数字依次试探填入，并行下一个方格，如果
    当前方格9个数字 都不满足上面说的三个规则，那么恢复当前环境，并且回溯到前一个方格，依次进行，直至结束。
'''

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        self.board = board
        self.solve()

    def findUnassigned(self):  # 依次查找未被分配的方格
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1, -1

    def isSafe(self, row, col, ch): # 判断是否当前方格填入的数字是否符合要求
        boxrow = row - row % 3
        boxcol = col - col % 3

        if self.checkrow(row, ch) and self.checkcol(col, ch) and self.checksquare(boxrow, boxcol, ch):
            return True
        return False

    def checkrow(self, row, ch):  # 检查一行是否符合条件
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True
 
    def checkcol(self, col, ch):  # 检查一列是否符合条件
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checksquare(self, row, col, ch):  # 检查3x3小宫格是否符合条件
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if self.board[r][c] == ch:
                    return False
        return True


    def solve(self):  # 主递归函数
        row, col = self.findUnassigned()  # 获取一个未被分配的方格
        if row == -1 and col == -1:  # 没有找到，说明已经填好
            return True
        for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if self.isSafe(row, col, num):  # 循环填入数字，并判断是否满足要求
                self.board[row][col] = num
                if self.solve():  # 递归进入下一个方格
                    return True
                self.board[row][col] = '.'  # 后续不满足，那么现在要回复当前环境，并进行下一个数字试探
        return False
        
        



if __name__ == '__main__':
    
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
 
    solu = Solution()
    solu.solveSudoku(board)
    print(solu.board)
    