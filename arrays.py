#Arrays - carries data type of similar type

courses = ["MIT", "Cyber Security", "Data Science"]
# printing whole array
print(courses)

#Accessing an element in an array
print(courses[1])

#Looping through an array
for y in courses:
    print("Course is", y)

#Addig a new element
courses.append("Android Development")
print(courses)

#Removing an element from an array
courses.remove("MIT")
print(courses)



