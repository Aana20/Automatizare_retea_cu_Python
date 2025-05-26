import yaml



from telnet_connection import telnet
from network_connection import  get_connection

def ping_submenu(connect, source_name, device_data):
    while True:
        print(f"\n[{source_name}] - Alege un dispozitiv către care vrei să faci ping:")
        for name in device_data:
            if name != source_name:
                print(f"→ {name}")

        target_device = input("Scrie numele dispozitivului destinație (sau 'exit'): ").strip()

        if target_device.lower() == "exit":
            break

        if target_device not in device_data:
            print("[!] Dispozitiv inexistent.")
            continue

        destination_ip = device_data[target_device]["ip"]
        command = f"ping {destination_ip}"
        output = connect.send_command(command)

        print(f"\n--- Ping către {target_device} ({destination_ip}) ---\n{output}")

        with open("ping_log.txt", "a", encoding="utf-8") as f:
            f.write(f"\n--- Ping de la {source_name} către {target_device} ({destination_ip}) ---\n")
            f.write(output + "\n")

        again = input("Vrei să mai testezi un alt dispozitiv? (da/nu): ").strip().lower()
        if again != "da":
            break
def connectivity():
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
              ping_submenu(network_connect, device_selected,device_data)
            elif device_selected == "MSW":
                info=device_data["MSW"]
                output=telnet(network_connect,info)
                ping_submenu(network_connect, device_selected,device_data)
            elif device_selected != "MSW":
                info = device_data["MSW"]
                output = telnet(network_connect, info)
                info_target=device_data[device_selected]
                output =telnet(network_connect, info_target)
                ping_submenu(network_connect,device_selected,device_data)
            else:
                print("Atat s-a putut")
        else:
            print("Dispozitivul nu exista in YAML. ")

