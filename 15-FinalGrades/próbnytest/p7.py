import re
def f(array):
    pattern = '[^a-z0-9_]+$'
    matching = []
    for word in array:
        if re.match(pattern, word) and 4<= len(word) <= 12:
            matching.append(word)
    return len(matching)
print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))