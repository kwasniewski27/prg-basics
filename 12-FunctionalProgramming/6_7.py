scores = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]
def calculate_scores(scores):
    return sum(scores) - max(scores) - min(scores)
final_scores = list(map(calculate_scores, scores))
print(final_scores)