def threenp1(n):
    count = 0
    while n > 1.0:
       count += 1
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    return count

def threenp1range(upper_limit):
    for n in range(2,upper_limit+1):
       threenp1(n)
       objs_in_sequence = { n: count}

threenp1range()
