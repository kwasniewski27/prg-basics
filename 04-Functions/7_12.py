def f(n):
    if n>0:
        return "*".join([""] * n).replace("", "/")[1:-1]
print(f(2))