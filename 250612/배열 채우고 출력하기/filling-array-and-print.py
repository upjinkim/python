A = input().split()
result = ''
for i in range(len(A)-1, -1, -1):
    result += A[i]

print(result)