def solution(s):
    import string
    return sum((string.ascii_uppercase.index(v)+1) * (26**i) for i,v in enumerate(s[::-1]))

if __name__ == '__main__':
    print(solution(""))
    print(solution("C"))
    print(solution("ABC"))