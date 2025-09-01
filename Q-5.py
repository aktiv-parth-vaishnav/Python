def max_new_seats(seats):
    n = len(seats)
    count = 0

    for i in range(n):
        if seats[i] == 0:
            before = (i-1 < 0 or seats[i-1] == 0) and (i-2 < 0 or seats[i-2] == 0)
            after = (i+1 >= n or seats[i+1] == 0) and (i+2 >= n or seats[i+2] == 0)

            if before and after:
                seats[i] = 1  # Occupy the seat
                count += 1

    return count

seats = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
print(max_new_seats(seats))  # Output: 2
