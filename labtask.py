def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if(char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

text = "DEFENDTHEFORT"
s = int(input("Enter number: "))

print("Normal text: ", text)
print("Encrypted code: ", encrypt(text,s))


def decrypt(data, n):
    result = ""

    for i in range(len(text)):
        data = text[i]

        if(data.isupper()):
            result += chr((ord(data) - n + 65)%26 + 65)

        else:
            result += chr((ord(data) - n + 97) % 26 + 97)

    return result

data = "KLMLUKAOLMVYA"
n = int(input("Enter number: "))

print("Normal text: ", data)
print("Encrypted code: ", decrypt(data,n))