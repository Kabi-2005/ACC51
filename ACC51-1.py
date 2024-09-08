arr = [1, 2, 3, 2, 1, 4]
N = 2
xor2 = 0
for num in arr:
    xor2 ^= num
right = xor2 & -xor2
num1 = 0
num2 = 0
for num in arr:
    if num & right:
        num1 ^= num
    else:
        num2 ^= num
result = sorted([num1, num2])
print(result)

