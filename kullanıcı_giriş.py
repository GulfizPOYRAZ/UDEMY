print("*****************"

      "Kullanıcı giriş proğramı"

      "*************\n")
print("******************   Abone kayıt işlemleri  *********************\n")
sys_kullanıcı=input("kullanıcı adınızı giriniz=")
sys_parola= input("paralonuzu giriniz= ")

print("kayıt işlemizi tamamlamak için enter tuşuna basınız.")
a=input("")
print("****************   kayıt işlerleriniz başarı ile tamamlanmıştır.\n")
print("\n")

giriş_sayısı=3
print("sisteme tekrar girmek için E ,çıkmak için H ye basınız.\n")

s=input("cevabınızı giriniz=")
if (s == "E"):
  while True:
   kullanıcı= input("kullanıcı adınızı giriniz=")
   parola= input("paralonuzu giriniz=")

   if (kullanıcı != sys_kullanıcı ) and (parola== sys_parola) :
       print("parola hatalı")
       giriş_sayısı -= 1
   elif (kullanıcı == sys_kullanıcı ) and (parola != sys_parola):
           print("parola hatalı")
           giriş_sayısı -= 1
   elif (kullanıcı!= sys_kullanıcı ) and (sys_parola != parola ):
            print("kullanıcı adı ve paralo hatalı")
            giriş_sayısı -= 1
   else:
       print("**********giriş yapıldı")
       break
   if (giriş_sayısı==0):
       print("**********giriş hakkı bitti")
       break
else:
    print("*****************sistemden çıkış gerçekleşmiştir.")