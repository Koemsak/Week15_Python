studentsDictionary = eval(input())
newStudentsNumber = int(input())
newStudentsClass = input()

if newStudentsClass in studentsDictionary:
    studentsDictionary[newStudentsClass] += newStudentsNumber
else:
    studentsDictionary[newStudentsClass] = newStudentsNumber
result = ""
for className in (studentsDictionary):
    studentNumber = studentsDictionary[className]
    result += "Class " + className + " has " + str(studentNumber) + " students" + "\n"
print(result)