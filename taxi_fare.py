def fare(distance):
    return 50 + (10 * distance)
trips = [5, 10, 3]
total = 0
for i, d in enumerate(trips, 1):
    f = fare(d)
    print("Trip", i, ":$", f)
    total += f
print("Total Fare:$", total)
