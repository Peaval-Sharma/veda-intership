# Student names and marks
names = []
marks = []

n = int(input("Enter the number of students: "))
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    mark = int(input(f"Enter marks of student {i+1}: "))
    names.append(name)
    marks.append(mark)

# Display student records
print("Student Records:")
for i in range(len(names)):
    print(names[i], ":", marks[i])


# Searching a student
search = input("\nEnter student name to search: ")

if search in names:
    index = names.index(search)
    print("Student Found!")
    print("Name:", names[index])
    print("Marks:", marks[index])
else:
    print("Student not found.")


# Highest marks
highest = max(marks)
index = marks.index(highest)

print("\nHighest Score:")
print(names[index], ":", highest)


# Lowest marks
lowest = min(marks)
index = marks.index(lowest)

print("\nLowest Score:")
print(names[index], ":", lowest)


# Sorting marks
sorted_marks = sorted(marks)

print("\nMarks in Ascending Order:")
print(sorted_marks)