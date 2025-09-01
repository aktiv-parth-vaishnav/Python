def list_nouns(nouns):
    phrases = []
     # Apply  noun according to char
    for word in nouns:
        if word[0].lower() in "aeiou":
            phrases.append("an " + word)
        else:
            phrases.append("a " + word)

    # if there is two word then join with and
    # otherwise apply and just before last word
    if len(phrases) == 2:
        sentence = phrases[0] + " and " + phrases[1]
    else:
        sentence = ", ".join(phrases[:-1]) + " and " + phrases[-1]

    # Step 3: capitalize first letter + add period
    sentence = sentence[0].upper() + sentence[1:] + "."

    return sentence


# Example 1
print(list_nouns(["orange", "apple", "pear"]))
# "An orange, an apple and a pear."

# Example 2
print(list_nouns(["keyboard", "mouse"]))
# "A keyboard and a mouse."

# Example 3
print(list_nouns(["car", "plane", "truck", "boat", "apple"]))
# "A car, a plane, a truck, a boat and an apple."
