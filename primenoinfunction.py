def prime(a):
    for i in range(2,a):
        if a%i==0:
            return "Not a Prime :("
    return "Prime"

prime(12)