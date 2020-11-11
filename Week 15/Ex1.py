studentDictionary = eval(input())
result = ""
for studentClass in studentDictionary:
    studentNumber = studentDictionary[studentClass]
    result += "Class " + studentClass + " has" + str(studentNumber) + " students" + "\n"
print(result)