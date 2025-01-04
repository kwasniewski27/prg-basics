speed = [48,47,54,50,42,68,39,46]
too_high = filter(lambda s: s>50, speed)
print(list(too_high))