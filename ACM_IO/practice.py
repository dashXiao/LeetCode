'''
Python ACM模式下IO的 “最简” 实现

方法：
读终端输入时，不做类型转换，默认全用str。
之后要用到该数据时，再做可能的类型转换（如 str -> int）

- Author: xyh
- Date:   March 11, 2026
'''

# 单字符
n = input()
print(n)

# 列表
nums = input().split()  # 全为str类型
# nums = [int(num) for num in nums]
print(nums)

# dict
n = int(input())  # 大小
d = dict(input().split() for _ in range(n))  # k-v 全为str类型
print(d)

# matrix
n = int(input())  # 行数
matrix = [input().split() for _ in range(n)]  # 所有元素全为str类型
print(matrix)
