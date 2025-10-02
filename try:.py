try: 
    pikkus=float(input("Palun anna pikkus meetrites:"))    
    laius=float(input("Palun anna laius meetrites:"))
    if pikkus>0 and laius>0:
        pindala=pikkus*laius
    print("pindala on ", pindala, "ruutmeetrit")
    vastus=input("Kas soovid remonti teha? (jah/ei)")
    if vastus== "jah":
        print("Suurepärane, hakkame pihta!")
        ruutmeeter=float(input("Milline on ruutmeetri hind?"))
        if ruutmeeter>0:
            maatulu=pindala*ruutmeeter
            print("Hinnaks on ", maatulu, "eurot")

    elif vastus== "ei":
        print("Teeme siis hiljem")

except:
    print("Palun sisesta õige info, mis on seotud andmetega!")