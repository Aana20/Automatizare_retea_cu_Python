from netmiko import ConnectHandler
#functia pentru conectarea la router ,care principalul la care trebuie conectat
def get_connection(router):
    return ConnectHandler(
        device_type=router['device_type'],
        host=router['ip'],
        username=router['user_ssh'],
        password=router['password_ssh'],
        secret=router['password_privileged_mod']
    )