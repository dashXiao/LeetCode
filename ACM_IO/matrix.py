"""
需要在py文件，通过终端执行

(1) 未知行数

a b c
d e f
g h i

(回车换行，在新行 Ctrl + D)


(2) 已知行数

3
1 2 3
4 5 6
7 8 9

"""

import sys

# 未知行数，元素为str
matrix = [line.split() for line in sys.stdin if line]

# 未知行数，元素为int
# matrix = [list(map(int, line)) for line in sys.stdin if line]

# 若已知行数（最简单）
# n = int(input())
# matrix = [input().split() for _ in range(n)]

print(f"matrix: {matrix}\nlen: {len(matrix)}\n")
