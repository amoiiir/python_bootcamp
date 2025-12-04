# Unordered, mutable and does not allow dupliate
fruits = {"apple", "banana", "orange"}
numbers = {1,2,3,4,5}

#Set operations
# fruits.add("grape")
# fruits.remove("banana")
# fruits.discard("kiwi")

# print(fruits)

#mathematic operations
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = {5, 1}

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set1.union(set3))
# print(set1.difference(set3))


# Exercise

grades = [("Alice", "Math", 85),
          ("Bob", "Math", 90),
          ("Alice", "Science", 95),
          ("Bob", "Science", 80),
          ("Charlie", "Math", 70),
          ("Charlie", "Science", 75)]

# use loops
student = set()
for grade in grades:
    student.add(grade[0])
print(f"Unique student: {student}")

subject = set()
for sub in grades:
    subject.add(sub[1])
print(f"Unique subject: {subject}")
