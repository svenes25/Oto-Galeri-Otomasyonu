Galeri=[]
Arac=[]
print("Galeriye Hoş Geldiniz\n")
while True:
    def Galeri_Genislet():
        with open("Galeri.txt","a+",encoding="utf-8") as galeri:
            for i in range(0,1):
                galeri.write("[] [] [] [] [] \n")
        print("Başarılı Bir Şekilde Yer Arttırıldı\n")
    def Galeri_Goster():
        def listele():
            print("     0     1     2     3     4 ")
            for i,e in enumerate(Galeri):
                print(i,e)
        global Galeri
        Galeri=[]
        with open("Galeri.txt","r",encoding="utf-8") as galeri:
            oku=galeri.readlines()
            for i in oku:
                sira=[]
                araba=i.split(" ")
                araba.pop()
                for i in araba:
                    sira.append(i)
                Galeri.append(sira)
        listele()
    def Galeri_Yazdır():
        with open("Galeri.txt","w",encoding="utf-8") as galeri:
            for i in Galeri:
                galeri.write("{} {} {} {} {} \n".format(i[0],i[1],i[2],i[3],i[4]))
    def Arac_Yazdır():
        with open("21100011020.txt","w",encoding="utf-8") as araba:
            for arac in Arac:
             araba.write("{}/{}/{}/{}/{}/{}/{}/\n".format(arac["MARKA"],arac["MODEL"],arac["PLAKA"],arac["FİYAT"],arac["YIL"],arac["SATIR"],arac["SUTUN"]))
    def Arac_Ekle_Sozluk(marka,model,plaka,fiyat,yıl,satir,sutun):
        arac={}
        arac["MARKA"]=marka
        arac["MODEL"]=model
        arac["PLAKA"]=plaka
        arac["FİYAT"]=fiyat
        arac["YIL"]=yıl
        arac["SATIR"]=satir
        arac["SUTUN"]=sutun
        Arac.append(arac)
        with open("21100011020.txt","a",encoding="utf-8") as araba:
            araba.write("{}/{}/{}/{}/{}/{}/{}/\n".format(arac["MARKA"],arac["MODEL"],arac["PLAKA"],arac["FİYAT"],arac["YIL"],arac["SATIR"],arac["SUTUN"]))
    def Arac_Ekle(marka,model,plaka,fiyat,yıl):
        Galeri_Goster()
        konum_X=int(input("Aracın Park Edileceği X Kordinatını Giriniz"))
        konum_Y=int(input("Aracın Park Edileceği Y Kordinatını Giriniz"))
        for i,e in enumerate(Galeri):
            for j,k in enumerate(e):
                if(i==konum_X and j==konum_Y):
                    if(Galeri[i][j]!="[+]"):
                        Galeri[i][j]="[+]"
                    else:
                        print("Seçilen Konumda Araba Bulunmaktadır\n")
                        Arac_Ekle(marka,model,plaka,fiyat,yıl)
        Galeri_Yazdır()
        Arac_Ekle_Sozluk(marka,model,plaka,fiyat,yıl,konum_X,konum_Y)
    def Arac_Listele():
        global Arac
        Arac=[]
        def listele():
            for i in Arac:
                print(i)
        with open("21100011020.txt","r",encoding="utf-8") as arac:
            oku=arac.readlines()
            for i in oku:
                arabalar={}
                araba=i.split("/")
                araba.pop()
                arabalar["MARKA"]=araba[0]
                arabalar["MODEL"]=araba[1]
                arabalar["PLAKA"]=araba[2]
                arabalar["FİYAT"]=araba[3]
                arabalar["YIL"]=araba[4]
                arabalar["SATIR"]=araba[5]
                arabalar["SUTUN"]=araba[6]
                Arac.append(arabalar)
        listele()
    def Plaka_Sorgu(plaka):
        SORGU=0
        for i in Arac:
            if(i["PLAKA"]==plaka):
                return i
            else:
                print("Araç Sorgulanıyorrrrr....\n")
        if(SORGU==0):
            print("Araç Bulunamadı\n")
    def Konum_Sorgu():
        Galeri_Goster()
        print("Bilgilerini Görmek İstediğiniz Aracın Konumlarını Giriniz\n")
        Konum_X=input("X Konumunu Giriniz ")
        Konum_Y=input("Y Konumunu Giriniz ")
        SORGU=0
        for i in Arac:
            if(i["SATIR"]==Konum_X and i["SUTUN"]==Konum_Y):
                return i
            else:
                print("Araç Sorgulanıyorrrr.....\n")
        if(SORGU==0):
            print("Araç Bilgileri Bulunamadı\n")
    def Arac_Guncelle(plaka):
        for i in Arac:
            if(i["PLAKA"]==plaka):
                print("1: Marka\n")
                print("2: Model\n")
                print("3: Plaka\n")
                print("4: Fiyat\n")
                print("5: Yıl\n")
                guncelle=input("")
                if(guncelle=="1"):
                    marka=input("Aracın Yeni Markasını Giriniz ")
                    i["MARKA"]=marka
                elif(guncelle=="2"):
                    model=input("Aracın Yeni Modelini Giriniz ")
                    i["MODEL"]=model
                elif(guncelle=="3"):
                    plaka=input("Aracın Yeni Plakasını Giriniz ")
                    i["PLAKA"]=plaka
                elif(guncelle=="4"):
                    fiyat=input("Aracın Yeni Fiyatını Gİriniz ")
                    i["FİYAT"]=fiyat
                elif(guncelle=="5"):
                    yil=input("Aracın Yeni Yılını Giriniz ")
                    i["YIL"]=yıl
        Arac_Yazdır()
    def Arac_Sil(plaka):
        for i in Arac:
            if(i["PLAKA"]==plaka):
                Arac.remove(i)
        Arac_Yazdır()
    print("1: Araç Ekle\n")
    print("2: Araç Listele\n")
    print("3: Araç Güncelle\n")
    print("4: Araç Sil\n")
    print("5: Araç Sorgulama\n")
    print("6: Galeri Göster\n")
    print("7: Galeri Yer Arttır\n")
    print("8: Çıkış\n")
    Secenek=input("")
    if Secenek=="1":
        marka=input("Araç Markasını Giriniz ")
        model=input("Araç Modelini Giriniz ")
        plaka=input("Araç Plakasını Giriniz ")
        fiyat=input("Araç Değerini Giriniz ")
        yıl=input("Araç Çıkış Yılını Giriniz ")
        Arac_Ekle(marka,model,plaka,fiyat,yıl)
        print("Araç Galeriye Eklendi\n")
    elif Secenek=="2":
        Arac_Listele()
    elif Secenek=="3":
        plaka=input("Güncellemek İstediğiniz Aracın Plakasını Giriniz ")
        Arac_Guncelle(plaka)
        print(plaka,"Plakalı Araç Güncellendi")
    elif Secenek=="4":
        plaka=input("Silmek İstediğniz Aracın Plakasını Giriniz ")
        Arac_Sil(plaka)
        print(plaka,"Plaka Araç Silindi")
    elif Secenek=="5":
        print("1: Plakadan Sorgulama\n")
        print("2: Konumdan Sorgulama\n")
        sorgu=input("")
        if(sorgu=="1"):
            plaka=input("Sorgulamak İstediğiniz Aracın Plakasını Giriniz\n")
            araba=Plaka_Sorgu(plaka)
            print(araba,"\n")
        elif(sorgu=="2"):
            e=Konum_Sorgu()
            print(e,"\n")
        else:
            print("Yanlış Sorgulama Girdiniz\n")
    elif Secenek=="6":
        Galeri_Goster()
    elif Secenek=="7":
        Galeri_Genislet()
        print("Galeri Genişletildi\n")
    elif Secenek=="8":
        print("Çıkış Yapılıyorrrrr.........")
        break
    else:
        print("Geçersiz Seçenek\n")