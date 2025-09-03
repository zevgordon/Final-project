import base64

with open('cood.txt', 'r') as f:
    cood = f.read()

class Encryption:

    @staticmethod
    def encryption_xor(stringToEncrypt):
        cypher = cood
        cypher = [(ord(cypher[i])) for i in range(len(cypher))]

        repeated_cypher = cypher * (len(stringToEncrypt) // len(cypher)) + cypher[:len(stringToEncrypt)]

        strList = [chr(ord(x) ^ y) for x , y  in zip(stringToEncrypt , repeated_cypher)]

        strList = (base64.b64encode("".join(strList).encode()).decode())
        return strList

A = Encryption.encryption_xor("yossef")
print(A)
