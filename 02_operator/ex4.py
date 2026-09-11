# 반복문 : while, for

# while
# 1 ~ 10
i = 0
while i < 10:
    i += 1
    print(i)
else:
    print("End")

nums = [1,3,5,7,9]
target = 2
i = 0

while i < len(nums):
    if target == nums[i]:
        print(f"{target} Found")
        break
    i += 1
else:
    print("404 Not found")

i = 0
tot = 0

while i <= 10:
    i += 1
    if i % 2:
        continue
    tot += i

print(f"sum = {tot}")