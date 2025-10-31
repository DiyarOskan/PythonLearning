import random
import tkinter

import download as download
import pip
import pytube as pytube

print("selam")

print("merhaba \tyakın kampüs")

print('Ali\'nin evi')

print("""Ben
Alt
Alta 
Yazabiliyorum""")

print("benim adım {}, yaşım {}".format('diyar', 21))

print("benim adım {1} , yaşım {0}".format(21, "diyar"))

print("benim adım {ad} , yaşım {yaş}".format(yaş=21, ad="diyar"))

renkler=["siyah","beyaz","mavi","yeşil"]
renkler.insert(3,"pembe")
print(renkler)

liste2=sorted(renkler)
print(liste2)
print(renkler)

print("mor" in renkler)

stringrenkler= "-".join(renkler)
print(stringrenkler)

isim="İbrahim"
mesaj="merhaba"

print(f"{isim} {mesaj} dedi")

sayı = 10
print(sayı)

sayı = sayı + 1
print(sayı)

print(3 + 4)
print(3 * 4)
print(5 % 3)
print(5 - 3)
print(6 / 2)
print(5**5)
print(abs(-3))
sayı=52/7
print(round(sayı))

a = "Python"
print(a)

print(a[0])

print(a[2:])

print(a[:3])

print(a[2:5])

print(a[::2])

print(a[1:5:3])

print(a[::-1])


print(len(a))

print(a + " ogren!")

print(a * 3)

print(a.upper())

print(a.lower())

b = "Python ogren"
print(b.split())
print(b.split("o"))
print(b.split("o", maxsplit=1))

a = True
print(type(a))

yaş1 = 20
yaş2 = 18
print(yaş1 > 18)
print(yaş2 > 18)

print(not yaş2 > 18)

liste = ["a", "b", "c", "d", "e", "a"]
print(liste)
liste = liste + ["f"]
print(liste)
print(liste[0])
print(liste[3:5])
liste.append("g")
print(liste)
liste.pop()
print(liste)
print(liste.pop())
liste.pop(4)
print(liste)

sayılar = [123, 12321, 312, 45435, 35, 345, 1, 1]
sayılar.sort()
print(sayılar)
sayılar.reverse()
print(sayılar)

küme1={"sarı","mavi","yeşil","beyaz","siyah"}
küme2={"sarı","mavi","gri","mor"}
print(küme1.intersection(küme2))

phyton=set("PHYTON")
print(phyton)

tup = ("a", "b", "c", "d", "e", "a")
print(tup)
liste[0] = "123"
print(liste)
print(tup.count("a"))
print(tup.index("b"))

dic1 = {"isim": "Diyar",
        "yaş": 21,
        "lokasyon": "İstanbul"}
print(dic1)

print(dic1.get("soyad"))
print(dic1.get("soyad","bulunamadı"))

for x in dic1:
    print(dic1[x])

dic2 = {"isim": "Diyar",
        "yaş": 21,
        "lokasyon": {"doğduğu_şehir": "Diyarbakır",
                     "yaşadığı_şehir": "İstanbul"
                     }
        }
print(dic2)

del dic2["isim"]
print(dic2)


fruits={"apple","banana","cherry"}
more_fruits={"strawberry","watermelon"}
fruits.update(more_fruits)
print(fruits)


print(dic2["yaş"])
print(dic2["lokasyon"]["doğduğu_şehir"])

print(dic1.keys())
print(dic1.values())
print(dic1.items())


hava_durumu = "karlı"
if hava_durumu == "yağışlı":
    print("şemsiyeni al")
elif hava_durumu == "karlı":
    print("atkını al")
else:
    print("sorun yok")
liste3 = ["a", "b", "c"]
hedef_harf = "d"
if hedef_harf in liste3 and hedef_harf == liste3[0]:
    print("buldum ve listenin ilk elemanı")
elif hedef_harf in liste3:
    print("listede var ancak ilk eleman değil")
else:
    liste3.append(hedef_harf)
    print("listeye ekledim")
    print("güncel liste{}".format(liste3))

ibrahim_oley = ["İbrahim", "Ceren", "Leyla", "Atahan", "Şayan", "İrem", "Hivda"]

for üyeler in ibrahim_oley:
    print(üyeler)

üye_sayısı = 0
for üyeler in ibrahim_oley:
    üye_sayısı = üye_sayısı + 1
    print(üye_sayısı, üyeler)
tup1 = (1, 3, 5, 7)
for sayi in tup1:
    print(sayi)

liste = [[1, 2], [3, 4], [5, 6]]
for x, y in liste:
    print(x)
liste2 = [[1, 2], [3, 4], [5, 6]]
for x, y in liste2:
    print(x * y)
kullanıcı1 = {
    "ad": "diyar",
    "soyad": "oskan"
}
print(kullanıcı1.items())
for k, v in kullanıcı1.items():
    print("key:{}  \tvalue:{}".format(k, v))

x = 0
while x < 10:
    print("{} değeri 10'dan küçüktür".format(x))
    x += 1
else:
    print("{} değeri 10'dan küçük değildir".format(x))

sayı = 6
sonuç = 1

while sayı > 0:
    sonuç = sonuç * sayı
    sayı -= 1
print(sonuç)

sayı = 6
sonuç = 1

while sayı > 0:
    sonuç = sonuç * sayı
    sayı -= 1
    print(sonuç)

sonuç = 1
for i in range(10):
    sonuç *= 2
print(sonuç)


liste1=["a","b","c"]
liste2=[1,2,3]

for harf in liste1:
    for rakam in liste2:
        print(harf,rakam)
boş_liste=[]
liste = range(1,30)
for x in liste:
    if x%3==0:
        print(x)

x=2
y=3
while x*y<200:
    print(x,"kere",y,x*y,"eder")
    x+=2
    y+=2

i=1
while True:
    print(i)
    i+=1
    if i == 10:
        break


a = range(10)
print(a)

a = list(range(10))
print(a)

for sayı in range(10):
    if sayı > 5:
        print(sayı)

harfler = ["a", "b", "c", "d", "e"]
for harf in enumerate(harfler):
    print(harf)

for index, harf in enumerate(harfler,start=1):
    print(index, harf)

ülkeler = ["TR", "FR", "DE"]
sıralamalar = range(1, 4)
for ülke in zip(ülkeler, sıralamalar):
    print(ülke)

harfler = ["a", "b", "c", "d", "e"] * 5
for index, harf in enumerate(harfler):
    if harf == "c":
        print(" c harfi {}. indexte!".format(index))

harfler = ["a", "b", "c", "d", "e"] * 5
for index, harf in enumerate(harfler):
    if harf == "c":
        print(" c harfi {}. indexte!".format(index))
        break

for sayı in range(1, 6):
    if sayı % 2 == 0:
        continue
    print(sayı)

for sayı in range(1, 6):
    if sayı % 2 == 0:
        pass
    else:
        print(sayı)

if sayı < 5:
    pass
else:
    print("hey")

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["color"] = "red"
print(car)


"""
sayı= int(input("Bir sayı giriniz:"))
faktoriyel=1
for i in range(1,sayı+1):
    faktoriyel *= i
print(f"{sayı}! = {faktoriyel}")
"""
"""
sayı= int(input("Bir sayı giriniz:"))
prime=True
for i in range(2,sayı):
    if sayı%i==0:
        prime = False
        break
if prime==True:
    print(f"{sayı} sayısı asaldır")
else:
    print(f"{sayı} sayısı asal değildir")
"""
"""
sayı= int(input("Bir sayı giriniz:"))

bölen_sayısı=0
for i in range(1,sayı+1):
     if sayı %i==0:
         bölen_sayısı +=1
print(f"{sayı} sayısının {bölen_sayısı} tane pozitif tam sayı böleni vardır.")
"""
"""
sayı= int(input("Bir sayı giriniz:"))

bölen_sayısı=0
for i in range(1,sayı+1):
     if sayı %i==0:
         bölen_sayısı +=1
print(f"{sayı} sayısının {bölen_sayısı*2} tane tam sayı böleni vardır.")
"""
"""
sayı= int(input("Bir sayı giriniz:"))
str_sayı=str(sayı)
toplam=0
for rakam in str_sayı:
    toplam += int(rakam)
print(toplam)
"""
"""
sayı= int(input("Bir sayı giriniz:"))
boş_liste=[]
liste = range(1,sayı)
for x in liste:
    if x%3==0:
        boş_liste.append(x)
print(len(boş_liste))
"""
"""
liste=[]
for i in range(5):
    sayı=int(input("Bir sayı giriniz:"))
    liste.append(sayı)
print(f"Girilen sayılar arasında en büyük olan {max(liste)} sayısıdır :)")
"""
"""
sayı=int(input("Bir sayı giriniz:"))
karekök=sayı ** 0.5
if karekök==int(karekök):
    print(f"{sayı} bir tamkare sayıdır :)")
else:
    print(f"{sayı} bir tamkare sayı değildir :(")
"""
"""
metin = input("bir metin girin:")
sözlük= dict()

for harf in metin:
    if harf in sözlük:
        sözlük[harf] +=1
    else:
        sözlük[harf] =1
for harf,adet in sözlük.items():
    print(harf,adet)

"""
def my_function():
    print(5)
my_function()


def my_function():
    """
    bu fonksiyon 5 bastırıyor
    """
    print(5)

my_function()


def my_function2(sayı):
    return sayı


print(my_function2(10))


def büyük_sayıyı_döndür(x, y):
    if x > y:
        return x
    elif y > x:
        return y

print(büyük_sayıyı_döndür(3,10))

def metin_yazdır(x,y):
    şablon_metin = "{} daha büyük sayıdır".format(büyük_sayıyı_döndür(x, y))
    print(şablon_metin)
metin_yazdır(5,10)

def isimleri_ayır(*args):
    return " ".join(args)
print(isimleri_ayır("ibrahim" ,"Oskan"))

def göbekadı_yazdır(**kwargs):
    if "göbekadı"in kwargs:
        print(kwargs["göbekadı"])
    else:
        print("göbek adı yok")
göbekadı_yazdır(adı="İbrahim",soyadı="Oskan")
göbekadı_yazdır(adı="İbrahim",göbekadı="diyar" , soyadı="Oskan")

def karesini_al(x):
    return x**2

sayılar=list(range(1,6))
print(sayılar)

for a in range(len(sayılar)):
    sayılar[a]= karesini_al(sayılar[a])
print(sayılar)

sayılar=list(range(1,6))
print(list(map(karesini_al,sayılar)))


def çift_sayıları_filtrele(x):
    return x if x%2==0 else "sayı çift değil"
print(çift_sayıları_filtrele(33))

sayılar=list(range(1,11))
def çift_sayıları_filtrele(x):
    return x if x%2==0 else None
print(list(filter(çift_sayıları_filtrele,sayılar)))


"""x=input("bir sayı girin:")
print(int(x))
"""

"""def uygulama():
      girdi= input("Lütfen bir sayı giriniz:")
      işlem= input("Girdiğiniz sayı tek midir, yoksa çift midir?")
      if işlem=="çift":
          if int(girdi)%2==0:
              return "Evet {} sayısı çift bir sayıdır.".format(girdi)
          else:
              return "Hayır {} sayısı bir çift sayı değildir.".format(girdi)
      if işlem=="tek":
          if int(girdi)%2==1:
              return "Evet {} sayısı tek bir sayıdır.".format(girdi)
          else:
              return "Hayır {} sayısı bir tek sayı değildir.".format(girdi)
print(uygulama())"""

"""
def sayı_girdisi_kontrol_döngüsü():
    girdi= input("Bir sayı giriniz:")
    while not girdi.isdigit():
        print("Bu bir sayı mı sence eşşşek!")
        girdi=input("Bir sayı giriniz:")
    else:
        print("Helal ln sana, sayıları biliyon!")
print(sayı_girdisi_kontrol_döngüsü())
"""
"""def eposta_kontrol():
    girdi=input("geçerli bir eposta adresi gir:")

    while not (("." in girdi) and ("@") in girdi):
        print("düzgün bişi gir")
        girdi = input("geçerli bir eposta adresi gir:")
    else:
        print("Afferim")
print(eposta_kontrol())"""
"""def tam_sayıya_çevir():
    girdi=input("Bir ondalık sayı gir:")
    status=""
    try:
        girdi=float(girdi)
        print("Yuvarlama işlemi sonucu:{}".format(round((girdi))))
        status="başarılı"
    except:
        print("{} girdisi ondalık tipe çevrilemiyor".format(girdi))
        status="başarısız"
    finally:
        print("yuvarlama işlemi {} olarak tamamlandı!".format(status))
print(tam_sayıya_çevir())"""


"""
def rowOperation(matrix, i, j, multiplier):

    columlength = len(matrix[0])
    for k in range(columlength):
        matrix[j][k] = multiplier * matrix[i][k] + matrix[j][k]
    i+=1


def reduceColumn(matrix, i):

    n, m = len(matrix), len(matrix[0])
    for j in range(i+1, n):
        factor = matrix[j][i] / matrix[i][i]
        for k in range(i, m):
            matrix[j][k] -= factor * matrix[i][k]

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 12, 12]]
reduceColumn(matrix, 0)
print(matrix)
reduceColumn(matrix, 1)
print(matrix)
reduceColumn(matrix, 2)
print(matrix)
"""

from random import randint
from random import shuffle
print(randint(0,100))

my_list = [10,20,30,40]
shuffle(my_list)
print(my_list)

food_list= ["apple","banana","melon"]
calories_list = ["100","150","200"]
day_list = ["monday", "tuesday", "wednesday"]
zipped_list = list(zip(food_list,calories_list,day_list))
print(zipped_list)

my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}
if "c" in my_dictionary.values():
    print("yes")

r_list = [3,2,5,8,4,6,9,12]
new_list = []
for i in r_list:
    new_list.append(2*3.14 * i)
print(new_list)

age_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]
age_list = []
for (name,age) in age_name_list:
    age_list.append(age)
print(age_list)

metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]
from random import randint
print(metal_list[randint(0,len(metal_list)-1)])


def unutma():
    print("BAŞARMAK İSTİYORSAN DİŞİNİ SIKACAKSIN !!!")

unutma()
def hello_name(name):
    print("hello")
    print(name)
hello_name("ibrahim")

"""def toplama_işlemi(sayı1,sayı2):
    sayı3 = sayı1 + sayı2
    print(sayı3)
toplama_işlemi(3,5)

def bölüm(sayılar):
    return sayılar / 2
listem=[3,5,7,10,20,30]
boş_listem=[]
for i in listem:
    boş_listem.append(bölüm(i))
print(boş_listem)

numList=[10,20,30]
print(list(map(lambda i:i/4,numList)))

class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printName(self):
        print(self.name)
diyar= Person("diyar",22,"erkek")

diyar.printName()

class Dog():
    year=7
    def __init__ (self,age):
        self.age=age
        self.humanAge = age * Dog.year
myDog= Dog(3)
print(myDog.age)
print(myDog.humanAge)

class Engineer():
    def __init__(self,name):
        self.name= name
        print("Engineer")
    def test1(self):
        print("test1")
diyar= Engineer("diyar")
print(diyar.name)

class EngineerPlus(Engineer):
    def __init__(self,name):
        Engineer.__init__(self,name)
        print("EngineerPlus")
İbrahim= EngineerPlus("İbrahim")
print(İbrahim.name)


class Banana():
    def __init__(self,name):
        self.name = name
    def info(self):
        return "100 calories {}".format(self.name)


class Apple():
    def __init__(self, name):
        self.name = name

    def info(self):
        return "50 calories {}".format(self.name)

fruitlist=[Banana,Apple]
for fruit in fruitlist:
    print(fruit.info())

class Phone ():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def info(self):
        return f"{self.name} price is : {self.price}"
Iphone = Phone("Iphone 14",500)
print(Iphone.info())

myList = [2,3,4,5,6]

boş_liste=[]
def myFunc(num):
    return num ** 3
for i in myList:
    boş_liste.append(myFunc(i))
print(boş_liste)

def bölüm(sayılar):
    return sayılar / 2

listem=[3,5,7,10,20,30]
boş_listem=[]
for i in listem:
    boş_listem.append(bölüm(i))
print(boş_listem)

"""

myList = [2,3,4,5,6]

boş_liste=[]
def myFunc(num):
    return num ** 3
print(list(map(myFunc,myList)))

class Phone ():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def info(self):
        return f"{self.name} price is : {self.price}"
Iphone = Phone("Iphone 14",500)
print(Iphone.info())

barkodDizisi = ["ABC231","SA3123XYZ","XYZA123Q","QRE1231KJ","X112QGL"]

def filtreleme(list):
    for i in list:
        if "XYZ" in i:
            print(i)

filtreleme(barkodDizisi)

"""while True:
    try:
        myAge= int(input("enter age:")) * 2
        print(myAge)
        break
    except:
        print("enter your age!!!")"""

"""with open("dosya1","r") as f:
    dosyanın_içindekiler = f.read()
    print(dosyanın_içindekiler)

with open("dosya1","r") as f:
    dosyanın_içindekiler = f.readlines()
    print(dosyanın_içindekiler)

with open("dosya2","a") as f:
    f.write("Endüstri Mühendisliği 3. sınıf öğrencisi")

with open("dosya1",) as iç_dosya:
    with open("dosya2","w") as dış_dosya:
        for iç_dosyada_yazılanlar in iç_dosya:
            dış_dosya.write(iç_dosyada_yazılanlar)"""

"""from animalPackage.catPackage import meow"""


"""
********************************************** YOUTUBE VİDEO İNDİRİCİ***************************************************
import pytube
from pytube import YouTube

url = input("enter video url: ")

path = ""

pytube.YouTube(url).streams.get_highest_resolution().download(path)
"""
"""
*********************************************** FOTO ARKA PLAN TEMİZLEYİCİ *********************************************

from rembg import remove

input_path = "python_fotoo.png"
output_path = "output.png"

with open(input_path,"rb") as i:
    with open(output_path, "wb") as o:
        input_file = i.read()
        output_file= remove(input_file)
        o.write(output_file)
"""
"""
**************************************** PDF ÇEVİRİCİ ******************************************************************
 from pdf2docx import Converter

pdf_file = "sample.pdf"
docx_file = "sample.docx"

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
"""


"""
**********************************************  QR KOD OLUŞTURUCU*******************************************************
import pyqrcode

url = input("enter url to generate qr code: ")

qr_code = pyqrcode.create(url)
qr_code.svg('qrcode.svg',scale= 5)
"""

"""
********************************************** REMINDER FOR PC *********************************************************

#import notification from plyer module
from plyer import notification
#import time
import time

#Use while loop to create notifications indefinetly
while(True):
    #notification
    notification.notify(
        title = "Reminder to take a break",
        message = '''Drink water, take a walk''',
        timeout = 10
    )
    #System pause the execution of this programm for 60 minutes
    time.sleep(3600)
"""
"""
************************************************** TURTLE **************************************************************

KARE ÇİZİM

import turtle

drawing_board= turtle.screen()
drawing_board.bgcolor("#FF5733")
drawing_board.title("python turtle")

turtle_instance = turtle.Turtle()
for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.left(90)
turtle.done()

YILDIZ ÇİZİM
import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#FF5733")
drawing_board.title("python turtle")

turtle_instance = turtle.Turtle()
for i in range(5):
    turtle_instance.right(144)
    turtle_instance.forward(100)
turtle.done()

POLYGON (ÇOK KENARLI) ÇİZİMİ

import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#FF5733")
drawing_board.title("python turtle")

turtle_instance = turtle.Turtle()
num_sides=8
angle = 360.0/ num_sides
side_length = 100
for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)
turtle.done()

KULLANICIYA TURTLE'I HAREKET ETTİRMEK

import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("turtle")

turtle_instance = turtle.Turtle()

def forward ():
    turtle_instance.forward(10)
def rotate_angle_left():
    turtle_instance.left(10)
def rotate_angle_right():
    turtle_instance.right(10)
def clear_screen():
    turtle_instance.clear()
def return_home():
    turtle_instance.home()
def pen_up():
    turtle_instance.penup()
def pen_down():
    turtle_instance.pendown()
drawing_board.listen()
drawing_board.onkey(fun=forward,key="space")
drawing_board.onkey(fun=rotate_angle_right,key="s")
drawing_board.onkey(fun=rotate_angle_left,key="w")
drawing_board.onkey(fun=clear_screen,key="c")
drawing_board.onkey(fun=return_home,key="h")
drawing_board.onkey(fun=pen_up,key="d")
drawing_board.onkey(fun=pen_down,key="a")

turtle.mainloop()

"""


class Team():

    def __init__(self,points,averages,scored_goals):
        self.points = points
        self.averages = averages
        self.scored_goals= scored_goals
        print("infos are identified ")
    def points_writer(self):
        print(self.points)

Beşiktaş = Team(100,89,44)

print(Beşiktaş.averages)
Beşiktaş.points_writer()

class Dog():
    year= 7

    def __init__(self,age):
        self.age = age
        self.doghumanage= age * self.year
    def dogs_age_related_to_human_age(self):
        print(self.age*self.year)
        # "self.year" yerine "Dog.year" da yazılabilir.

my_dog = Dog(3)
print(my_dog.age)
print(my_dog.doghumanage)
my_dog.dogs_age_related_to_human_age()


class Musician():
    def __init__(self,name):
        self.name=name
        print(("musician class"))
    def test1(self):
        print("test 1")
    def test2(self):
        print("test 2")

class MusicianPlus(Musician):
    def __init__(self,name):
        Musician.__init__(self,name)
        print("musicianplus")
    def test1(self):
        print("test1 test1 test1")

    def test3(self):
        print("test 3")

ibrahim= Musician("ibrahim")
print(type(ibrahim))
ibrahim.test1()
diyar= MusicianPlus("diyar")
diyar.test1()
diyar.test3()




"""
while 1==1: # 1==1 yerine "True"da yazabilirdik:
    try  :
        myAge = int(input("write your age please:"))
        print(myAge*2)
        break
    except ValueError: #burada ValueError yazmayabilirdik de 
        print("please write it as an integer")
    finally: # bunun altına yazdığın her durumda çalışacak
        print("finally")
"""

"""
******************************************************* Tkinter *******************************************************
from tkinter import *

#window
window = Tk()
window.title("Tkinter")
window.minsize(width=600,height=600)
window.config(pady=20,padx=20)

#label
label=Label()
label.config(text="The label",font=("Times New Roman",20,"bold"),padx=30,pady=30)
label.pack()


def Button_click():
    print(text.get(1.0,END))
#Button
button=Button()
button.config(text="The button",font=("Times New Roman",20,"bold"),command=Button_click)
button.pack()

#Entry
entry=Entry()
entry.config(width=20)
entry.pack()

#Text

text=Text()
text.config(width=30,height=5)
text.pack()
text.focus()

def number_selected(value):
    x=value
    print(f"My age is:{x}")

#Scale
scale = Scale()
scale.config(from_=0,to=50,command=number_selected)
scale.pack()

def spinbox_selcted():
    print(spinbox.get())
#Spinbox
spinbox=Spinbox()
spinbox.config(from_=0,to=50,command=spinbox_selcted)
spinbox.pack()


def checkbutton_selected():
    print(check_state.get())
#CheckButton
checkbutton=Checkbutton()
check_state=IntVar()
checkbutton.config(text="check",variable=check_state,command=checkbutton_selected)
checkbutton.pack()

#Radiobutton
def Radio_selected():
    print(radio_checked_state.get())

radio_checked_state = IntVar()
radiobutton=Radiobutton(text="1.option",value=10,variable=radio_checked_state,command=Radio_selected)
radiobutton_2=Radiobutton(text="2.option",value=20,variable=radio_checked_state,command=Radio_selected)
radiobutton.pack()
radiobutton_2.pack()

#Listbox
def listbox_selected(event):
    print(listbox.get(listbox.curselection()))
name_list=["Diyar","İbrahim","Oskan"]
listbox=Listbox(height=len(name_list)+1)
for i in range(len(name_list)):
    listbox.insert(i,name_list[i])
listbox.bind("<<ListboxSelect>>",listbox_selected)
listbox.pack()


window.mainloop()



from tkinter import *

window=Tk()
window.title("BMI Calculation")
window.minsize(width=300,height=300)
window.config(padx=50,pady=50)

#label1
label1 = Label()
label1.config(text="Enter your weight(kg)",pady=10)
label1.pack()

#entry1
entry1 = Entry()
entry1 .config(width=10)
entry1.pack()
entry1.focus()

#label2
label2=Label()
label2.config(text="Enter your height(cm)",pady=10)
label2.pack()

#entry2
entry2 = Entry()
entry2 .config(width=10)
entry2.pack()

def BMI_calculater():
    #kilo / (boy)^2

    x = float(entry1.get())
    y = float(entry2.get())
    i = x/ (y/100)**2

    if 0 < i <=18.5:
        print("underweight")
    elif 18.5 < i <= 24.5:
        print("normal weight")
    elif 24.5 < i <=29.9:
        print("overweight")
    elif 29.9 < i <= 39.9:
        print("obesity")
    elif i > 39.9:
        print("extreme obesity")

#button
button=Button()
button.config(text="calculate",width=10,command=BMI_calculater)
button.place(x=60,y=125)


mainloop()

"""
"""
###################### şifreli mesaj #####################
from tkinter import *
from PIL import Image, ImageTk
import base64
import os
from tkinter import messagebox

window = Tk()
window.title("Secret Notes")
window.minsize(width=300, height=300)
window.config(padx=50, pady=50)

#logo
image = Image.open("output.png")
image = image.resize((70, 70))  # 40x40 piksel
logo_image = ImageTk.PhotoImage(image)
logo_label = Label(image=logo_image)
logo_label.pack()


# label1
label1 = Label()
label1.config(text="Enter your title", pady=10)
label1.pack()

# entry1
entry1 = Entry()
entry1.config(width=20)
entry1.pack()
entry1.focus()

# label2
label2 = Label()
label2.config(text="Enter your secret", pady=10)
label2.pack()

# entry2
entry2 = Text()
entry2.config(width=20, height=10)
entry2.pack()

# label3
label3 = Label()
label3.config(text="Enter master key", pady=10)
label3.pack()

# entry3
entry3 = Entry()
entry3.config(width=20, show="*")  # Şifre gizlensin
entry3.pack()


def simple_encrypt_decrypt(text, key):
    encrypted_text = ""
    key_length = len(key)

    for i, char in enumerate(text):
        key_char = key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        encrypted_text += encrypted_char

    # Base64 encoding ile güvenli metin
    encrypted_bytes = encrypted_text.encode('latin-1')
    base64_encoded = base64.b64encode(encrypted_bytes).decode('latin-1')
    return base64_encoded


def simple_decrypt_encrypted(encrypted_text, key):
    try:
        # Base64 decoding
        encrypted_bytes = base64.b64decode(encrypted_text.encode('latin-1'))
        encrypted_text_decoded = encrypted_bytes.decode('latin-1')

        decrypted_text = ""
        key_length = len(key)

        for i, char in enumerate(encrypted_text_decoded):
            key_char = key[i % key_length]
            decrypted_char = chr(ord(char) ^ ord(key_char))
            decrypted_text += decrypted_char

        return decrypted_text
    except Exception as e:
        return None


def save_and_encrypt():
    title = entry1.get().strip()
    secret = entry2.get("1.0", END).strip()
    master_key = entry3.get().strip()

    # Validasyon
    if not title or not secret or not master_key:
        messagebox.showwarning("Warning", "Please fill all fields!")
        return

    if len(master_key) < 4:
        messagebox.showwarning("Warning", "Master key must be at least 4 characters!")
        return

    # Şifreleme
    encrypted_secret = simple_encrypt_decrypt(secret, master_key)

    # Dosyaya kaydet
    try:
        with open(f"{title}.txt", "w") as file:
            file.write(encrypted_secret)

        # Alanları temizle
        entry1.delete(0, END)
        entry2.delete("1.0", END)
        entry3.delete(0, END)
        entry1.focus()

        messagebox.showinfo("Success", "Your secret has been encrypted and saved!")

    except Exception as e:
        messagebox.showerror("Error", f"Could not save file: {e}")


def decrypt():
    title = entry1.get().strip()
    master_key = entry3.get().strip()

    if not title or not master_key:
        messagebox.showwarning("Warning", "Please enter title and master key!")
        return

    # Dosyayı oku
    try:
        with open(f"{title}.txt", "r") as file:
            encrypted_secret = file.read().strip()

        # Şifreyi çöz
        decrypted_secret = simple_decrypt_encrypted(encrypted_secret, master_key)

        if decrypted_secret is None:
            messagebox.showerror("Error", "Failed to decrypt! Check your master key.")
            return

        # Çözülmüş metni göster
        entry2.delete("1.0", END)
        entry2.insert("1.0", decrypted_secret)

        messagebox.showinfo("Success", "Secret decrypted successfully!")

    except FileNotFoundError:
        messagebox.showerror("Error", f"No file found with title: {title}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not decrypt: {e}")


# button1
button1 = Button()
button1.config(text="save & encrypt", command=save_and_encrypt)
button1.pack(pady=5)

# button2
button2 = Button()
button2.config(text="decrypt", command=decrypt)
button2.pack()

mainloop()
"""

