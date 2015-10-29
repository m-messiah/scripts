def solution(s):
    import string
    return sum((string.ascii_uppercase.index(v)+1) * (26**i) for i,v in enumerate(s[::-1]))
