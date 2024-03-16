def big_word_filter():
  long_words = []

  with open("master_file", "r") as input_file:
    for line in input_file:
      words = line.split()
      for word in words:
        if word and word != "\n":
          if len(word) >= 7:
            long_words.append(word)

  with open("big_words", "w") as output_file:
    for word in long_words:
      output_file.write(word + "\n")

big_word_filter()

def count_words_in_file(master_file):
  word_count = 0

  with open("master_file", "r") as master_file:
    for line in master_file:
      words_in = line.split()
      word_count += len(words_in)
    return word_count

master_file = "master_file"

word_count = count_words_in_file(master_file)

print(f"Number of words in the file '{master_file}': {word_count}")

def unacceptable_words():
  search_text = "die"
  replace_text = "***"
  with open("master_file", "r") as file:
    data = file.read()
    data = data.replace(search_text, replace_text)

  with open("unacceptable_words", "w") as file:
     file.write(data)

print(unacceptable_words())