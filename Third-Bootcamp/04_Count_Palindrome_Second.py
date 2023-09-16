

main_set = set()
reverse_set = set()
num_words = int(input("Enter the number of words: "))
for i in range(num_words):
    word = input(f"Enter word {i + 1}: ")
    main_set.add(word)
    reverse_set.add(word[::-1])
difference = main_set - reverse_set
count = len(difference)
print(len(main_set) - count)