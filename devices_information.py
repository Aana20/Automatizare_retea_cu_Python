import yaml



from telnet_connection import telnet
from network_connection import  get_connection

def information_submenu(connect, device_name):
    while True:
        print(f"\n[ {device_name} ] - Ce informație dorești?")
        print("1. Status porturi")
        print("2. VLAN-uri")
        print("3. Versiune")
        print("0. Înapoi la selecția dispozitivului")

        opt = input("Alege opțiunea: ")

        if opt == "1":
            output = connect.send_command("show ip int brief")
            with open("raport_output.txt", "a") as f:
                f.write(f"\n--- Output pentru {device_name} (optiunea {opt}) ---\n")
                f.write(output)
                f.write("\n")
        elif opt == "2":
            output =connect.send_command("show vlan brief")
            with open("raport_output.txt", "a") as f:
                f.write(f"\n--- Output pentru {device_name} (optiunea {opt}) ---\n")
                f.write(output)
                f.write("\n")
        elif opt == "3":
            output = connect.send_command("show version")
            with open("raport_output.txt", "a") as f:
                f.write(f"\n--- Output pentru {device_name} (optiunea {opt}) ---\n")
                f.write(output)
                f.write("\n")
        elif opt == "0":
            break
        else:
            print("Opțiune invalidă.")

def information():
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
              information_submenu(network_connect, device_selected)
            elif device_selected == "MSW":
                info=device_data["MSW"]
                output=telnet(network_connect,info)
                information_submenu(network_connect, device_selected)
            elif device_selected != "MSW":
                info = device_data["MSW"]
                output = telnet(network_connect, info)
                info_target=device_data[device_selected]
                output =telnet(network_connect, info_target)
                information_submenu(network_connect,device_selected)
            else:
                print("Nu s-a facut conexiunea")
        else:
            print("Dispozitivul nu exista in YAML. ")

