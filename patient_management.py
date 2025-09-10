import json
def search(patients, disease):
    result = []
    for p in patients:
        if p["Disease"] == disease:
            result.append(p["Name"])
    return result
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
print("Patients with Flu:", json.dumps(search(patients, "Flu")))
