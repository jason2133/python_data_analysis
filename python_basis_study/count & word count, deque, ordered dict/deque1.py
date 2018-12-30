from collections import deque

a = deque()

for i in range(5):
    a.append(i)
print(a)

a.appendleft(10)
print(a)

a.rotate(2)
print(a)

a.rotate(2)
print(a)

print(deque(reversed(a)))

a.extend([5, 6, 7])
print(a)
# 오른쪽에 연장시켜요 들어가요

a.extendleft([5, 6, 7])
print(a)
# 왼쪽에 연장시켜요 들어가요
# 5 먼저, 6 두번째, 7 세번째이므로 보이는건 7, 6, 5


