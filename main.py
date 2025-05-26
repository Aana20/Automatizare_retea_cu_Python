

from devices_information import  information
from devices_config import config
from devices_connectivity import connectivity
#Meniul pentru utilizator
def show_meniu():
    print("\n   Acesta este meniul pentru automatizarea retelei   \n")
    print("#### Ce ai vrea sa faci/verifici ? ####\n")
    print("1.Acceseaza informatii despre un dispozitiv")
    print("2.Configureaza un dispozitiv (ex. hostname ,vlan)")
    print("3.Teste de conectivitate (ping/depanare)")
    print("4.Schimba parola sau adresa IP a unui dispozitiv")
    print("5.Verifica daca dispozitivele sunt pornite/oprite")
    print("6.Iesire din meniul principal")

    #option=input("\nAlege o optiune (1-6) : ")

while True:
    show_meniu()
    option = input("\nAlege o optiune (1-6) : ")
    if option=="1":
        while True:
            information()
            print("Verifica raport.txt")
            iesire = input("Vrei sa faci alt ceva? (da/nu)  : ")
            if iesire == "nu":
                break
    elif option=="2":
        while True:
            config()
            print("Verifica raport.txt")
            iesire = input("Vrei sa faci alt ceva? (da/nu)  : ")
            if iesire == "nu":
                break
    elif option=="3":
        while True:
            connectivity()
            iesire = input("Vrei sa faci alt ceva? (da/nu)  : ")
            if iesire == "nu":
                break
    else :
        break



