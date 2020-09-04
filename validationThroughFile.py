f = open("demofile2.txt", "w")
f.write("nauman 123")
f.close()

f = open("demofile2.txt", "r")
print(f.read())

print(f.read())