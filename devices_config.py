import yaml



from telnet_connection import telnet
from network_connection import  get_connection

def configuration_submenu(connect, device_name):
    while True:
        print(f"\n[ {device_name} ] - Ce vrei să configurezi?")
        print("1. Schimbă hostname")
        print("2. Creează VLAN")
        print("0. Înapoi la selecția dispozitivului")

        opt = input("Alege opțiunea: ")

        if opt == "1":
            hostname = input("Noul hostname: ")
            cmds = [f"hostname {hostname}"]
            output = connect.send_config_set(cmds)
            print(output)
        elif opt == "2":
            vlan = input("VLAN ID: ")
            name = input("Nume VLAN: ")
            cmds = [f"vlan {vlan}", f"name {name}"]
            output = connect.send_config_set(cmds)
            print(output)
        elif opt == "0":
            break
        else:
            print("Opțiune invalidă.")


def config():
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
           # r1=device_data["R1"]
            network_connect =get_connection(info)
            network_connect.enable()

            if device_selected == "R1" :
              configuration_submenu(network_connect, device_selected)
            elif device_selected == "MSW":
                info=device_data["MSW"]
                output=telnet(network_connect,info)
                configuration_submenu(network_connect, device_selected)
            elif device_selected != "MSW":
                info = device_data["MSW"]
                output = telnet(network_connect, info)
                info_target=device_data[device_selected]
                output =telnet(network_connect, info_target)
                configuration_submenu(network_connect,device_selected)
            else:
                print("Atat s-a putut")
        else:
            print("Dispozitivul nu exista in YAML. ")

