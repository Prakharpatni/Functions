def convert(n):
    if n > 1:
        convert(n//2)
    print(n % 2,end = '')


dec = 23

convert(dec)
