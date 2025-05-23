import time

def telnet(network_connect,info):
    try:
        output = network_connect.send_command_timing(f"telnet {info['ip']}")
        if "Password" in output:
             output += network_connect.send_command_timing(info["password_telnet"])

         # Intri in exec mode pe dispozitiv
        output += network_connect.send_command_timing("enable")
        if "Password" in output:
            output += network_connect.send_command_timing(info["password_privileged_mod"])
            return output
    except Exception as e:
        print(f"[Exceptie] Eroare la Telnet catre {info['ip']}: {e} ")
        return None