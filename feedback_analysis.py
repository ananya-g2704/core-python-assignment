def positive_feedback(ratings):
    if not ratings:
        return 0
    count = 0
    for r in ratings:
        if r >= 4:
            count += 1
    return (count / len(ratings)) * 100
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print("Positive Feedback:", round(positive_feedback(ratings), 2), "%")
