def extract_strings(string_list):
    """
    extract strings where The first character must capitalize and consonant.
    The string must not contain any number.

    return extracted_list
    """
    consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
    extracted_list = [
        s for s in string_list
        if s and s[0].isupper() and s[0] in consonants and not any(char.isdigit() for char in s)
    ]
    return extracted_list


unfiltered_strings = []
words = input("enter a word : ")
unfiltered_strings = words.split(" ")
filtered_strings = extract_strings(unfiltered_strings)

print("Enter Strings:", unfiltered_strings)
print("Extracted strings:", filtered_strings)
