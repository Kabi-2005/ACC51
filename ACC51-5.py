n = int(input().strip())
prices = [int(input().strip()) for _ in range(n)]
money = int(input().strip())
start = 0
currentsum = 0
maxlength = 0
for end in range(n):
    currentsum += prices[end]
    while currentsum > money:
        currentsum -= prices[start]
        start += 1    
    maxlength = max(maxlength, end - start + 1)
print(maxlength)

