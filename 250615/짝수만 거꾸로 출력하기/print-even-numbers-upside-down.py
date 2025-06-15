a = int(input())
b = list(map(int,input().split()))
even_numbers = []

for num in b:
    if num % 2 == 0:
        even_numbers.append(num)

for i in range(len(even_numbers)-1, -1, -1):
    print(even_numbers[i], end = " ")