def solution(n):
    a = []
    if n == 0:
        return ""
    while n > 0:
        mod = n % 26
        if mod == 0:
            a.append("Z")
            n = n // 26 - 1
        else:
            a.append(chr(mod + 64))
            n = n // 26

    return "".join(a)[::-1]

if __name__ == '__main__':
    print(solution(0))
    print(solution(14))
    print(solution(134))
