# 비트 연산자
a = 5       # 0000 0101
b = 3       # 0000 0011
print(a & b)
print(a | b)
print(a ^ b)
print(a << b)
print(a >> b)
print(~a)

# 멤버십 연산자
print("a" in "apple")
print(3 in [1,2,3])

# 삼항 연산자
max = a if a > b else b
print("홀수" if a % 2 else "짝수")

score = 85
print("A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D")