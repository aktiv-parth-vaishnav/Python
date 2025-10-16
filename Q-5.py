def count_words(words):
    """
    this method calculate cunt of each ch
    in words

    return count
    """
    count = {}
    for ch in words:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    return count


def most_frequent_word(freq):
    """
    this method count which words have  max
    count

    return word
    """
    max_word = None
    max_count = 0
    for word in freq:
        if freq[word] > max_count:
            max_word = word
            max_count = freq[word]
    return max_word


def analyze_data(text):
    """
    this method saw count of each word in dict and
    most freq word

    return dict
    """
    words = text.split()
    freq = count_words(words)
    most_freq = most_frequent_word(freq)
    return {"Word Frequencies": freq, "Most Frequent Word": most_freq}


text = "apple banana apple orange banana apple banana banana"

# Result Data
print(analyze_data(text))
