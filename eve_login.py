#pentru a face cereri HTTP
import requests

    #logarea catre eve ng
    # cred-username, parola + ce consola sa fie
    # cerere post cu date de  login
    # salveaza intr-o variabila cookie-urile primite de la server
    # return cookeis ca sa pot sa-l folosesc in  main , altfel da null la cokies
def login_eve():
    url_login= 'http://192.168.238.128/api/auth/login'
    authentication='{"username":"admin","password":"eve","html5" : "1"}'
    #headers = {'Content-Type': 'application/json'}  -merge si fara
    login=requests.post(url=url_login,data=authentication)
    cookies =login.cookies
    if login.status_code==200:
        print("Autentificare EVE-NG reușita.")
        return cookies
        print(cookies)
    else:
        print("Autentificare EVE-NG  esuata")
        return None



#pentru verificare status  nod
def node_status_check_stop(cookies,node_name,lab_path="/Licenta/Automatizare.unl",eve_ip="192.168.238.128"):
    node_url=f"http://{eve_ip}/api/labs{lab_path}/nodes"
    n=cookies.get(node_url)
    if n.status_code != 200:
        print("Eroare la accesarea nodurilor din lab.")
        return False

    nodes = n.json()["data"]

    for node_id, node in nodes.items():
        if node["name"].strip().upper() == node_name.strip().upper():
            return node["status"] == 2

    print(f"[!] Nodul {node_name} nu a fost găsit.")
    return False

