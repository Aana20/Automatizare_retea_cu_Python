#  Automatizarea procesului de administrare a unei rețele de calculatoare folosind scripturi Python



## Cuprins

* [Introducere](#introducere)
* [Motivația Proiectului](#motivația-proiectului)
* [Arhitectură și Topologie](#arhitectură-și-topologie)
* [Funcționalități](#funcționalități)
* [Instalare și Configurare](#instalare-și-configurare)
* [Utilizare (Exemple de Rulare)](#utilizare-exemple-de-rulare)
* [Rezultate și Demonstrație](#rezultate-și-demonstrație)
* [Contribuție și Licență](#contribuție-și-licență)
* [Contact](#contact)

---

## Introducere

Această secțiune oferă o prezentare generală a proiectului.

Proiectul abordează provocările legate de complexitatea și administrarea manuală a rețelelor moderne. Prin dezvoltarea unui set de scripturi Python, se urmărește eficientizarea operațiunilor de rețea, reducerea erorilor umane și îmbunătățirea scalabilității. Implementarea și testarea au fost realizate într-un mediu de emulare EVE-NG.

## Motivația Proiectului


* **Context actual:** Evoluția rapidă a infrastructurilor IT și complexitatea crescută a rețelelor necesită soluții eficiente de administrare.
* **Provocări:** Administrarea manuală este consumatoare de timp, predispusă la erori și dificil de scalat.
* **Obiectiv:** Dezvoltarea unei soluții practice pentru automatizarea proceselor repetitive și critice în rețelistică.
* **Interes personal:** Consolidarea cunoștințelor în rețelistică și Python, asimilarea de noi competențe în automatizare.

## Arhitectură și Topologie



* **Platforma de Emulare:** EVE-NG (Environments for Virtualized Network Emulation) a fost utilizată pentru simularea detaliată a infrastructurii de rețea.
* **Topologia Rețelei:** Prezintă o diagramă simplificată a topologiei.
    * Laptop fizic (unde rulează scripturile Python).
    * Conexiune SSH către echipamentele virtuale (routere, switch-uri) din EVE-NG.
    * **Exemplu diagramă:**
        ```
        Laptop (Script Python) ----SSH----> Router R1 (EVE-NG)
                                     |
                                     |____Other Devices (Switches, Servers, etc.)
        ```

## Funcționalități


* **Configurare inițială a dispozitivelor:**
    * Setare hostname, parole.
    * Configurare interfețe (adrese IP, starea porturilor).
    * Creare VLAN-uri.
* **Gestionarea conectivității:**
    * Configurare rute statice/dinamice (dacă e cazul).
    * Verificări de conectivitate (ping, traceroute).
* **Monitorizare:**
    * Colectarea informațiilor despre starea interfețelor.
    * Verificarea tabelului de rute.
    * Vizualizarea log-urilor (dacă e implementat).
* **Alte funcționalități:** (ex: backup configurații, restart servicii, etc.)

## Instalare și Configurare

Pnetru a rula proiectul e nevoie si de EVE-NG

### Pre-rechizite:

* Python 3.x instalat (recomandat 3.8+).
* Acces la un mediu EVE-NG (versiunea Community sau Professional).
* Biblioteci Python necesare (ex: `paramiko`, `netmiko`, `requests`).
    ```bash
    pip install paramiko netmiko requests
    ```

### Pași de instalare:

1.  **Clonează depozitul GitHub:**
    ```bash
    git clone [https://github.com/nume_utilizator/nume_repo.git](https://github.com/nume_utilizator/nume_repo.git)
    cd nume_repo
    ```
2.  **Configurare EVE-NG:**
    * Asigură-te că ai o topologie configurată în EVE-NG cu routere/switch-uri accessibile prin SSH.
    * Notează adresele IP ale echipamentelor și credențialele de autentificare.
3.  **Configurare scripturi:**
    * Editează fișierul de configurare (ex: `config.py` sau direct în scripturi) pentru a introduce adresele IP, username-urile și parolele echipamentelor tale.
    * *Exemplu:*
        ```python
        DEVICES = {
            "router1": {"host": "192.168.238.254", "username": "admin", "password": "password"},
            # Adaugă și alte echipamente
        }
        ```

## Utilizare (Exemple de Rulare)

Cum se folosesc scripturile.

* **Exemplu 1: Rularea scriptului de configurare inițială:**
    ```bash
    python configure_router.py
    ```
 
* **Exemplu 2: Rularea scriptului de verificare a stării interfețelor:**
    ```bash
    python check_interfaces.py
    ```
  


## Rezultate și Demonstrație



* Scripturile au demonstrat o **reducere semnificativă a timpului de configurare** și a erorilor.
* **Fiabilitatea** operațiunilor a crescut.

