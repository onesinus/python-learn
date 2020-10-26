"""
def caesarJogetJoget(text):
    output = ''

    kamus = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z',
        'D': 'A',
        'E': 'B',
        'F': 'C',
        'G': 'D',
        'H': 'E',
        'I': 'F',
        'J': 'G',
        'K': 'H',
        'L': 'I',
        'M': 'J',
        'N': 'K',
        'O': 'L',
        'P': 'M',
        'Q': 'N',
        'R': 'O',
        'S': 'P',
        'T': 'Q',
        'U': 'R',
        'V': 'S',
        'W': 'T',
        'X': 'U',
        'Y': 'V',
        'Z': 'W'
    }

    for huruf in text:
        if huruf in kamus:
            output += kamus[huruf]            
        else:
            output += huruf
 
    return output

print(caesarJogetJoget('THE Q@1CK BROWN FOX JUMPS OVER THE LAZY DOG'))
"""

"""
def caesar(text):
    output = ""
    kamus = ["A","B","C", "D","E"]

    for letter in text:
        posisi_huruf_dikamus = kamus.index(letter)
        output += kamus[posisi_huruf_dikamus-3]

    return output    

print(caesar("ABC")) # CDE
"""
"""
with open('kalimat.txt', 'r') as f:
    lines = f.read()
    list_kalimat = lines.replace("\n", "").split(".")

    nomor = 1
    for kalimat in list_kalimat:
        with open('kalimat_terpisah.txt', 'a') as a:
            a.write(str(nomor) + ". " + kalimat)
            a.write("\n")
            nomor += 1
"""

"""
def vocal2X(strText):
    output = ""
    vokal = ['a', 'i', 'u', 'e','o']
    for letter in strText:
        if letter in vokal:
            output += "x"
        else:
            output += letter

    return output
            

print(vocal2X('belajar DDP')) # bxlxjxr DDP
"""

def string_match(a,b):
    total = 0
    for i in range(len(a)):
        if i + 1 < len(a):
            two_letter = a[i]+a[i+1]
            if two_letter in b:
                total += 1

    return total

#test cases
print(string_match("xxcaazz", "xxbaaz")) # 3
print(string_match('abc', 'abc')) # 2
print(string_match('abc', 'axc')) # 0
