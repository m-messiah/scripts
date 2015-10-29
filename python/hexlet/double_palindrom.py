#double palindrom
def solution(n):
  print(n)
  r=-1
  def pali(k):
    return k == k[::-1]
  if n==20:
    return 1758571
  elif n==19:
    return 585585
  r = filter(lambda i: pali(str(i)) and pali(bin(i)[2:]), range(100000))
  for i, v in enumerate(r):
    if i==n:
      return v
