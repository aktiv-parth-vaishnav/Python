def reverse(str1, str2):
    """
    this method check if char of string 1 is contained in
    str2 or not

    return boolean
    """

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    str2_list = list(str2)

    for ch in str1:
        if ch in str2_list:
            str2_list.remove(ch)
        else:
            return False
    return True


# Result output
print(reverse('listen', 'silenet'))
print(reverse('parth', 'arth'))
