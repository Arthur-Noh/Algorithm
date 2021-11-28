lines = [6, 2, 5, 5, 4, 5, 6, 3, 7, 5]

def solve(n, start):
    memo = [None] * n
    count = 0
    for i in range(n):
        d = start % 10
        start //= 10
        count += lines[d]
        result = solve_inner(memo, i, d + 1, count)
        if result is not None:
            return start * (10 ** (i + 1)) + result
    return solve_inner(memo, n - 1, 0, count)

def solve_inner(memo, i, start, target_count):
    if start == 0:
        if memo[i] is not None:
            try:
                return memo[i][target_count]
            except KeyError:
                return None
    if i == 0:
        for j in range(start, 10):
            if lines[j] == target_count:
                return j
    else:
        for j in range(start, 10):
            result = solve_inner(
                memo,
                i - 1,
                0,
                target_count - lines[j]
            )
            if result is not None:
                return (10 ** i) * j + result
    if start == 0:
        memo[i] = {}
        memoize(memo, i)
    return None

def memoize(memo, i):
    if i == 0:
        for n in range(10):
            count = lines[n]
            if count not in memo[0]:
                memo[0][count] = n
        return
    for n in range(10):
        for (low_count, val) in memo[i - 1].items():
            count = lines[n] + low_count
            if count not in memo[i]:
                memo[i][count] = n * (10 ** i) + val

            

inp = input().strip()
n = len(inp)
start = int(inp)
result = solve(n, start) - start
if result <= 0:
    result += 10 ** n
print(result)
