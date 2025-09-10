def max_seated(seats):
    """
    this method check from before current seat
    and after current seat if seats are empty
    increase count by 1

    return count
    """
    total_seat = len(seats)
    count = 0

    for i in range(total_seat):
        if seats[i] == 0:
            before = (i - 1 < 0 or seats[i - 1] == 0) and (i - 2 < 0 or seats[i - 2] == 0)
            after = (i + 1 >= total_seat or seats[i + 1] == 0) and (i + 2 >= total_seat or seats[i + 2] == 0)

            if before and after:
                seats[i] = 1
                count += 1

    return count


seats = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
print(max_seated(seats))
