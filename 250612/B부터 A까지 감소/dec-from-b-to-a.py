A,B = map(int,input().split())
if A < B:
    for i in range(B, A -1, -1):
        print(i, end= ' ')
elif A == B:
    print(A)
     