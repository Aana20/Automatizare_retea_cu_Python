import yaml
from netmiko import ConnectHandler

# Citim detaliile din YAML
with open("../details_devices.yaml") as f:
    device_data = yaml.safe_load(f)

# Meniu principal
print("\n=== Ce vrei sa faci? ===")
print("1. Acceseaza un dispozitiv si ruleaza comanda")
print("2. Iesi")
opt = input("Alege optiunea (1-2): ")

if opt == "1":
    # Lista de dispozitive
    print("\n=== Dispozitive disponibile ===")
    for dev_id in device_data:
        print(f"- {dev_id}")


    selected = input("\nAlege un dispozitiv (ex: SW1_ST): ")

    if selected in device_data:
        info = device_data[selected]

        # Conectare la R1 (presupunem ca e mereu punctul de intrare)
        r1 = device_data["R1"]
        net_connect = ConnectHandler(
            device_type=r1["device_type"],
            host=r1["ip"],
            username=r1["username"],
            password=r1["password"],
            secret=r1["secret"]
        )
        net_connect.enable()

        # Telnet la MSW si apoi la dispozitivul ales
        output = net_connect.send_command_timing(f"telnet {info['via_msw']}")
        if "Password" in output:
            output += net_connect.send_command_timing(info["telnet_pass"])

        # Intri in exec mode pe dispozitiv
        output += net_connect.send_command_timing("enable")
        if "Password" in output:
            output += net_connect.send_command_timing(info["secret"])

        # Afisare lista de comenzi
        print("\nComenzi disponibile:")
        cmds = ["show ip interface brief", "show version", "show vlan"]
        for i, c in enumerate(cmds, 1):
            print(f"{i}. {c}")
        cmd_opt = int(input("Alege comanda (1-3): "))

        final_output = net_connect.send_command(cmds[cmd_opt - 1])
        print("\n=== Rezultatul comenzii ===")
        print(final_output)

        net_connect.disconnect()
    else:
        print("Dispozitivul nu exista in YAML.")

elif opt == "2":
    print("Iesire...")
else:
    print("Optiune invalida.")
