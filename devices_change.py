from idlelib.config import idleConf

import yaml



from telnet_connection import telnet
from network_connection import  get_connection

def config_device_submenu(connect, device_name):
    while True:
        print(f"\n[{device_name}] - Ce vrei să schimbi?")
        print("1. Parola de exec (enable)")
        print("2. Parola linie VTY")
        print("3. Adresa IP a unei interfețe")
        print("0. Înapoi")

        opt = input("Alege opțiunea: ").strip()

        if opt == "1":
            parola = input("Noua parola pentru enable: ")
            cmds = [
                "enable secret " + parola
            ]
        elif opt == "2":
            parola = input("Noua parola VTY: ")
            cmds = [
                "line vty 0 4",
                f"password {parola}",
                "login",
                "exit"
            ]
        elif opt == "3":
            interfata = input("Interfața (ex: FastEthernet0/1): ")
            ip = input("Noua adresă IP: ")
            mask = input("Mască (ex: 255.255.255.0): ")
            cmds = [
                f"interface {interfata}",
                f"ip address {ip} {mask}",
                "no shutdown",
                "exit"
            ]
        elif opt == "0":
            break
        else:
            print("Opțiune invalidă.")
            continue

        output = connect.send_config_set(cmds)
        print(output)

        with open("config_log.txt", "a", encoding="utf-8") as f:
            f.write(f"\n--- Modificare pe {device_name} ---\n")
            f.write("\n".join(cmds) + "\n")
            f.write(output + "\n")

def modify_device_config():
#se face citrea din  fisierul .yaml
    with open('details_devices.yaml', 'r') as file:
        device_data=yaml.safe_load(file)


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
              config_device_submenu(network_connect, device_selected)
            elif device_selected == "MSW":
                info=device_data["MSW"]
                output=telnet(network_connect,info)
                config_device_submenu(network_connect, device_selected)
            elif device_selected != "MSW":
                info = device_data["MSW"]
                output = telnet(network_connect, info)
                info_target=device_data[device_selected]
                output =telnet(network_connect, info_target)
                config_device_submenu(network_connect,device_selected)
            else:
                print("Atat s-a putut")
        else:
            print("Dispozitivul nu exista in YAML. ")

