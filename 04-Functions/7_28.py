def f(dice):
    naj = max(set(dice), key = dice.count)
    return naj
print(f("5233165554211"))
print(f("2133"))