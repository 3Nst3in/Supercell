# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92

ClashofInfo: Script for displaying info about players, clans, leagues etc. in the famous game: Clash of Clans.
"""

try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[!] Error ! ClashofInfo requires Python version 3.X ! ")
        sleep(2)
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python 3 and then use ClashofInfo ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    import platform
    from tqdm import tqdm
    total_mods = 7
    bar = tqdm(total=total_mods, desc='Loading modules', unit='module')
    for _ in range(total_mods):
        sleep(0.75)
        bar.update(1)
    bar.close()
    from os import system
    import requests
    import os
    import json
except ImportError or ModuleNotFoundError:
    print("[!] WARNING: Not all packages used in ClashofInfo have been installed !")
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
                print("[!] Error ! Cannot install the required modules !")
                sleep(1)
                print(f"[*] Error message ==> {ex}")
                sleep(2)
                print("[1] Uninstall ClashofInfo")
                print("[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 2 or opt == None:
                    if opt == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers: [1,2]")
                    sleep(1)
                    print("[1] Uninstall ClashofInfo")
                    print("[2] Exit")
                    opt=int(input("[>] Please enter again a number (from the above ones): "))
                if opt == 1:
                    def fpath(fname: str):
                        for root, dirs, files in os.walk('/'):
                            if fname in files:
                                return os.path.abspath(os.path.join(root, fname))
                        return None
                    def rmdir(dire):
                        DIRS = []
                        for root, dirs, files in os.walk(dire):
                            for file in files:
                                os.remove(os.path.join(root,file))
                            for dir in dirs:
                                DIRS.append(os.path.join(root,dir))
                        for i in range(len(DIRS)):
                            os.rmdir(DIRS[i])
                        os.rmdir(dire)
                    rmdir(fpath('Supercell'))
                    print("[✓] Files and dependencies uninstalled successfully !")
                else:
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] See you next time 👋")
                    quit(0)
        else:
            system("sudo pip install -r requirements.txt")
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")

with open('apiKey.json') as keyFile:
    data = json.load(keyFile)

headers = {
    'Accept': 'application/json',
    'authorization': f'Bearer {data["key"]}'
}

print("[✓] Successfully loaded modules !")
sleep(1)

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

def clear():
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')

def ScriptInfo():
    clear()
    with open('config.json') as config:
        conf = json.load(config)
    f = conf['name'] + '.py'
    if os.path.exists(fpath(f)):
        fsize = os.stat(fpath(f)).st_size
    else:
        fsize = 0
    print(f"[+] Author: {conf['author']}")
    print(f"[+] Github: @{conf['author']}")
    print(f"[+] License: {conf['lice']}")
    print(f"[+] Programming language(s) used: {conf['lang']}")
    print(f"[+] Language(s): {conf['language']}")
    print(f"[+] Script's name: {conf['name']}")
    print(f"[+] Lines of code: {conf['lines']}")
    print(f"[+] API(s) used: {conf['api']}")
    print(f"[+] URL: {conf['api_url']}")
    print(f"[+] File size: {fsize} bytes")
    print(f"[+] File path: {fpath(f)}")
    print("|======|GITHUB REPO INFO|======|")
    print(f"[+] Stars: {conf['stars']}")
    print(f"[+] Forks: {conf['forks']}")
    print(f"[+] Open issues: {conf['issues']}")
    print(f"[+] Closed issues: {conf['clissues']}")
    print(f"[+] Open pull requests: {conf['prs']}")
    print(f"[+] Closed pull requests: {conf['clprs']}")
    print(f"[+] Discussions: {conf['discs']}")

def clear():
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')

ANS = ['yes','no']

def Player(tag: str):
    tag = tag.upper()
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
        print('|'+"-"*10+"labels".upper()+"-"*10+'|')
        if len(js['labels']) != 0:
            for i in range(len(js['labels'])):
                print(f"[+] Name: {js['labels'][i]['name']}")
                print(f"[+] Icon: {js['labels'][i]['iconUrls']['medium']}")
        else:
            print("[!] User has no registered labels !")
        sleep(1)
        print("\n")
        print("[+] Acceptable answers: [yes/no]")
        sleep(1.5)
        dispach=str(input("[?] Display player's achievements ?? "))
        while dispach.lower() not in ANS or dispach == '' or dispach == None or dispach == ' ':
            if dispach == '' or dispach == None or dispach == ' ':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid answer !")
                sleep(1)
                print("[+] Acceptable answers: [yes/no]")
            sleep(1)
            dispach=str(input("[?] Display player's achievements ? "))
        if dispach.lower() == ANS[0]:
            def isCompleted(num: int) -> bool:
                return True if num == 3 else False
            for i in range(len(js['achievements'])):
                print(f"[+] Name: {js['achievements'][i]['name']}")
                print(f"[+] Achievement completed: {isCompleted(js['achievements'][i]['stars'])}")
                print(f"[+] Description: {js['achievements'][i]['info']}")
                print(f"[+] Highest value: {js['achievements'][i]['value']}")
                print(f"[+] Only need {js['achievements'][i]['target']} to receive the achievement")
                print(f"[+] Village: {js['achievements'][i]['village']}")
        sleep(1)
        print("\n")
        print("[+] Acceptable answers: [yes/no]")
        sleep(1.5)
        distr=str(input("[?] Display player's troops ? "))
        while distr.lower() not in ANS or distr == None or distr == '' or distr == ' ':
            if distr == None or distr == '' or distr == ' ':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid answer !")
                sleep(1)
                print("[+] Acceptable answers: [yes/no]")
            sleep(1)
            distr=str(input("[?] Display player's troops ? "))
        if distr.lower() == ANS[0]:
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
                        print(f"[+] {js['troops'][i]['maxLevel'] - js['troops'][i]['level']} more levels to max the troop")
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
        sleep(1)
        print("\n")
        print("[+] Acceptable answers: [yes/no]")
        sleep(1.5)
        disph=str(input("[?] Display player's heroes ? "))
        while disph.lower() not in ANS or disph == None or disph == '' or disph == ' ':
            if disph == None or disph == '' or disph == ' ':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid answer !")
                sleep(1)
                print("[+] Acceptable answers: [yes/no]")
            sleep(1)
            disph=str(input("[?] Display player's heroes ? "))
        if disph.lower() == ANS[0]:
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
            print(f"[+] Player owns {per}% of the heroes")
            print(f"[+] Percentage of maxed heroes: {(maxedh / len(js['heroes']))*100}")
            print(f"[+] Number of maxed heroes: {maxedh}/{len(js['heroes'])}")
        sleep(1)
        print("[+] Acceptable answers: [yes/no]")
        sleep(1.5)
        disps=str(input("[?] Display player's spells ? "))
        while disps.lower() not in ANS or disps == None or disps == '' or disps == ' ':
            if disps == None or disps == '' or disps == ' ':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid input !")
                sleep(1)
                print("[+] Acceptable answers: [yes/no]")
            sleep(1)
            disps=str(input("[?] Display player's spells ? "))
        if disps.lower() == ANS[0]:
            maxeds = 0
            pers = (len(js['spells']) / 13.0)*100
            for i in range(len(js['spells'])):
                print(f"[+] Name: {js['spells'][i]['name']}")
                print(f"[+] Level: {js['spells'][i]['level']}")
                print(f"[+] Max level: {js['spells'][i]['maxLevel']}")
                if js['spells'][i]['maxLevel'] == js['spells'][i]['level']:
                    maxeds += 1
                    print("[!] Maxed spell !")
                else:
                    print(f"[+] {js['spells'][i]['maxLevel'] - js['spells'][i]['level']} more levels to max the spell")
            print(f"[+] Percentage of spells owned by the player: {pers}%")
            print(f"[+] Percentage of maxed spells: {(maxeds / len(js['spells']))*100}%")
            print(f"[+] Number of maxed spells: {maxeds}/{len(js['spells'])}")
        print("-" * 45)
    else:
        print(f"[!] Failed to retrieve data ! Error code: {page.status_code}")
        sleep(2)
        print("[+] Exiting...")
        sleep(0.5)
        exit(0)

def Clan(tag: str):
    tag = tag.upper().strip()
    print("[1] Display info for a clan")
    print("[2] Display info for the members of a clan")
    print("[3] Search clans")
    print("[4] Return to menu")
    option=int(input("[::] Please enter a number (from the above ones): "))
    while option < 1 or option > 4 or option == None:
        print("[!] Invalid number !")
        sleep(1)
        print("[+] Acceptable numbers: [1-4]")
        sleep(1)
        option=int(input("[::] Please enter again a number (from the above ones): "))
    if option == 1:
        page = requests.get(f"https://api.clashofclans.com/v1/clans/%23{tag}", headers=headers)
        if page.status_code == 200:
            js = page.json()
            print("-" * 40)
            print(f"[+] Name: {js['name']}")
            print(f"[+] Type: {js['type']}")
            print(f"[+] Description: {js['description']}")
            print(f"[+] Chat language: {js['chatLanguage']['name']}")
            print(f"[+] Is family friendly: {js['isFamilyFriendly']}")
            print(f"[+] Number of members: {js['members']}")
            print(f"[+] Required VS trophies: {js['requiredVersusTrophies']}")
            print(f"[+] Required town hall level: {js['requiredTownhallLevel']}")
            print(f"[+] Location: {js['location']['name']}")
            print(f"[+] Is country: {js['isCountry']}")
            print(f"[+] Icon: {js['badgeUrls']['medium']}")
            print(f"[+] Level: {js['clanLevel']}")
            print(f"[+] Points: {js['clanPoints']}")
            print(f"[+] Required Trophies: {js['requiredTrophies']}")
            print(f"[+] War frequency: {js['warFrequency']}")
            print(f"[+] Current war win streak: {js['warWinStreak']}")
            print(f"[+] War wins: {js['warWins']}")
            print(f"[+] War ties: {js['warTies']}")
            print(f"[+] War losses: {js['warLosses']}")
            print(f"[+] Is war log public: {js['isWarLogPublic']}")
            print(f"[+] War league: {js['warLeague']['name']}")
            print(f"[+] Clan capital league: {js['capitalLeague']['name']}")
            print(f"[+] Clan capital hall level: {js['clanCapital']['capitalHallLevel']}")
            print("-"*10+"districts".upper()+"-"*10)
            for i in range(len(js['clanCapital']['districts'])):
                print(f"[+] Name: {js['clanCapital']['districts'][i]['name']}")
                print(f"[+] Level: {js['clanCapital']['districts'][i]['districtHallLevel']}")
            print("-"*10+"labels".upper()+"-"*10)
            for i in range(len(js['labels'])):
                print(f"[+] Name: {js['labels'][i]['name']}")
                print(f"[+] Icon: {js['labels'][i]['iconUrls']['medium']}")
            print("-" * 40)
        else:
            print(f"[!] Failed to retrieve data ! Error code: {page.status_code}")
            sleep(2)
            print("[+] Exiting...")
            sleep(0.5)
            exit(0)
    elif option == 2:
        page = requests.get(f"https://api.clashofclans.com/v1/clans/%23{tag}/members", headers=headers)
        if page.status_code == 200:
            js = page.json()
            role = ''
            for i in range(len(js['items'])):
                print(f"[+] Name: {js['items'][i]['name']}")
                print(f"[+] Tag: {js['items'][i]['tag']}")
                if js['items'][i]['role'] == 'admin':
                    role = 'Elder'
                elif js['items'][i]['role'] == 'coLeader':
                    role = 'Co-Leader'
                else:
                    role = 'Leader'
                print(f"[+] Role: {role}")
                print(f"[+] Clan rank: {js['items'][i]['clanRank']}")
                print(f"[+] Previous clan rank: {js['items'][i]['previousClanRank']}")
                print(f"[+] Experience level: {js['items'][i]['expLevel']}")
                print(f"[+] League: {js['items'][i]['league']['name']}")
                print(f"[+] Trophies: {js['items'][i]['trophies']}")
                print(f"[+] Versus trophies: {js['items'][i]['versusTrophies']}")
                print(f"[+] Donations made: {js['items'][i]['donations']}")
                print(f"[+] Troops received: {js['items'][i]['donationsReceived']}")
            print("\n")
        else:
            print(f"[!] Failed to retrieve data ! Error code: {page.status_code}")
            sleep(2)
            print("[+] Exiting...")
            sleep(0.5)
            exit(0)
    elif option == 3:
        print("\n")
        name=str(input("[::] Clan name >>> "))
        while name == None or name == '' or name == ' ':
            print("[!] This field can't be blank !")
            sleep(1)
            name=str(input("[::] Clan name >>> "))
        sleep(1)
        count=int(input("[::] Results to display (integer) >>> "))
        while count <= 0 or count == None:
            print("[!] Invalid number !")
            sleep(1)
            count=int(input("[::] Results to display (integer) >>> "))
        page = requests.get(f"https://api.clashofclans.com/v1/clans?name={name}&limit={count}", headers=headers)
        if page.status_code == 200:
            js = page.json()
            wl_pub = "yes"
            for i in range(len(js['items'])):
                print(f"[+] Name: {js['items'][i]['name']}")
                print(f"[+] Type: {js['items'][i]['type']}")
                print(f"[+] Location: {js['items'][i]['location']['name']}")
                print(f"[+] Badge: {js['items'][i]['badgeUrls']['medium']}")
                print(f"[+] Level: {js['items'][i]['clanLevel']}")
                print(f"[+] Points: {js['items'][i]['clanPoints']}")
                print(f"[+] Versus points: {js['items'][i]['clanVerusPoints']}")
                print(f"[+] Required trophies: {js['items'][i]['requiredTrophies']}")
                print(f"[+] War frequency: {js['items'][i]['warFrequency']}")
                print(f"[+] War win streak: {js['items'][i]['warWinStreak']}")
                print(f"[+] War wins: {js['items'][i]['warWins']}")
                print(f"[+] War ties: {js['items'][i]['warTies']}")
                print(f"[+] War losses: {js['items'][i]['warLosses']}")
                if not js['items'][i]['isWarLogPublic']:
                    wl_pub = "No"
                print(f"[+] Is the war log public ? {wl_pub}")
                print(f"[+] War league: {js['items'][i]['warLeague']['name']}")
                print(f"[+] Required versus trophies: {js['items'][i]['requiredVersusTrophies']}")
                print(f"[+] Required TownHall level: {js['items'][i]['requiredTownhallLevel']}")
                print(f"[+] Chat language: {js['items'][i]['chatLanguage']['name']}")
                print(f"[+] Number of members: {js['items'][i]['members']}")
        else:
            print(f"[!] Failed to retrieve data ! Error code: {page.status_code}")
            sleep(2)
            print("[+] Exiting...")
            sleep(0.5)
            exit(0)
    else:
        clear()
        main()

def League():
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
    print("[*] ==> NOTE: If you want display info about a league you need to enter first one of the three number (1-3) to get the league ID (if you don't already have it):)")
    print("\n")
    option=int(input("[::] Please enter a number (from the above ones): "))
    while option < 1 or option > 9 or option == None:
        print("[!] Invalid number !")
        sleep(1)
        print("[+] Acceptable numbers: [1-9]")
        sleep(1)
        option=int(input("[::] Please enter again a number (from the above ones): "))
    if option == 1:
        clear()
        page = requests.get("https://api.clashofclans.com/v1/leagues", headers=headers)
        if page.status_code == 200:
            js = page.json()
            print("-"*20+"leagues".upper()+"-"*20)
            for i in range(len(js['items'])):
                print(f"[+] ID: {js['items'][i]['id']}")
                print(f"[+] Name: {js['items'][i]['name']}")
                print(f"[+] Icon Url: {js['items'][i]['iconUrls']['small']}")
        else:
            print(f"[!] Failed to retrieve data ! Error code: {page.status_code}")
            sleep(2)
            print("[+] Exiting...")
            sleep(0.5)
            exit(0)
    elif option == 2:
        clear()
        page = requests.get("https://api.clashofclans.com/v1/capitalleagues", headers=headers)
        if page.status_code == 200:
            js = page.json()
            print("-"*20+"clan capital leagues".upper()+"-"*20)
            for i in range(len(js['items'])):
                print(f"[+] ID: {js['items'][i]['id']}")
                print(f"[+] Name: {js['items'][i]['name']}")
        else:
            print(f"[!] Failed to retrieve data ! Error code: {page.status_code}")
            sleep(2)
            print("[+] Exiting...")
            sleep(0.5)
            exit(0)
    elif option == 3:
        clear()
        page = requests.get("https://api.clashofclans.com/v1/warleagues", headers=headers)
        if page.status_code == 200:
            js = page.json()
            print("-"*20+"war leagues".upper()+"-"*20)
            for i in range(len(js['items'])):
                print(f"[+] ID: {js['items'][i]['id']}")
                print(f"[+] Name: {js['items'][i]['name']}")
        else:
            print(f"[!] Failed to retrieve data ! Error code: {page.status_code}")
            sleep(2)
            print("[+] Exiting...")
            sleep(0.5)
            exit(0)
    elif option == 4:
        clear()
        id=int(input("[::] League ID >>> "))
        while len(id) != 8 or id == None:
            print("[!] Invalid league ID !")
            sleep(1)
            print("[+] Acceptable length of league ID >> 8 characters")
            sleep(1)
            id=int(input("[::] League ID >>> "))
        sleep(1)
        page = requests.get(f"https://api.clashofclans.com/v1/leagues/{id}", headers=headers)
        if page.status_code == 200:
            js = page.json()
            print(f"[+] Name: {js['name']}")
            print(f"[+] Icon: {js['iconUrls']['small']}")
        else:
            print(f"[!] Failed to retrieve data ! Error code: {page.status_code}")
            sleep(2)
            print("[+] Exiting...")
            sleep(0.5)
            exit(0)
    elif option == 5:
        clear()
        id=int(input("[::] Clan capital league ID >>> "))
        while len(id) != 8 or id == None:
            print("[!] Invalid league ID !")
            sleep(1)
            print("[+] Acceptable length of league ID >> 8 characters")
            sleep(1)
            id=int(input("[::] Clan capital league ID >>> "))
        page = requests.get(f"https://api.clashofclans.com/v1/capitalleagues/{id}", headers=headers)
        if page.status_code == 200:
            js = page.json()
            print(f"[+] Name: {js['name']}")
        else:
            print(f"[!] Failed to retrieve data ! Error code: {page.status_code}")
            sleep(2)
            print("[+] Exiting...")
            sleep(0.5)
            exit(0)
    elif option == 6:
        clear()
        id=int(input("[::] War league ID >>> "))
        while len(id) != 8 or id == None:
            print("[!] Invalid league ID !")
            sleep(1)
            print("[+] Acceptable length of league ID >> 8 characters")
            sleep(1)
            id=int(input("[::] War league ID >>> "))
        page = requests.get(f"https://api.clashofclans.com/v1/warleagues/{id}", headers=headers)
        if page.status_code == 200:
            js = page.json()
            print(f"[+] Name: {js['name']}")
        else:
            print(f"[!] Failed to retrieve data ! Error code: {page.status_code}")
            sleep(2)
            print("[+] Exiting...")
            sleep(0.5)
            exit(0)
    elif option == 7:
        clear()
        page = requests.get("https://api.clashofclans.com/v1/leagues/29000022/seasons", headers=headers)
        if page.status_code == 200:
            js = page.json()
            print("-"*20+"season ids".upper()+"-"*20)
            for i in range(len(js['items'])):
                print(f"[+] ID No{i+1}: {js['items'][i]['id']}")
        else:
            print(f"[!] Failed to retrieve data ! Error code: {page.status_code}")
            sleep(2)
            print("[+] Exiting...")
            sleep(0.5)
            exit(0)
    elif option == 8:
        clear()
        id=str(input("[::] Season ID >>> "))
        while id == None or '-' not in id or id == '' or id == ' ':
            if id == None or id == '' or id == ' ':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid league ID !")
                sleep(1)
                print("[+] Acceptable league ID format >>> xxxx-xx")
            sleep(1)
            id=str(input("[::] Season ID >>> "))
        id = id.strip()
        page = requests.get(f"https://api.clashofclans.com/v1/leagues/29000022/seasons/{id}", headers=headers)
        if page.status_code == 200:
            js = page.json()
            print("-"*20+"rankings".upper()+"-"*20)
            for i in range(len(js['items'])):
                print(f"[+] Name: {js['items'][i]['name']}")
                print(f"[+] Tag: {js['items'][i]['tag']}")
                print(f"[+] Rank: {js['items'][i]['rank']}")
                print(f"[+] Experience level: {js['items'][i]['expLevel']}")
                print(f"[+] Trophies: {js['items'][i]['trophies']}")
                print(f"[+] Number of attack wins: {js['items'][i]['attackWins']}")
                print(f"[+] Number of defence wins: {js['items'][i]['defenseWins']}")
                print(f"[+] Clan: {js['items'][i]['clan']['name']}")
        else:
            print(f"[!] Failed to retrieve data ! Error code: {page.status_code}")
            sleep(2)
            print("[+] Exiting...")
            sleep(0.5)
            exit(0)
    else:
        clear()
        main()

def Uninstall() -> str:
    def rmdir(dire):
        DIRS = []
        for root, dirs, files in os.walk(dire):
            for file in files:
                os.remove(os.path.join(root,file))
            for dir in dirs:
                DIRS.append(os.path.join(root,dir))
        for i in range(len(DIRS)):
            os.rmdir(DIRS[i])
        os.rmdir(dire)
    rmdir(fpath('Supercell'))
    return "[✓] Files and dependencies uninstalled successfully !"

def banner() -> str:
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
    print("[+] ClashofInfo: Script which provides info about clans, users, leagues and much more... in the famous game: Clash of Clans :)")
    print("\n")
    print("[1] Display info for a player")
    print("[2] Display info for a clan")
    print("[3] Display info for a league")
    print("[4] Display ClashofInfo's info and exit")
    print("[5] Uninstall ClashofInfo")
    print("[6] Exit")
    option=int(input("[::] Number >>> "))
    while option < 1 or option > 6 or option == None:
        print("[!] Invalid number !")
        sleep(1)
        print("[+] Acceptable numbers: [1-6]")
        sleep(1)
        option=int(input("[::] Number >>> "))
    if option == 1:
        clear()
        tag=str(input("[::] Player tag >>> "))
        while tag == None or tag == '' or tag == ' ':
            print("[!] This field can't be blank !")
            sleep(1)
            tag=str(input("[::] Player tag >>> "))
        if '#' == tag[0]:
            tag = tag[1:]
        tag = tag.upper().strip()
        Player(tag)

    elif option == 2:
        clear()
        tag=str(input("[::] Clan tag >>> "))
        while tag == None or tag == ' ' or tag == '':
            print("[!] This field can't be blank !")
            sleep(1)
            tag=str(input("[::] Clan tag >>> "))
        tag = tag.upper().strip()
        Clan(tag)

    elif option == 3:
        clear()
        League()

    elif option == 4:
        clear()
        ScriptInfo()

    elif option == 5:
        clear()
        print(Uninstall())
        sleep(2)
        print("[+] Thank you for using ClashofInfo 😁")
        sleep(2)
        print("[+] Until we meet again 🫡")
        sleep(1)
        quit(0)

    else:
        clear()
        print("[+] Thank you for using ClashofInfo 😁")
        sleep(2)
        print("See you next time 👋")
        sleep(1)
        exit(0)

    print("[1] Return to menu")
    print("[2] Exit")
    n=int(input("[::] Please enter a number (from the above ones): "))
    while n < 1 or n > 2:
        if type(n) == int:
            print("[!] Invalid number !")
        else:
            print("[!] This input can't be blank")
            sleep(1)
            print("[1] Return to menu")
            print("[2] Exit")
            n=int(input("[::] Please enter again a number (from the above ones): "))
    if n == 1:
        clear()
        main()
    else:
        clear()
        print("[+] Exiting...")
        sleep(1)
        print("[+] Thank you for using Mutuals 😁")
        sleep(2)
        print("[+] Until next time 👋")
        sleep(1)
        quit(0)

if __name__ == '__main__':
    main()
