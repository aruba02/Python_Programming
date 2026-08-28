# string

a = "python"
print(a, type(a))

print("I'll be back")
print('I\'ll be back')

a = """
Life is short
You need python
"""
print(a)

def func():
    """
    func() 함수에 대한 설명 작성
    """
    pass
print(func.__doc__)

print("Hello" + "Python")

print("Hello" * 10)
print("-" * 50)

print("Hello" + str(3))

print("10" + "2")
print(int("10") + int("2"))

name = "pororo"
age = 23

print(f"이름 : {name}, 나이: {age}")
print(f"내년 나이: {age + 1}살")
print(f"{name.upper()}")

pi = 3.141592

print(f"{pi:.3f}")
print(f"{pi:.0f}")

num = 123456789
print(f"{num:,}")

print(f"{num:15,d}")
print(f"{num:<15,d}")

print(f"{num:015,d}")
print(f"{num:<015,d}")
