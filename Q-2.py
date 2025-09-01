def reverse_only_letters(str)  :
    #  convert sentence in to letters and reverse it
    letters = [ch for ch in str if ch.isalpha()]
    letters.reverse()  # reverse them

    # create new list and append only if char is alpha
    result = []
    idx = 0
    for ch in str :
        if ch.isalpha() :
            result.append(letters[idx])
            idx += 1
        else :
            result.append(ch)

    return "".join(result)



var = "a-bC-dEf-ghIj"
print(reverse_only_letters(var))


var = "Test1ng-Leet=code-Q!"
print(reverse_only_letters(var))
