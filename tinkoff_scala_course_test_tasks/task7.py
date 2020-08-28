import itertools
# from functools import lru_cache

def _check(a, s, d, n):
    x = pow(a, d, n)
    if x == 1:
        return True
    n1 = n-1
    for _ in range(s-1):
        if x == n1:
            return True
        x = pow(x, 2, n)
    return x == n1


def check_prime_miller(n):
    k = 10
    if n < 2:
        return False
    if n < 4:
        return True
    if not n & 1:
        return False
    s = 0
    d = n - 1
    while not d & 1:
        d >> 1
        s += 1
        for a in range(3, n-2, max((n-5) // k, 1)):
            if not _check(a, s, d, n):
                return False
        return True


def get_primes_for_inclusive_interval(start, end):
    primes = [2]
    for i in range(start, end+1, 2):
        if check_prime_miller(i):
            primes.append(i)
    return primes


def get_rd(primes):
    rd = {}
    for i in itertools.product(primes, primes):
        if i[0] < i[1]:
            if not rd.get(i[1]-i[0]):
                rd[i[1]-i[0]] = set()
                rd[i[1] - i[0]].add(i)
            else:
                rd[i[1]-i[0]].add(i)
    return rd


def get_intervals(k, primes):
    rd = get_rd(primes)
    res_keys = list(filter(lambda x: x>=k, rd.keys()))
    intervals_of_primes = dict((k, rd[k]) for k in res_keys)
    return intervals_of_primes


def get_cnt_of_primes(start, end, primes):
    cnt_primes = len(list(filter(lambda x: start<=x<=end, primes)))
    return cnt_primes


def find_first_left_border(c, intervals_of_primes, primes):
    sorted_keys = sorted(intervals_of_primes.keys())
    for item in sorted_keys:
        for i in intervals_of_primes.get(item):
            if c == get_cnt_of_primes(i[0], i[1], primes):
                return i[0]
    return -1


def left_interval_search():
    q = input()
    kc = []
    for i in range(int(q)):
        e = input()
        kc.append([int(x) for x in e.split()])
    primes = get_primes_for_inclusive_interval(3, 100000)
    len_primes = len(primes)
    for i in kc:
        k, c = i
        if (c > len_primes) or (k < c):
            print(-1)
            continue
        intervals = get_intervals(k, primes)
        print(find_first_left_border(c, intervals, primes))
    # return len_primes, primes

left_interval_search()
# primes = get_primes_for_inclusive_interval(2, 10_000)
