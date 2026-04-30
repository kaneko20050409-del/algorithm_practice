n = int(input())
s = input()

ABC_count = s.count('ABC')

print(ABC_count)

# あえてcountを使わずに書くと
n = int(input())
s = list(input())

count = 0

for i in range(n-2):
    if ''.join(s[i:i+3]) == 'ABC':
        count += 1

print(count)