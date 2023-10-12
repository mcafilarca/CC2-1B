n = input("Input: ")

n = int(n)
total_sum = 0

# sum of n numbers in python using for loop
for i in range(1, n+1):
    total_sum = total_sum + i

print("Formula:", sep="", end="")
for i in range(1, n):
    print(i, end="+")
print(n)

print("Output:", total_sum)