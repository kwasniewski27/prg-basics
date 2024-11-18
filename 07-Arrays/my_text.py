def word_count(text):
    words = text.split()
    return len(words)
def lts(text):
    words = text.split()
    return sorted(words, key = lambda words:(-len(words), words))
def alphabet(text):
    words = text.split()
    return sorted(words, key=str.lower)
