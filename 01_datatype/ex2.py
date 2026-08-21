# 파이썬 자료형
# 1. 기본 자료형: int, float, bool, string
# 2. 컬렉션 자료형: 리스트, 튜플, 딕셔너리, 집합

# int
a = 10
print(a, type(a))

#2진수, 8진수, 16진수
print(bin(a), oct(a), hex(a))
print(ord("A"), chr(65))
x = 10 ** 100
print(x)

# float
b = 3.14
print(b, type(b))

import sys
print(sys.float_info.min)
print(sys.float_info.max)

a = 1.7e308
b = 1.8e308
print(a, b)

print(0.1 + 0.2 == 0.3)
print(f"{0.1:.20f}")
print(f"{0.2:.20f}")
print(f"{0.3:.20f}")

print(float(10))
print(int(3.14))
print(int("100"))
print(float("3.14"))