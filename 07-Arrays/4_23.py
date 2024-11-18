import my_text
text = 'An apple a day keeps the doctor away'
num_words = my_text.word_count(text)
sorted_len = my_text.lts(text)
sorted_alphabet = my_text.alphabet(text)
print(f"Text: {text}")
print(f"Number of words: {num_words}")
print(f"Words from the longest: {', '.join(sorted_len)}")
print(f"Words ordered alphabetically: {', '.join(sorted_alphabet)}")