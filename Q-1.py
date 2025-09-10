def two_sum(indices, target):
    """
    this method find index that values sum equal = target

    return index
    """
    target_index = []
    length = len(indices)
    for index1 in range(length):
        for index2 in range(index1 + 1, length):
            if indices[index1] + indices[index2] == target:
                target_index.append([index1, index2])
    return target_index


indices = [3, 2, 3, 1, 4]
print(two_sum(indices, 7))
