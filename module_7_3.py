class WordsFinder:
    file_names = ()
    all_words = {}
    def __init__(self, *name):
        self.file_names = name

    def get_all_words(self):
        for name in self.file_names:
            full_text = ''
            with (open(name, encoding='utf-8') as file):
                for line in file:
                    line = line.lower()
                    new_line = ''
                    for char in line:
                        if char == ',' or char == '.' or char == '=' or char == '!' \
                                or char == '?' or char == ';' or char == ':' or char == '-':

                            char = ' '

                        new_line = new_line + char
                        # print(char, end='')

                    full_text = full_text + new_line
                    # print(new_line)
                    self.all_words[file.name] = full_text.split()

        return self.all_words

    def find(self, word):
        file_word_position = {}
        text.get_all_words()
        for file in self.file_names:
            word_position = 0

            for words in self.all_words[file]:
                word_position += 1
                if word.lower() == words:
                    file_word_position.setdefault(file, word_position)
                    break
                else:
                    continue

        return file_word_position

    def count(self, word):
        file_words_count = {}
        for file in self.file_names:
            words_count = 0

            for words in self.all_words[file]:

                if word.lower() == words:
                    words_count +=1
                else:
                    continue

            file_words_count.setdefault(file, words_count)

        return file_words_count







text = WordsFinder('text.txt', 'bob.txt')
# print(text.file_names)

print(text.get_all_words())
print(text.find('teXT'))
print(text.count('teXT'))
