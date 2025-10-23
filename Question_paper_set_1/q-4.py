def is_consonant(ch):
    """check character is a lowercase and
     consonant """
    return ch.islower() and ch not in 'aeiou'

def valid_string(s):
    """
    check string match conditions
    """
    return (s.isalpha() and is_consonant(s[0]))

def extract_strings(lst):
    """Extract valid strings from list"""
    return [x for x in lst if isinstance(x, str) and valid_string(x)]

# Example
data = ['apple', 'banana', 'mango', 'kiwi', 'cat', 'dog', 'Elephant', 'tiger', 'ball1', 'go@t']
print(extract_strings(data))