n = int(input("Enter the number of words in the dictionary: "))
dictionary = set(input("Enter the dictionary words separated by space: ").split())
s = input("Enter the string: ")
dp = [False] * (len(s) + 1)
dp[0] = True
for i in range(1, len(s) + 1):
    for j in range(i):
        if dp[j] and s[j:i] in dictionary:
            dp[i] = True
            break
print(1 if dp[len(s)] else 0)
