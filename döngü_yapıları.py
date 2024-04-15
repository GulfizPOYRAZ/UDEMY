print("*********  döngü yapıları 1.problemler********\n")
print("***** mükemmel sayıyı bulalım ******\n")
sayı= int(input("sayı_giriniz= "))
i=1
top=0
for i in range (1,sayı):
        if(sayı%i==0):
            top+=i
            print("bölen sayıları= {}".format(i))
top==top
if (top == sayı):
           print("mükemmel sayı ")
           print("bölen sayıların toplamı= {}".format(top))
elif(top != sayı):
 print("mükemmel sayı değil ")
print(" ****yeni probleme geçmek için enter a basınız\n")
geç= input(" ")

print("************* problem 2 ********\n")
print("******** Armstrong sayısı ******\n")
print("verilen sayının armstrong sayısı olup olmaığının bulunması ")
sayı= input("sayı:")
bas_say= len(sayı)
sayı=int(sayı)
bas=0
top=0
geçici_sayı= sayı
while(geçici_sayı>0) :
    bas = geçici_sayı % 10
    top += bas ** bas_say
    geçici_sayı //= 10
    print(geçici_sayı)
print(top)
if (top==sayı):
    print("********* {}".format(int(sayı)), "sayımız armstrong sayısıdır.***********\n")
else:
    print("*********{}".format(int(sayı)), "sayımız armstrong sayısı değildir.**********\n")
print(" ****yeni probleme geçmek için enter a basınız\n")
geç= input(" ")
print("************* problem 3 ********\n")
print("******** çarpım tablosu ******\n")
i=1
j=1
for j in range(1,11):
    print("\t\t\t\t\t{}".format(j),"lerin çarpım tablosu\n")
    for i in range(1,11):
      
      print("\t{}x{}={}".format(i, j, i * j),"\t\t\t*-------*","\t\t\t{}x{}={}".format(j, i, i * j))
print(" ****yeni probleme geçmek için enter a basınız\n")
geç= input(" ")

print("************* problem 4 ********\n")
print("**** while döngüsünü break ile sonlandırma ***\n")
top= 0
while True :
    print("çıkmak için q' a basabilirsiniz")
    sayı = input("sayı gir= ")
    if (sayı =="q"):
      break
    sayı = int(sayı)
    top+= sayı
    print("\t\t\t\t\ttop =  ",top)
print(" ****yeni probleme geçmek için enter a basınız\n")
geç= input(" ")
print("************* problem 5 ********\n")
print("**** 3'e bölünen sayıları *continue* ile bulma ****\n")
liste = []
while True:
    for i in range(1, 101):
        if (i % 3 == 0):
            liste.append(i)
            print(liste)
        continue
    break
print(" ****yeni probleme geçmek için enter a basınız\n")
geç= input(" ")
print("************* problem 6 ********\n")
print("****  list comprehension kullanarak 1'den 100'e sedece çift sayıları bir listeye atmayı******\n")
liste = []
while True:
    for i in range(1, 101):
        if (i % 2 == 0):
            liste.append(i)
            print(liste)
        continue

    break

geç= input(" ")
print (" :):):):) ***  T E B R İ K L E R  *** :):):):)")
