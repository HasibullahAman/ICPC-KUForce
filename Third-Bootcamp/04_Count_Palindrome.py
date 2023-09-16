main_set = set()
reverse_set = set()
for i in range(int(input("Enter the number of word: "))):
    word = input("Enter the " + str(i) + " word: ")
    main_set.add(word)
    reverse_set.add("".join(reversed(word)))
deff = main_set.difference(reverse_set)
print(len(main_set) -len(deff))