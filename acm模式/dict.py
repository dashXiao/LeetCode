"""
需要在py文件，通过终端执行

(1) 未知大小

a 1
b 2
c 3

(回车换行，在新行 Ctrl + D)

(2) 已知大小

3
a 1
b 2
c 3

"""

import sys

d = {}

# 未知大小
for line in sys.stdin:
    k, v = line.split()
    d[k] = v

# 已知大小
# （真正用到数据时再类型转换，似乎更方便？）
# n = int(input())
# d = dict(input().split() for _ in range(n))

print("dict:", d)
