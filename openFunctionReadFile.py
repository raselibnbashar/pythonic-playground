file = open("student.txt","r+")
#print(file.writable())

#text = file.read()
#text = file.readlines()[0]

for line in file:
    print(line)
#size = len(text)
#print(size)
file.close()