results = [37,51,44,23,78,92,39,84,83,51]
def min_pts(limit):
   return lambda pts: pts>=limit
pts70 = list(filter(min_pts(70), results))
pts40 = list(filter(min_pts(40), results))
pts30 = list(filter(min_pts(30), results))
print(pts70)
print(pts40)
print(pts30)