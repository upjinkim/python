cnt_3 = 0
cnt_5 = 0

for i in range(1, 11):
    a = int(input())
    if a % 3 == 0:
        cnt_3 += 1
    if a % 5 == 0:
        cnt_5 += 1
print(f'{cnt_3} {cnt_5}')