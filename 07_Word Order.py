from collections import Counter
n = int(input("Enter the number of word: "))
list_of_word = []
for _ in range(n):
    list_of_word.append(input())

distinct_words = Counter(list_of_word)
print(len(distinct_words))
print(*distinct_words.values())
