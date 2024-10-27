def f(palindrom):
    return palindrom == palindrom[::-1]
print(f('radar'))
print(f('1221'))