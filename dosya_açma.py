"""

f=open("dosya2")
print(f.read())
f.seek(0) # cursor'ı bu şekilde başa almak lazım yoksa 2. denemede boşluk okur
print(f.read())
f.close()

"""

"""
with open("dosya1","r") as f:
    icerik = f.read()
    print(icerik)
"""
"""
with open("text_file","r") as f:
    icerik = f.readlines()
    print(icerik)
    for satır in icerik:
        print(satır,end="")
"""
"""
with open("dosya2","w") as f:
    f.write("phyton")
"""
""""
with open("dosya2","a") as f:
    f.write(" ogreniyorum")
"""
"""
with open("dosya1","r") as okunacak:
    with open("dosya2","w") as yazılacak:
        for satir in okunacak:
            yazılacak.write(satir)
"""
"""
with open("Python-Symbol.png","rb") as okunacak:
    with open("dosya4","wb") as yazılacak:
        okunacak_miktar=1024
        içerik=okunacak.read(okunacak_miktar)
        while len(içerik)>0:
            yazılacak.write(içerik)
            içerik=okunacak.read(okunacak_miktar)
"""

""""
text_file = open("dosya1", "r").read()
print("Question A:\n")
print(text_file)
print("______________________")

print("Question B:\n")
for i in text_file.strip().split('\n'):
    [print(j) for j in i.split()]
print("__________________________")

print("Question C:\n")
wordcount = {}
for word in text_file.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for key in wordcount.keys():
    print("%s %s " % (key, wordcount[key]))
print("__________________________")
print("Question D:\n")

"""
"""
icerik = input("Lütfen içeriğinizi giriniz:")
print("question A")
print(icerik)
print("_______________")
"""
""""
kelime = icerik.split()
print(kelime)
print("_______________")
wordcount = {}
for word in icerik.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for key in wordcount.keys():
    print("%s %s " % (key, wordcount[key]))
"""

"""
text_file = open("text_file","r").read()
print ("Question A:\n")
print(text_file)
print("_______________")

print("Question B:\n")
for i in text_file.strip().split("\n"):
    [print(j) for j in i.split()]
print("_______________")

print("Question C:\n")
QuizList = []
with open("text_file",'r') as f:
    for line in f:
        QuizList.append(line.split(None, 1)[0])
capacity = len(QuizList)
index = 0
while index!=capacity:
    line = QuizList[index]
    for word in line.split():
        print(word)
        index = index+1
print("_______________")
print("Question D:\n")
from collections import Counter
words = text_file.split(' ')
dict = Counter(words)
for key in words:
    if dict[key]>1:
        print (key)

from collections import Counter
split_it = text_file.split()
Counter = Counter(split_it)
most_occur = Counter.most_common(5)
print(most_occur)

kelime = text_file.split()


wordcount = {}
for word in text_file.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for key in wordcount.keys():
    print("%s %s " % (key, wordcount[key]))
"""



