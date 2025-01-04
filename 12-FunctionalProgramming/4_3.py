import statistics
grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
to_count = filter(lambda g: g>2.0,grades)
a_mean = statistics.mean(to_count)
print(round(a_mean,2))