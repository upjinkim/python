a = int(input())
b = []
for i in range(1, a+1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    else:
        b.append(i)
print(len(b)) 