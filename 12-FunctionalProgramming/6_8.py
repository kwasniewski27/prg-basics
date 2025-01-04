results = [37,51,44,23,78,92,39,84,83,51]
def min_pts(limit):
   return lambda pts: pts>=limit
min_70 = list(filter(min_pts(70), results))
min_40 = list(filter(min_pts(40), results))
min_30 = list(filter(min_pts(30), results))
print(min_70)
print(min_40)
print(min_30)