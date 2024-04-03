p=int(input("üçgenin çevresini hesplamak istiyorsunuz? ="))


print("üçgenin çevresini hesaplayalım")
a=int(input("üçgenin 1. kenar uzunluğunu yazınız="))
b=int(input("üçgenin 2. kenar uzunluğunu yazınız="))
c=int(input("üçgenin 3. kenar uzunluğunu yazınız="))
print("\t\t\t\tVerilen uzunluklar üçgen oluşturuyor mu ? inceleyelim")
print("\t\t\t\tüçgen eşitsizliği kuralı")
print("\t\t\t\tI(a-b)I<c<a+b")

if (abs(a-b)<c<a+b) and (abs(c-b) < a < c+ b)  and (abs(c-a) < b < c+ a):

     print("\t\t {}<{}<{}\n".format(abs(a - b), c, a + b))
     print("\t\t {}<{}<{}\n".format(abs(c-b), a, c + b))
     print("\t\t {}<{}<{}\n".format(abs(c - a), b, c + a))
     print("------eşitsizlikler doğru olduğu için uzunluklar üçgen belirtir.-----")
     print("********üçgen çevresini bulalım={}\t".format(a+b+c))
else:
    print("------eşitsizlikler doğru olmadığı için üçgen belirtmez.çevre hesaplanamaz.-----")
if p==4 :
    print("dörtgenin çevresini hesaplayalım ")

