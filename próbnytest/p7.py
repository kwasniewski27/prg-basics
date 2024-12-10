import re
def f(array):
    count = 0
    pattern = '^[A-Za-z0-9_]+$'
    for word in array:
        if re.match(pattern, word) and 4<=len(word)<=12:
            count += 1
    return count
print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))