import random
import string
H = input("masukan jumlah string: ")
N = int(H) / 2
N = int(N)
text = ''.join(random.choices(string.ascii_uppercase, k = N))
jomblo = ''.join(random.choices(string.ascii_uppercase, k = 1))
def kebalik(text):
    return text[::-1]
    pallindrom = kebalik(text)+str(text)
if (int(H)%2 == 0):
    print(text + kebalik(text))
else:
    print(text + jomblo + kebalik(text))
