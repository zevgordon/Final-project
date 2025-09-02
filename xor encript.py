
import base64

cypher = 123
stringToEncrypt = "this is a normal string"

strList = [chr(ord(stringToEncrypt[i]) ^ cypher) for i in range(len(stringToEncrypt))]

strList = (base64.b64encode("".join(strList).encode()).decode())
print(strList)

#להחזיר את ההצפנה
newString = base64.b64decode(strList)

newLst = []

for i in range(len(newString)):
    newLst.append(chr(newString[i] ^ cypher))
print("".join(newLst))
