print("******* Hangi yıl şubat ayı 29 gündür ?*********\n")
def artık(yıl):

    if (yıl%4==0):

         print("------->  {}".format(yıl),"yılı şubat ayı 29 gündür.")
    else:
        print("------->  {}".format(yıl),"yılı şubat ayı 28 gündür.")

yıl =int(input("\t\t\tyıl giriniz = "))
artık(yıl)
