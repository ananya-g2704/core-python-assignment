import json  
def average(marks):
    return sum(marks) / len(marks)
students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}
averages = {}
for name, marks in students.items():
    averages[name] = round(average(marks), 2)
print("Average Marks:", json.dumps(averages))
top_student = max(averages, key=averages.get)
print("Top Performer:", f"\"{top_student}\"")
