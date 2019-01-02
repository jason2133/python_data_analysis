a = [[1, 2, 3], [4, 5, 6]]
b = [[element for element in t] for t in zip(*a)]
print(b)

# transpose를 먹이면 [1, 4], [2, 5], [3, 6] 이렇게 한 팀을 먹여야 함

