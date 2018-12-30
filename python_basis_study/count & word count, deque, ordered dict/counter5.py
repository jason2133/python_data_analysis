from collections import Counter

text = """Jason Lee is the best ceo of the world. He has bachelor degree in statistics, korea university. I think korea is the best country in the world.""".lower().split()

# 모두 균형을 맞춰주기 위해서 lower()를 통해 소문자 처리
# 그 다음 count 함수를 사용하여 Word 개수 새기

print(Counter(text))
print(Counter(text)["the"])


