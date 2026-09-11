# for
# for i in iterable

for i in range(5):
    print(i, end=" ")
print()

a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 5
for i in range(1,6):
    print(i, end=" ")
print()

# 0 ~ 10 even
for i in range(2,11,2):
    print(i,end=" ")
print()

for i in range(1,6):
    print(i*2, end=" ")
print()

# 5 4 3 2 1
for i in range(5,0,-1):
    print(i,end=" ")
print()

# 1 ~ 10 합
# tot = 0
# for i in range(1,11):
#     tot+=i
# print(f"sum = {tot}")
print(f"sum = {sum(range(1,11))}")

s = "hi12!@한글漢字😍"

for c in s:
    print(c,end=" ")
print()
print(len(s))

# 구구단
for i in range(2,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j:2d}",end="\t")
    print()