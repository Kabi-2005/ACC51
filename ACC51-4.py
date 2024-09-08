tickets = input("Enter the cost of the ticket: ").strip()
K = int(input("Enter the number of digits to be removed: "))
stack = []
for digit in tickets:
    while stack and K > 0 and stack[-1] > digit:
        stack.pop()
        K -= 1
    stack.append(digit)
while K > 0:
    stack.pop()
    K -= 1
result = ''.join(stack).lstrip('0')
print(result if result else "0")

