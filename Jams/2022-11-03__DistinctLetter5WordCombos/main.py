# with open('5-letter-words.txt') as words_file:
#     words_list = [word for word in words_file.read().splitlines()
#                   if len(set(word)) == 5]

# with open('5-letter-words-unique.txt', 'w') as words_file:
#     words_file.writelines(words_list)

with open('5-letter-words-unique.txt') as words_file:
    words_list = words_file.readlines()

print(len(words_list))
