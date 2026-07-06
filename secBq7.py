# 7. Create student.txt, write your name, then read and display it
file = open("student.txt", "w")
file.write("uma")
file.close() 
file = open("student.txt", "r")
data = file.read()
print(data)
file.close()