from netmiko import ConnectHandler

def telent_R1():
    R1={
        'device_type': 'cisco_ios',
        'host': '192.168.238.254',
        'username': 'ssh_R1',
        'password': 'R1',
        'secret': 'privilegiat_R1'  # parola de privileged EXEC mode
    }
    net_connect = ConnectHandler(**R1)
    net_connect.enable()
    output = net_connect.send_command_timing('telnet 192.168.10.1')
    output += net_connect.send_command_timing('telnet_MSW')
    output += net_connect.send_command_timing('enable')
    output += net_connect.send_command_timing('privilegiat_MSW')
    output += net_connect.send_command('show ip int brief')
    output += net_connect.send_command_timing('telnet 192.168.10.6')
    output += net_connect.send_command_timing('telnet_ST')
    output += net_connect.send_command_timing('enable')
    output += net_connect.send_command_timing('privilegiat_ST')
    output += net_connect.send_command('show ip int brief')
    print("Output de la msw+sw_st : ")
    print(output)
    print("[R1] Conectat.")
