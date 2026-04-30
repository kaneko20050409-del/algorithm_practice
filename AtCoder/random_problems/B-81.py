N = int(input())

check = False

for i in range(1,10):
    if N%i == 0 and 1 <= N//i <= 9:
        check = True
        break

if check:
    print('Yes')
else:
    print('No')

# 他の人のやつ
n=int(input())

ans="No"
for x in range(10):
  for y in range(10):
    if x*y==n:
      ans="Yes"
      break

print(ans)