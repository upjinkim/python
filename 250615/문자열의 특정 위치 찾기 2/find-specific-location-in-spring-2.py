a = ['apple','banana','grape','blueberry','orange']
b = input()
cnt= 0
for i in a:
    if len(b) > 0:
        if i[2] == b or i[3] == b:
            print(i)
            cnt += 1
print(cnt)