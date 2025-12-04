# student = {
#     "name": "Alice",
#     "age": 21,  
#     "courses": ["Math", "Science", "Art"]
# }

# # Accessing values
# print(student["name"])      # Output: Alice
# print(student.get("age"))   # Output: 21
# student["age"] = 22          # Updating age
# student["grade"] = "A"      # Adding new key-value pair
# print(student)

# # Dictionaries method
# keys = student.keys()
# values = student.values()
# items = student.items()

# print(keys)
# print(values)
# print(items)

# for key in student:
#     print(f"{key}: {student[key]}")

# for key, value in student.items():
#     print(f"{key}: {value}")

# # nested dictionaries
# company = {
#     "employees": {
#         "john": {"age": 30, "department": "IT"},
#         "maria": {"age": 23, "department": "Accounting"}
#     },
#     "departments": {"IT", "HR", "Finance"}
# }

# print(company["employees"].items())
# print(company["departments"])

# Exercise

student_records = {
    "student_001": {
        "name": "John",
        "age": "19",
        "major": "Computer Science",
        "grades": [85,92,78]
    },
    "student_002": {
        "name": "Sarah",
        "age": "20",
        "major": "Biology",
        "grades": [90,88,95]
    }
}

# Add new student

# student_records["student_003"] = {"name":"Mike", "age": "18", "major": "Mathematic", "grades": [80,85,88]}
# print(student_records)

# Update john age to 20

# student_records["student_001"]["age"] = 20 
# print(student_records)

# loop through dictionary
for key, values in student_records.items():
    print(f"StudentID: {key}, Name: {values["name"]}, Major: {values["major"]}")