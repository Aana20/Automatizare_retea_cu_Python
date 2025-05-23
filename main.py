

from eve_login import login_eve
from teste.conectare_la_dispozitive import telent_R1


#Meniul pentru utilizator



cookies =login_eve()

if cookies.get_dict():
    print("[Main] Continuăm cu automatizarea dispozitivelor.")
    telent_R1()
else:
    print("[Main] Automatizarea nu poate continua fără autentificare.")