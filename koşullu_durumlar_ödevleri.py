print("**********PROBLEM 1 **********\n")
print("\t\tBKİ HESAPLAMASI VE DEĞERLENDİRİLMESİ\n")
kilo=float(input("Kilonuzu giriniz= "))
boy=float(input("Boyunuzu giriniz= "))
if (boy<3):
    islem1=kilo/(boy**2)
    bki=islem1
else:
    islem2=kilo/(boy**2)*10000
    bki=islem2

if  (bki<=18.5) :
       print("BKİ= {}\t".format(bki),"............Zayıf\n")
elif (bki<=25) :
       print("BKİ= {}\t".format(bki), "............Normal\n")
elif(bki<= 30) :
        print("BKİ= {}\t".format(bki),"..........Fazla kilolu\n")
else:
     print("BKİ= {}\t".format(bki), ".............Obez\n\n")

print("**********PROBLEM 2 **********\n")
print("\t\t****SAYILARIN KARŞILAŞTIRILMASI****\n")
a=float(input("A sayısını giriniz="))
b=float(input("B sayısını giriniz="))
c=float(input("C sayısını giriniz="))
if(a==b==c):
     print("{}={}={}".format(a, b, c), "a=b=c\n")
elif (a>b) and (a>c):
    print("En büyük sayı={}\t".format(a),)
    if(b>c):
         print("{}>{}>{}".format(a, b, c), "a>b>c\n")
    else :
     print("{}>{}>{}".format(a, c, b), "a>c>b\n")

elif(b>a) and (b>c) :
     print("En büyüksayı={}\t".format(b),)
     if (a>c) :
         print("{}>{}>{}\t".format(b,a,c),"b>a>c\n")
     else:
        print("En büyüksayı={}\t".format(b),)
        print("{}>{}>{}".format(b,c,a),"b>c>a\n")
elif (c>a) and (c>b) :
    print("En büyüksayı={}\t".format(c),)
    if (a>b):
        print("{}>{}>{}".format(c, a, b), "c>a>b\n")
    else:
        print("En büyüksayı={}\t".format(a),)
        print("{}>{}>{}".format(c,b,a),"c>b>a\n")
        

print("**********PROBLEM 3 **********\n")
print("\t\tDERS GEÇME NOTU HESAPLAMA\n")

a=int(input("1.Vize notunuz="))
b=int(input("2.Vize notunuz="))
c=int(input(" Final notunuz="))
toplam=(a+b)*0.3+(c*0.4)

if toplam>=90:
    print("Geçme notu:{}".format(toplam),"********AA\n")
elif(toplam>=85):
    print("Geçme notu:{}".format(toplam), "********BA\n")
elif (toplam >= 80):
    print("Geçme notu:{}".format(toplam), "********BB\n")
elif (toplam >= 75):
    print("Geçme notu:{}".format(toplam), "********CB\n")
elif (toplam >= 70):
    print("Geçme notu:{}".format(toplam), "********CC\n")
elif (toplam >= 65):
    print("Geçme notu:{}".format(toplam), "********DC\n")

elif (toplam >= 60):
    print("Geçme notu:{}".format(toplam), "********DD\n")
elif (toplam >= 55):
    print("Geçme notu:{}".format(toplam), "********FD\n")
elif (toplam < 50):
     print("Geçme notu:{}".format(toplam), "********FF\n")


print("**********PROBLEM 4 **********\n")
print("\t\tÇOKGENLERİN ÇEVRE HESPLAMASI\n")
print("**********üçgen veya dörtgen çevresini hesaplıyoruz.:):):):):)*********\n")
p = int(input("Kaç kenarlı çokgenin çevresini hesplamak istiyorsunuz?p= "))
if p==3:
    print("üçgenin çevresini hesaplayalım")
    a = int(input("üçgenin 1. kenar uzunluğunu yazınız.a="))
    b = int(input("üçgenin 2. kenar uzunluğunu yazınız.b="))
    c = int(input("üçgenin 3. kenar uzunluğunu yazınız.c="))
    print("\t\t\t\tVerilen uzunluklar üçgen oluşturuyor mu ? inceleyelim\n")
    print("\t\t\t\tüçgen eşitsizliği kuralı\n")
    print("\t\t\t\tI(a-b)I<c<a+b\n")

if (abs(a - b) < c < a + b) and (abs(c - b) < a < c + b) and (abs(c - a) < b < c + a): 
     print("\t\t {}<{}<{}\n".format(abs(a - b), c, a + b))
     print("\t\t {}<{}<{}\n".format(abs(c - b), a, c + b))
     print("\t\t {}<{}<{}\n".format(abs(c - a), b, c + a))
     print("------eşitsizlikler doğru olduğu için uzunluklar üçgen belirtir.-----\n")
     if ((a == b) and (a != c) and (b != c)):
         print("********üçgenimiz : ikizkenar üçgen  ******\n")
     elif((a == c) and (a != b) and (c!= b)):
         print("********üçgenimiz : ikizkenar üçgen  ******\n")
     elif ((b == c) and (b != a) and (c != a)):
         print("********üçgenimiz : ikizkenar üçgen  ******\n")
     elif (a == b == c):
         print("********üçgenimiz : eşkenar üçgen  ******\n")
     else:
         print("********üçgenimiz : çeşitkenar üçgen  ****** \n")
     print("********üçgen çevresini bulalım={}\t".format(a + b + c))
else:
     print("------eşitsizlikler doğru olmadığı için üçgen belirtmez.çevre hesaplanamaz.-----\n")
if (p == 4):
    print("dörtgenin çevresini hesaplayalım ")
    a = int(input("dörtgenin 1. kenar uzunluğunu yazınız="))
    b = int(input("dörtgenin 2. kenar uzunluğunu yazınız="))
    c = int(input("dörtgenin3. kenar uzunluğunu yazınız="))
    d = int(input("dörtgenin 4. kenar uzunluğunu yazınız="))

    print("********dörtgenin çevresini bulalım={}\t".format(a + b + c + d))
else:
    print("kenar sayısını 3 veya 4 olarak giriniz!!!!!\n") 
print("*********TEBRİKLER********")
