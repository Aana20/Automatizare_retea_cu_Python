import yaml
from requests import session


from telnet_connection import telnet
from network_connection import  get_connection


#se face citrea din  fisierul .yaml
with open('details_devices.yaml', 'r') as file:
    device_data=yaml.safe_load(file)

#Meniul principal pentru untilizator
print("\n   Acesta este meniul pentru utilizatori  \n")
print("#### Ce ai vrea sa faci ? ####\n")
print("1.Acceseaza un dispozitiv")
print("2.Iesire")

option=input("Alege o optiune (1-2) : ")

if option=="1":
    #afisam lista de dispozitive din .yaml
    print("\n## Dispozitivele disponibile sunt ##: ")
    for device_name in device_data:
        print(f"->{device_name}")

    device_selected =input("Alege un dispozitiv : ")

    #daca cel selectat e in lista mea
    if device_selected in device_data:
        info=device_data[device_selected] #in variabila info se preiau datele despre device-ul selectat
        r1=device_data["R1"]
        network_connect =get_connection(r1)
        network_connect.enable()

        if device_selected == "R1" :
           #output=network_connect.send_command("show ip int brief")
           output=network_connect.send_config_from_file('show_test.txt')
           #print(output)
           with open("raport_output.txt", "a") as f:
               f.write(f"\n--- Output pentru {device_selected} ---\n")
               f.write(output)
               f.write("\n\n")
        elif device_selected == "MSW":
            info=device_data["MSW"]
            output=telnet(network_connect,info)
            #output+=network_connect.send_command('show ip int brief')
            #print(output)
            with open("raport_output.txt", "a") as f:
                f.write(f"\n--- Output pentru {device_selected} ---\n")
                f.write(output)
                f.write("\n\n")
        elif device_selected != "MSW":
            info = device_data["MSW"]
            output = telnet(network_connect, info)

            info_target=device_data[device_selected]
            output =telnet(network_connect, info_target)
            if output:
                output += network_connect.send_command("show ip int brief")
                print(output)
            else:
                print("\nNu s-a realizat conexiunea Telnet. Nu se trimit comenzi.")

        else:
            print("Atat s-a putut")
    else:
        print("Dispozitivul nu exista in YAML. ")
#pentru optiunea 2
elif option == "2":
    print("\n   Iesire ")
#daca nu se introduce o optiune valida
else:
    print("\n Optiune invalida.  ")