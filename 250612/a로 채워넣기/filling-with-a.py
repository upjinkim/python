b = list(input())

if len(b) > 1 :
    b[1] = 'a'
if len(b) > 2 :
    b[-2] = 'a'

print(''.join(b))



