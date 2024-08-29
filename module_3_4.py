def single_root_words(root_word, *other_words):
  same_words = []
  words = list(other_words)
  for i in range(len(other_words)):
    if root_word.lower() in words[i].lower() or words[i].lower() in root_word.lower():
      same_words.append(other_words[i])
  print(same_words)

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')