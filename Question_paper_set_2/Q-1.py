from collections import Counter

def separate_word(sentence):
    """
    this method check in sentence if word count >1
    separate word with #

    return Words
    """

    words = sentence.split()
    word_counts = Counter(words)
    repeated_words = [word for word, count in word_counts.items() if count > 1]
    return ' # '.join(repeated_words)

sentence1 = input("Enter Sentence: ")
result1 = separate_word(sentence1)
print(result1)
