def reverse_letters(input_str):
    """
    this method store only letters in reverse and 
    append in new list in reverse

    return reverse_string
    """
    letters = [letter for letter in input_str if letter.isalpha()]
    letters.reverse()
    reverse_string = []
    idx = 0
    for letter in input_str:
        if letter.isalpha():
            reverse_string.append(letters[idx])
            idx += 1
        else:
            reverse_string.append(letter)

    return "".join(reverse_string)


example1 = "a-bC-dEf-ghIj"
print(reverse_letters(example1))
