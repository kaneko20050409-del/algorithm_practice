num = int(input())
surplus = []
value = num

while value != 0:
  surplus.append(value%2)
  value = value//2

binary = ''
for i in range(len(surplus)):
  j = i+1
  binary += str(surplus[-j])

while len(binary) != 10:
  binary = '0' + binary

print(binary)


#f-stringを使った最速コード
num = int(input())
# 010b -> 0埋め、10桁、binary（2進数）の意味
binary = f"{num:010b}"
print(binary)


# ビット演算を利用したコード
num = int(input())
binary = ""

# 9番目のビットから0番目のビットまで順番に調べる
for i in range(9, -1, -1):
    # numをiビット右シフトして、1と論理積をとる
    bit = (num >> i) & 1
    binary += str(bit)

print(binary)