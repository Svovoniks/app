def solve(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        print("no roots")
    elif d == 0:
        print(-b/(2*a))
    else:
        print((-b-d**0.5)/(2*a), 
              (-b+d**0.5)/(2*a))


print("input: a b c")
solve(*map(int, input().split()))
