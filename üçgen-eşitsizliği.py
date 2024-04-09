
print("*****Üçgenin Çevresini Hesaplayalım*****")


a=int(input("üçgenin 1. kenar uzunluğunu yazınız="))
b=int(input("üçgenin 2. kenar uzunluğunu yazınız="))
c=int(input("üçgenin 3. kenar uzunluğunu yazınız="))
print("\t\t\t\tVerilen uzunluklar üçgen oluşturuyor mu inceleyelim")
print("\t\t\t\tüçgen eşitsizliği kuralı")
print("\t\t\t\tI(a-b)I<c<a+b")

if (abs(a-b)<c<a+b) and (abs(c-b) < a < c+ b)  and (abs(c-a) < b < c+ a):

     print("\t\t {}<{}<{}\n".format(abs(a - b), c, a + b),"doğru")
     print("\t\t {}<{}<{}\n".format(abs(c-b), a, c + b),"doğru")
     print("\t\t {}<{}<{}\n".format(abs(c - a), b, c + a),"doğru")
     print("------eşitsizlikler doğru olduğu için uzunluklar üçgen belirtir.-----")
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
     print("********üçgen çevresini bulalım={}\t".format(a+b+c))
else:
    print("------eşitsizlikler doğru olmadığı için üçgen belirtmez.çevre hesaplanamaz.-----")
