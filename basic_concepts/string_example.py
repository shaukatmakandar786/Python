str="Rahul is a good boy"

print(len(str))# 19
print(str)  #Rahul is a good boy
print(str[4])  #l
print(str[0:5]) #Rahul
print(str[0:19])  #Rahul is a good boy
#print(str[75]) error
print(str[0:75]) #Rahul is a good boy
print(str[0:])  #Rahul is a good boy (it means that print(str[0:19]))
print(str[:5])   #Rahul (it means that print(str[0:5]))
print(str[:])   #Rahul is a good boy (it means that print(str[0:19]))
print(str[::])   #Rahul is a good boy (it means that print(str[0:19:1]))
print(str[0:19:1])   #Rahul is a good boy (it means that print(str[0:19:1]))
print(str[:19:1])   #Rahul is a good boy (it means that print(str[0:19:1]))
print(str[::1])   #Rahul is a good boy (it means that print(str[0:19:1]))
print(str[::])   #Rahul is a good boy (it means that print(str[0:19:1]))

                                #but
print(str[0:19:2]) #Rhli  odby (it skips one one charecter)
print(str[::3])  #Ruiao y (it skips two two charecter)


print(str[-3]) # it gives output from right side and from right side b is on 3rd index
print(str[-3:])  #boy
print(str[-5:-2])  #d b


print(str[::-1])#yob doog a si luhaR (it means it reverse whole string)
print(str[::-2])#ybdo  ilhR (it reverse whole string and print skipping by one charecter)

"""F:\shaukat\ws\ezir-cloud\e-rest\v1\venv1\Scripts\python.exe F:/python/basic_concepts/string_example.py
19
Rahul is a good boy
l
Rahul
Rahul is a good boy
Rahul is a good boy
Rahul is a good boy
Rahul
Rahul is a good boy
Rahul is a good boy
Rahul is a good boy
Rahul is a good boy
Rahul is a good boy
Rahul is a good boy
Rhli  odby
Ruiao y
b
boy
d b
yob doog a si luhaR
ybdo  ilhR

Process finished with exit code 0
"""