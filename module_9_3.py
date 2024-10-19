first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


first_result = (len(word1) - len(word2) for word1, word2 in zip(first, second) if len(word1) != len(word2))
print(list(first_result))

second_result = (bool(len(word1) == len(word2)) for i in range(len(first)) \
                 for word1 in first[i:i+1] for word2 in second[i:i+1])
print(list(second_result))

# zp = zip(first,second)
# for string in list(zp):
#     print(string)
#     print(len(string[0]) - len(string[1]))
# print(list(zp))

# for i in range(3):
#     for word1 in first[i:i+1]:
#         for word2 in second[i:i+1]:
#             result = bool(len(word1) == len(word2))
#             print(result)