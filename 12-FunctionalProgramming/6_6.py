employee = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]
result = list(map(lambda e: e[0].upper() + ", " + e[1], employee))
print(result)