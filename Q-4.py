def list_nouns(nouns):
    """
    this method count length of list and
    if list length is 2 put and before last element
    and if list is more than 2 put appropriate noun

    return sentance
    """
    sentance = []
    for word in nouns:
        if word[0].lower() in "aeiou":
            sentance.append("an " + word)
        else:
            sentance.append("a " + word)

    if len(sentance) == 2:
        sentence = sentance[0] + " and " + sentance[1]
    else:
        sentence = ", ".join(sentance[:-1]) + " and " + sentance[-1]

    sentence = sentence[0].upper() + sentence[1:] + "."

    return sentence


# Example 1
print(list_nouns(["orange", "apple", "pear"]))

# Example 2
print(list_nouns(["keyboard", "mouse"]))
