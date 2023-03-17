"""
Author: new92
Github: @new92

Script for displaying info for players, clans, leagues etc. in the famous game: Clash of Clans.
"""

try:
    import sys
    import platform
    from os import system
    from time import sleep
    import json
    import requests
    import os
except ImportError as imp:
    print("[!] WARNING: Not all packages used in this script have been installed !")
    sleep(2)
    print("[+] Ignoring warning...")
    sleep(1)
    if sys.platform.startswith('linux'):
        if os.geteuid() != 0:
            print("[!] Root user not detected !")
            sleep(2)
            print("[+] Trying to enable root user...")
            sleep(1)
            system("sudo su")
            try:
                system("sudo pip install -r requirements.txt")
            except Exception as ex:
                print("[!] Error !")
                sleep(1)
                print(ex)
                sleep(2)
                print("[+] Exiting...")
                quit(0)
        else:
            system("sudo pip install -r requirements.txt")
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")

headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer <ENTER YOUR API KEY HERE>'
}

def ProgInfo():
    if platform.system() == 'Windows':
        system("cls")
    else:
        system("clear")
    author = 'new92'
    lice = 'MIT'
    f = "/Supercell/ClashRoyale/RoyaleInfo.py"
    if os.path.exists(os.path.abspath(f)):
        fsize = (os.stat(f)).st_size
    else:
        fsize = 0
    lang = 'Python'
    language = 'en-US'
    name = 'ClashofInfo'
    api = 'Clash of Clans API'
    api_url = 'https://developer.clashofclans.com/#/login'
    lines = 553
    stars = 6
    forks = 4
    print(f"[+] Author: {author}")
    print(f"[+] Github: @{author}")
    print(f"[+] License: {lice}")
    print(f"[+] Programming language(s) used: {lang}")
    print(f"[+] Language(s): {language}")
    print(f"[+] Program's name: {name}")
    print(f"[+] Lines of code: {lines}")
    print(f"[+] API used: {api}")
    print(f"[+] URL: {api_url}")
    print(f"[+] File size: {fsize} bytes")
    print(f"[+] Github repo stars: {stars}")
    print(f"[+] Github repo forks: {forks}")

ANS = ["yes","YES","Yes","y","Y","YeS","yEs","YEs","yES"]
NANS = ["no","NO","No","n","N","nO"]


def Player(tag: str):
    if platform.system() == 'Windows':
        system("cls")
    else:
        system("clear")
    tag = tag.upper()
    war = ''
    page = requests.get(f"https://api.clashofclans.com/v1/players/%23{tag}", headers=headers)
    if page.status_code == 200:
        js = page.json()
        if js['role'] == 'admin':
            role = 'Elder'
        elif js['role'] == 'coLeader':
            role = 'Co-Leader'
        else:
            role = 'Leader'
        print("-" * 45)
        print(f"[+] Name: {js['name']}")
        print(f"[+] Townhall level: {js['townHallLevel']}")
        print(f"[+] Experience level: {js['expLevel']}")
        print(f"[+] Number of trophies (in Home Village): {js['trophies']}")
        print(f"[+] Highest number of trophies from multiplayer battles player reached: {js['bestTrophies']}")
        print(f"[+] Stars from war: {js['warStars']}")
        print(f"[+] Attack wins: {js['attackWins']}")
        print(f"[+] Defence wins: {js['defenseWins']}")
        print(f"[+] Builderhall level: {js['builderHallLevel']}")
        print(f"[+] Number of trophies (Builder Base): {js['versusTrophies']}")
        print(f"[+] Highest number of trophies from versus battles player reached: {js['bestVersusTrophies']}")
        print(f"[+] Versus battles - number of wins: {js['versusBattleWins']}")
        print(f"[+] Player's role in clan: {role}")
        print(f"[+] Donations made: {js['donations']}")
        print(f"[+] Troops received: {js['donationsReceived']}")
        print(f"[+] Clan capital contributions: {js['clanCapitalContributions']}")
        print(f"[+] Clan's tag: {js['clan']['tag']}")
        print(f"[+] Clan's name: {js['clan']['name']}")
        print(f"[+] Clan's level: {js['clan']['clanLevel']}")
        print(f"[+] Clan's icon: {js['clan']['badgeUrls']['medium']}")
        print(f"[+] Total number of versus battles wins: {js['versusBattleWinCount']}")
        print("-"*10+"labels".upper()+"-"*10)
        if len(js['labels']) != 0:
            for i in range(len(js['labels'])):
                print(f"[+] Name: {js['labels'][i]['name']}")
                print(f"[+] Icon: {js['labels'][i]['iconUrls']['medium']}")
        else:
            print("[!] User has no registered labels !")
        dispach=str(input("[?] Do you want to display player's achievements ? [yes/no] "))
        while dispach not in ANS and dispach not in NANS:
            print("[!] Invalid input !")
            sleep(1)
            dispach=str(input("[?] Do you want to display player's achievements ? [yes/no] "))
        if dispach in ANS:
            def isCompleted(num):
                if num == 3:
                    return True
                return False
            for i in range(len(js['achievements'])):
                print(f"[+] Name: {js['achievements'][i]['name']}")
                print(f"[+] Achievement completed: {isCompleted(js['achievements'][i]['stars'])}")
                print(f"[+] Description: {js['achievements'][i]['info']}")
                print(f"[+] Highest value: {js['achievements'][i]['value']}")
                print(f"[+] Only need {js['achievements'][i]['target']} to receive the achievement")
                print(f"[+] Village: {js['achievements'][i]['village']}")
        distr=str(input("[?] Do you want to display player's troops ? [yes/no] "))
        while distr not in ANS and distr not in NANS:
            print("[!] Invalid input !")
            sleep(1)
            distr=str(input("[?] Do you want to display player's troops ? [yes/no] "))
        if distr in ANS:
            x = 0
            t = 0
            maxed = 0
            for i in range(len(js['troops'])):
                if js['troops'][i]['village'] == 'home' and 'Spell' not in js['troops'][i]['name']:
                    x += 1
                    print(f"[+] Name: {js['troops'][i]['name']}")
                    print(f"[+] Level: {js['troops'][i]['level']}")
                    print(f"[+] Max level: {js['troops'][i]['maxLevel']}")
                    if js['troops'][i]['maxLevel'] == js['troops'][i]['level']:
                        maxed += 1
                        print("[+] Maxed troop !")
                    else:
                        print(f"[+] {js['troops'][i]['maxLevel'] - js['troops'][i]['level'])} more levels to max the troop")
                    print(f"[+] Village: {js['troops'][i]['village']}")
                elif js['troops'][i]['village'] == 'builderBase' and 'Spell' not in js['troops'][i]['name']:
                    t += 1
                    print(f"[+] Name: {js['troops'][i]['name']}")
                    print(f"[+] Level: {js['troops'][i]['level']}")
                    print(f"[+] Max level: {js['troops'][i]['maxLevel']}")
                    if js['troops'][i]['maxLevel'] == js['troops'][i]['level']:
                        maxed += 1
                        print("[+] Maxed troop !")
                    else:
                        print(f"[+] {js['troops'][i]['maxLevel'] - js['troops'][i]['level']} more levels to max the troop")
                    print(f"[+] Village: {js['troops'][i]['village']}")
                elif 'Spell' in js['troops'][i]['name']:
                    pass
            perx = (x / 40.0)*100
            pert = (t / 11.0)*100
            permx = (maxed / len(js['troops']))*100
            print(f"[+] Percentage of troops (in the Home Village) owned by the player: {perx}%")
            print(f"[+] Percentage of troops (in the Builder Base) owned by the player: {pert}%")
            print(f"[+] Percentage of max troops owned by the player: {permx}%")
            print(f"[+] Number of maxed troops: {maxed}/{len(js['troops'])}")
        disph=str(input("[?] Do you want to display player's heroes ? [yes/no] "))
        while disph not in ANS and disph not in NANS:
            print("[!] Invalid input !")
            sleep(1)
            disph=str(input("[?] Do you want to display player's heroes ? [yes/no] "))
        if disph in ANS:
            maxedh = 0
            for i in range(len(js['heroes'])):
                print(f"[+] Name: {js['heroes'][i]['name']}")
                print(f"[+] Level: {js['heroes'][i]['level']}")
                print(f"[+] Max level: {js['heroes'][i]['maxLevel']}")
                if js['heroes'][i]['maxLevel'] == js['heroes'][i]['level']:
                    maxedh += 1
                    print("[+] Maxed hero !")
                else:
                    print(f"[+] {js['heroes'][i]['maxLevel'] - js['heroes'][i]['level']} more levels to max the hero")
            per = (len(js['heroes'] / 5.0))*100
            print(f"[+] Player own's {per}% of the heroes")
            print(f"[+] Percentage of maxed heroes: {(maxedh / len(js['heroes']))*100}")
            print("[+] Number of maxed heroes: "+str(maxedh)+"/"+str(len(js['heroes'])))
        disps=str(input("[?] Do you want to display player's spells ? [yes/no] "))
        while disph not in ANS and disph not in NANS:
            print("[!] Invalid input !")
            sleep(1)
            disph=str(input("[?] Do you want to display player's spells ? [yes/no] "))
        if disph in ANS:
            maxeds = 0
            pers = (len(js['spells']) / 13.0)*100
            for i in range(len(js['spells'])):
                print("[+] Name: "+str(js['spells'][i]['name']))
                print("[+] Level: "+str(js['spells'][i]['level']))
                print("[+] Max level: "+str(js['spells'][i]['maxLevel']))
                if js['spells'][i]['maxLevel'] == js['spells'][i]['level']:
                    maxeds += 1
                    print("[!] Maxed spell !")
                else:
                    print("[+] "+str(js['spells'][i]['maxLevel'] - js['spells'][i]['level'])+" more levels to max the spell")
            print("[+] Percentage of spells owned by the player: "+str(pers)+"%")
            print("[+] Percentage of maxed spells: "+str((maxeds / len(js['spells'])*100))+"%")
            print("[+] Number of maxed spells: "+str(maxeds)+"/"+str(len(js['spells'])))
        print("-" * 45)
    else:
        print(f"[!] Failed to retrieve data ! Error code: {page.status_code}")
        exit(0)
def Clan(tag: str):
    if platform.system() == 'Windows':
        system("cls")
    else:
        system("clear")
    print("\n")
    tag = tag.upper()
    print("[1] Display info for a clan")
    print("[2] Display info for the members of a clan")
    print("[3] Search clans")
    print("[4] Return to menu")
    option=int(input("[::] Please enter a number (from the above ones): "))
    while option < 1 or option > 4 or option == None:
        print("[!] Invalid number !")
        sleep(1)
        option=int(input("[::] Please enter again a number (from the above ones): "))
    if option == 1:
        tag = tag.upper()
        page = requests.get("https://api.clashofclans.com/v1/clans/%23"+str(tag), headers=headers)
        if page.status_code == 200:
            js = page.json()
            print("-" * 40)
            print("[+] Name: "+str(js['name']))
            print("[+] Type: "+str(js['type']))
            print("[+] Description: "+str(js['description']))
            print("[+] Chat language: "+str(js['chatLanguage']['name']))
            print("[+] Is family friendly: "+str(js['isFamilyFriendly']))
            print("[+] Number of members: "+str(js['members']))
            print("[+] Required VS trophies: "+str(js['requiredVersusTrophies']))
            print("[+] Required town hall level: "+str(js['requiredTownhallLevel']))
            print("[+] Location: "+str(js['location']['name']))
            print("[+] Is country: "+str(js['isCountry']))
            print("[+] Icon: "+str(js['badgeUrls']['medium']))
            print("[+] Level: "+str(js['clanLevel']))
            print("[+] Points: "+str(js['clanPoints']))
            print("[+] Required Trophies: "+str(js['requiredTrophies']))
            print("[+] War frequency: "+str(js['warFrequency']))
            print("[+] Current war win streak: "+str(js['warWinStreak']))
            print("[+] War wins: "+str(js['warWins']))
            print("[+] War ties: "+str(js['warTies']))
            print("[+] War losses: "+str(js['warLosses']))
            print("[+] Is war log public: "+str(js['isWarLogPublic']))
            print("[+] War league: "+str(js['warLeague']['name']))
            print("[+] Clan capital league: "+str(js['capitalLeague']['name']))
            print("[+] Clan capital hall level: "+str(js['clanCapital']['capitalHallLevel']))
            print("-"*10+"districts".upper()+"-"*10)
            for i in range(len(js['clanCapital']['districts'])):
                print("[+] Name: "+str(js['clanCapital']['districts'][i]['name']))
                print("[+] Level: "+str(js['clanCapital']['districts'][i]['districtHallLevel']))
            print("-"*10+"labels".upper()+"-"*10)
            for i in range(len(js['labels'])):
                print("[+] Name: "+str(js['labels'][i]['name']))
                print("[+] Icon: "+str(js['labels'][i]['iconUrls']['medium']))
            print("-" * 40)
        else:
            print("[!] Failed to retrieve data ! Error code: "+str(page.status_code))
            exit(0)
    elif option == 2:
        page = requests.get(f"https://api.clashofclans.com/v1/clans/%23{tag}/members", headers=headers)
        if page.status_code == 200:
            js = page.json()
            role = ''
            for i in range(len(js['items'])):
                print("[+] Name: "+str(js['items'][i]['name']))
                print("[+] Tag: "+str(js['items'][i]['tag']))
                if js['items'][i]['role'] == 'admin':
                    role = 'Elder'
                elif js['items'][i]['role'] == 'coLeader':
                    role = 'Co-Leader'
                else:
                    role = 'Leader'
                print("[+] Role: "+str(role))
                print("[+] Clan rank: "+str(js['items'][i]['clanRank']))
                print("[+] Previous clan rank: "+str(js['items'][i]['previousClanRank']))
                print("[+] Experience level: "+str(js['items'][i]['expLevel']))
                print("[+] League: "+str(js['items'][i]['league']['name']))
                print("[+] Trophies: "+str(js['items'][i]['trophies']))
                print("[+] Versus trophies: "+str(js['items'][i]['versusTrophies']))
                print("[+] Donations made: "+str(js['items'][i]['donations']))
                print("[+] Troops received: "+str(js['items'][i]['donationsReceived']))
            print("\n")
        else:
            print("[!] Failed to retrieve data ! Error code: "+str(page.status_code))
            exit(0)
    elif option == 3:
        print("\n")
        name=str(input("[::] Please enter the name of the clan: "))
        while name == None:
            print("[!] Invalid name !")
            sleep(1)
            name=str(input("[::] Please enter again the name of the clan: "))
        count=int(input("[?] How many results to display (enter an integer number) ? "))
        while count == None or count == 0:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[?] How many results to display (enter an integer number) ? "))
        page = requests.get(f"https://api.clashofclans.com/v1/clans?name={name}&limit={count}", headers=headers)
        if page.status_code == 200:
            js = page.json()
            wl_pub = "yes"
            for i in range(len(js['items'])):
                print("[+] Name: "+str(js['items'][i]['name']))
                print("[+] Type: "+str(js['items'][i]['type']))
                print("[+] Location: "+str(js['items'][i]['location']['name']))
                print("[+] Badge: "+str(js['items'][i]['badgeUrls']['medium']))
                print("[+] Level: "+str(js['items'][i]['clanLevel']))
                print("[+] Points: "+str(js['items'][i]['clanPoints']))
                print("[+] Versus points: "+str(js['items'][i]['clanVerusPoints']))
                print("[+] Required trophies: "+str(js['items'][i]['requiredTrophies']))
                print("[+] War frequency: "+str(js['items'][i]['warFrequency']))
                print("[+] War win streak: "+str(js['items'][i]['warWinStreak']))
                print("[+] War wins: "+str(js['items'][i]['warWins']))
                print("[+] War ties: "+str(js['items'][i]['warTies']))
                print("[+] War losses: "+str(js['items'][i]['warLosses']))
                if not js['items'][i]['isWarLogPublic']:
                    wl_pub = "No"
                print("[+] Is the war log public ? "+str(wl_pub))
                print("[+] War league: "+str(js['items'][i]['warLeague']['name']))
                print("[+] Required versus trophies: "+str(js['items'][i]['requiredVersusTrophies']))
                print("[+] Required TownHall level: "+str(js['items'][i]['requiredTownhallLevel']))
                print("[+] Chat language: "+str(js['items'][i]['chatLanguage']['name']))
                print("[+] Number of members: "+str(js['items'][i]['members']))
        else:
            print("[!] Failed to retrieve data ! Error code: "+str(page.status_code))
            exit(0)
    else:
        main()

def League():
    if platform.system() == 'Windows':
        system("cls")
    else:
        system("clear")
    print("\n")
    print("[1] Display the leagues")
    print("[2] Display the clan capital leagues")
    print("[3] Display the war leagues")
    print("[4] Display info about a league")
    print("[5] Display info about a clan capital league")
    print("[6] Display info about a war league")
    print("[7] Display season IDs")
    print("[8] Display season rankings")
    print("[9] Return to menu")
    print("\n")
    print("[+] ==> NOTE: If you want display info about a league you need to enter first one of the three number (1-3) to get the league ID (if you don't already have it):)")
    print("\n")
    option=int(input("[::] Please enter a number (from the above ones): "))
    while option < 1 or option > 9 or option == None:
        print("[!] Invalid number !")
        sleep(1)
        option=int(input("[::] Please enter again a number (from the above ones): "))
    if option == 1:
        page = requests.get("https://api.clashofclans.com/v1/leagues", headers=headers)
        if page.status_code == 200:
            js = page.json()
            print("-"*20+"leagues".upper()+"-"*20)
            for i in range(len(js['items'])):
                print("[+] ID: "+str(js['items'][i]['id']))
                print("[+] Name: "+str(js['items'][i]['name']))
                print("[+] Icon Url: "+str("js['items'][i]['iconUrls']['small']"))
        else:
            print("[!] Failed to retrieve data ! Error code: "+str(page.status_code))
            exit(0)
    elif option == 2:
        page = requests.get("https://api.clashofclans.com/v1/capitalleagues", headers=headers)
        if page.status_code == 200:
            js = page.json()
            print("-"*20+"clan capital leagues".upper()+"-"*20)
            for i in range(len(js['items'])):
                print("[+] ID: "+str(js['items'][i]['id']))
                print("[+] Name: "+str(js['items'][i]['name']))
        else:
            print("[!] Failed to retrieve data ! Error code: "+str(page.status_code))
            exit(0)
    elif option == 3:
        page = requests.get("https://api.clashofclans.com/v1/warleagues", headers=headers)
        if page.status_code == 200:
            js = page.json()
            print("-"*20+"war leagues".upper()+"-"*20)
            for i in range(len(js['items'])):
                print("[+] ID: "+str(js['items'][i]['id']))
                print("[+] Name: "+str(js['items'][i]['name']))
        else:
            print("[!] Failed to retrieve data ! Error code: "+str(page.status_code))
            exit(0)
    elif option == 4:
        id=int(input("[::] Please enter here the league ID: "))
        while id == None or len(id) < 8 or len(id) > 8:
            print("[!] Invalid league ID !")
            sleep(1)
            id=int(input("[::] Please enter again the league ID: "))
        page = requests.get("https://api.clashofclans.com/v1/leagues/"+str(id), headers=headers)
        if page.status_code == 200:
            js = page.json()
            print("[+] Name: "+str(js['name']))
            print("[+] Icon: "+str(js['iconUrls']['small']))
        else:
            print("[!] Failed to retrieve data ! Error code: "+str(page.status_code))
            exit(0)
    elif option == 5:
        id=int(input("[::] Please enter here the clan capital league ID: "))
        while id == None or len(id) < 8 or len(id) > 8:
            print("[!] Invalid league ID !")
            sleep(1)
            id=int(input("[::] Please enter again the clan capital league ID: "))
        page = requests.get("https://api.clashofclans.com/v1/capitalleagues/"+str(id), headers=headers)
        if page.status_code == 200:
            js = page.json()
            print("[+] Name: "+str(js['name']))
        else:
            print("[!] Failed to retrieve data ! Error code: "+str(page.status_code))
            exit(0)
    elif option == 6:
        id=int(input("[::] Please enter here the war league ID: "))
        while id == None or len(id) < 8 or len(id) > 8:
            print("[!] Invalid league ID !")
            sleep(1)
            id=int(input("[::] Please enter again the war league ID: "))
        page = requests.get("https://api.clashofclans.com/v1/warleagues/"+str(id), headers=headers)
        if page.status_code == 200:
            js = page.json()
            print("[+] Name: "+str(js['name']))
        else:
            print("[!] Failed to retrieve data ! Error code: "+str(page.status_code))
            exit(0)
    elif option == 7:
        page = requests.get("https://api.clashofclans.com/v1/leagues/29000022/seasons", headers=headers)
        if page.status_code == 200:
            js = page.json()
            print("-"*20+"season ids".upper()+"-"*20)
            for i in range(len(js['items'])):
                print(f"[+] ID No{i+1}: {js['items'][i]['id']}")
        else:
            print("[!] Failed to retrieve data ! Error code: "+str(page.status_code))
            exit(0)
    elif option == 8:
        id=input("[::] Please enter here the season ID: ")
        while id == None or '-' not in id:
            print("[!] Invalid league ID !")
            sleep(1)
            id=input("[::] Please enter again the season ID: ")
        page = requests.get("https://api.clashofclans.com/v1/leagues/29000022/seasons/"+str(id), headers=headers)
        if page.status_code == 200:
            js = page.json()
            print("-"*20+"rankings".upper()+"-"*20)
            for i in range(len(js['items'])):
                print("[+] Name: "+str(js['items'][i]['name']))
                print("[+] Tag: "+str(js['items'][i]['tag']))
                print("[+] Rank: "+str(js['items'][i]['rank']))
                print("[+] Experience level: "+str(js['items'][i]['expLevel']))
                print("[+] Trophies: "+str(js['items'][i]['trophies']))
                print("[+] Number of attack wins: "+str(js['items'][i]['attackWins']))
                print("[+] Number of defence wins: "+str(js['items'][i]['defenseWins']))
                print("[+] Clan: "+str(js['items'][i]['clan']['name']))
        else:
            print("[!] Failed to retrieve data ! Error code: "+str(page.status_code))
            exit(0)
    else:
        main()


def banner():
    return  """
░█████╗░██╗░░░░░░█████╗░░██████╗██╗░░██╗   ░█████╗░███████╗   ██╗███╗░░██╗███████╗░█████╗░
██╔══██╗██║░░░░░██╔══██╗██╔════╝██║░░██║   ██╔══██╗██╔════╝   ██║████╗░██║██╔════╝██╔══██╗
██║░░╚═╝██║░░░░░███████║╚█████╗░███████║   ██║░░██║█████╗░░   ██║██╔██╗██║█████╗░░██║░░██║
██║░░██╗██║░░░░░██╔══██║░╚═══██╗██╔══██║   ██║░░██║██╔══╝░░   ██║██║╚████║██╔══╝░░██║░░██║
╚█████╔╝███████╗██║░░██║██████╔╝██║░░██║   ╚█████╔╝██║░░░░░   ██║██║░╚███║██║░░░░░╚█████╔╝
░╚════╝░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝   ░╚════╝░╚═╝░░░░░   ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░
"""

def main():
    print(banner())
    print("\n")
    print("[+] Author: new92")
    print("[+] Github: @new92")
    print("\n")
    print("[+] Description: Script for getting information about clans, users, leagues and much more... in the famous game: Clash of Clans :)")
    print("\n")
    print("[1] Display info for a player")
    print("[2] Display info for a clan")
    print("[3] Display info for a league")
    print("[4] Display program's info and exit")
    print("[5] Exit")
    option=int(input("[::] Please enter a number (from the above ones): "))
    while option < 1 or option > 5 or option == None:
        print("[!] Sorry, invalid number !")
        sleep(1)
        option=int(input("[::] Please enter again a number (from the above ones): "))
    if option == 1:
        tag=str(input("[::] Please enter the tag of the player (please do not include the tag(#) symbol): "))
        while tag == None or tag[0] == "#":
            print("[!] Invalid tag !")
            sleep(1)
            if tag[0] == "#":
                print("[!] Please DO NOT include the tag (#) symbol in your next input !")
                sleep(2)
            tag=str(input("[::] Please enter again the tag of the player (please do not include the tag(#) symbol): "))
        Player(tag)
    elif option == 2:
        tag=str(input("[::] Please enter the tag of the clan (please do not include the tag(#) symbol): "))
        while tag == None or tag[0] == "#":
            print("[!] Invalid tag !")
            sleep(1)
            if tag[0] == "#":
                print("[!] Please DO NOT include the tag (#) symbol in your next input !")
                sleep(2)
            tag=str(input("[::] Please enter again the tag of the clan (please do not include the tag(#) symbol): "))
        Clan(tag)
    elif option == 3:
        League()
    elif option == 4:
        ProgInfo()
    else:
        print("[+] Thank you for using my script 😁")
        sleep(2)
        print("See you next time 👋")
        sleep(1)
        exit(0)
if __name__ == '__main__':
    main()
