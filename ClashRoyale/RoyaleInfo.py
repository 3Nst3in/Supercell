# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92

RoyaleInfo is a python script which helps the user retrieve info about players, clans, tournaments etc.
"""

try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[!] Error ! RoyaleInfo requires Python version 3.X ! ")
        sleep(2)
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python 3 and then use RoyaleInfo ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    from tqdm import tqdm
    total_mods = 7
    bar = tqdm(total=total_mods, desc='Loading modules', unit='module')
    for _ in range(total_mods):
        sleep(0.75)
        bar.update(1)
    bar.close()
    import platform
    from os import system
    import os
    import json
    import requests
except ImportError or ModuleNotFoundError:
    print("[!] WARNING: Not all packages used in RoyaleInfo have been installed !")
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
                print(f"[=] Error message ==> {ex}")
                sleep(2)
                print("[1] Uninstall script")
                print("[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 2:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers: [1/2]")
                    sleep(1)
                    print("[1] Uninstall script")
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

with open('apiKey.json') as api:
    key = json.load(api)

headers = {
    'Accept': 'application/json',
    'authorization': f'Bearer {key["key"]}'
}

def clear():
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')

print("[✓] Successfully loaded modules !")
sleep(1)

ANS = ['yes','no']
CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))
    return None

def ProgInfo():
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

def banner() -> str:
    return """
    ██████╗░░█████╗░██╗░░░██╗░█████╗░██╗░░░░░███████╗    ██╗███╗░░██╗███████╗░█████╗░
    ██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗██║░░░░░██╔════╝    ██║████╗░██║██╔════╝██╔══██╗
    ██████╔╝██║░░██║░╚████╔╝░███████║██║░░░░░█████╗░░    ██║██╔██╗██║█████╗░░██║░░██║
    ██╔══██╗██║░░██║░░╚██╔╝░░██╔══██║██║░░░░░██╔══╝░░    ██║██║╚████║██╔══╝░░██║░░██║
    ██║░░██║╚█████╔╝░░░██║░░░██║░░██║███████╗███████╗    ██║██║░╚███║██║░░░░░╚█████╔╝
    ╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝    ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░
    """

def checkTag(tag: str) -> bool:
    return tag == '' or tag == ' ' or tag == None

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

def Player():
    print("\n")
    print("[1] Display info for a player")
    print("[2] Display info about the upcoming chests of a player")
    print("[3] Display the battlelog of a player")
    print("[4] Return to menu")
    option=int(input("[::] Number >>> "))
    while option < 1 or option > 4:
        print("[!] Invalid number !")
        sleep(1)
        print("[+] Acceptable numbers: [1/2/3/4]")
        sleep(1)
        option=int(input("[::] Number >>> "))
    tag=str(input("[::] Player tag >>> "))
    while checkTag(tag):
        print("[!] This field can't be blank !")
        sleep(1)
        tag=str(input("[::] Player tag >>> "))
    tag = tag.upper().strip()
    if tag[0] == '#':
        tag = tag[1:]
    if option == 1:
        page = requests.get(f"https://api.clashroyale.com/v1/players/%23{tag}", headers=headers)
        js = page.json()
        name = js['name']
        print(f"[+] Name: {name}")
        print(f"[+] Experience level: {js['expLevel']}")
        print(f"[+] Trophies: {js['trophies']}")
        print(f"[+] Highest trophies: {js['bestTrophies']}")
        print(f"[+] Number of wins: {js['wins']}")
        print(f"[+] Number of losses: {js['losses']}")
        print(f"[+] Number of battles: {js['battleCount']}")
        print(f"[+] Number of three crown wins: {js['threeCrownWins']}")
        print(f"[+] Challenge cards won: {js['challengeCardsWon']}")
        print(f"[+] Challenge max wins: {js['challengeMaxWins']}")
        print(f"[+] Tournament cards won: {js['tournamentCardsWon']}")
        print(f"[+] Tournament battles: {js['tournamentBattleCount']}")
        print(f"[+] Number of donations: {js['donations']}")
        print(f"[+] Donations received: {js['donationsReceived']}")
        print(f"[+] Total donations: {js['totalDonations']}")
        print(f"[+] Number of War-Day wins: {js['warDayWins']}")
        print(f"[+] Clan cards collected: {js['clanCardsCollected']}")
        print(f"[+] Arena: {js['arena']['name']}")
        print(f"[+] Trophies current season: {js['leagueStatistics']['currentSeason']['trophies']}")
        print(f"[+] Highest trophies current season: {js['leagueStatistics']['currentSeason']['bestTrophies']}")
        print(f"[+] Trophies previous season: {js['leagueStatistics']['previousSeason']['trophies']}")
        print(f"[+] Trophies best season: {js['leagueStatistics']['bestSeason']['trophies']}")
        print("\n")
        sleep(2)
        print("[+] Acceptable answers: [yes/no]")
        sleep(1.5)
        dispBd = str(input("[?] Display player's badges ? "))
        while dispBd == None or dispBd.lower() not in ANS or dispBd == '' or dispBd == ' ':
            if dispBd == None or dispBd == '' or dispBd == ' ':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid answer !")
                sleep(1)
                print("[+] Acceptable answers: [yes/no]")
            sleep(1)
            dispBd = str(input(f"[?] Display {name}'s badges ? "))
        if dispBd.lower() == ANS[0]:
            for i in range(len(js['badges'])):
                print(f"[+] Number of badges: {len(js['badges'])}")
                print(f"[+] Badge name: {js['badges'][i]['name']}")
                print(f"[+] Level: {js['badges'][i]['level']}")
                print(f"[+] Max level: {js['badges'][i]['maxLevel']}")
                print(f"[+] Player's progress: {js['badges'][i]['progress']}")
                print(f"[+] URL: {js['badges'][i]['iconUrls']['large']}")
                print(f"[+] Player's star points: {js['starPoints'][i]}")
                print(f"[+] Player's experience points: {js['expPoints'][i]}")
                print("-" * 25)
        sleep(1)
        print("[+] Acceptable answers: [yes/no]")
        sleep(1.5)
        dispAch = str(input("[?] Display player's achievements ? "))
        while dispAch == None or dispAch.lower() not in ANS or dispAch == '' or dispAch == ' ':
            if dispAch == None or dispAch == '' or dispAch == ' ':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid answer !")
                sleep(1)
                print("[+] Acceptable answers: [yes/no]")
            sleep(1)
            dispAch = str(input(f"[?] Display {name}'s achievements ? "))
        if dispAch.lower() == ANS[0]:
            for i in range(len(js['achievements'])):
                print(f"[+] Number of player's achievemenents: {len(js['achievements'])}")
                print(f"[+] Name: {js['achievements'][i]['name']}")
                if js['achievements'][i]['name'] == "Team Player":
                    print(f"[+] Player has joined: {js['achievements'][0]['value']} clans so far...")
                print(f"[+] How many times does a player has to make the action in order to receive the achievement ? {js['achievements'][i]['target']}")
                print(f"[+] Achievement description: {js['achievements'][i]['info']}")
                print("-" * 25)
        sleep(1)
        print("[+] Acceptable answers: [yes/no]")
        sleep(1.5)
        dispCards = str(input(f"[?] Display cards owned by {name} ? "))
        while dispCards == None or dispCards.lower() not in ANS and dispCards == '' or dispCards == ' ':
            if dispCards == None or dispCards == '' or dispCards == ' ':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid answer !")
                sleep(1)
                print("[+] Acceptable answers: [yes/no]")
            sleep(1)
            dispCards = str(input("[?] Do you want to display the cards the player owns ? [yes/no] "))
        if dispCards.lower() == ANS[0]:
            for i in range(len(js['cards'])):
                print(f"[+] Total cards player owns: {len(js['cards'])}")
                print(f"[+] Card name: {js['cards'][i]['name']}")
                print(f"[+] Card level: {js['cards'][i]['level']}")
                print(f"[+] Card's max level: {js['cards'][i]['maxLevel']}")
                print(f"[+] Current number of points for upgrade: {js['cards'][i]['count']}")
                print(f"[+] Icon URL: {js['cards'][i]['iconUrls']['medium']}")
                print("-" * 25)

    elif option == 2:
        page = requests.get(f"https://api.clashroyale.com/v1/players/%23{tag}/upcomingchests", headers=headers)
        js = page.json()
        for item in range(len(js['items'])):
            print(f"[+] Number of wins: {js['items'][item]['index']}")
            print(f"[+] Chest: {js['items'][item]['name']}")
            print("-" * 15)

    elif option == 3:
        page = requests.get(f"https://api.clashroyale.com/v1/players/%23{tag}/battlelog", headers=headers)
        js = page.json()
        for i in range(len(js[:])):
            print(f"[+] Type of battle: {js['type'][i]}")
            if js['type'][i] == "challenge":
                if js['isLadderTournament'][i]:
                    isLadT = "yes"
                else:
                    isLadT = "no"
                print(f"[+] Is the challenge ladder tournament ? [{isLadT}]")
            print(f"[+] Arena: {js[i]['arena']['name']}")
            print(f"[+] Gamemode: {js[i]['gameMode']['name']}")
            if js[i]['deckSelection'] == "eventDeck":
                dkSel = "via event"
            else:
                dkSel = "other"
            print(f"[+] How is the deck being selected ? {dkSel}")
            print(f"[+] Player's name: {js[i]['team']['name']}")
            print(f"[+] Crown's won: {js[i]['team']['crowns']}")
            print(f"[+] Player's clan name: {js[i]['team']['clan']['name']}")
            print("-"*15)
            print("[+] Player's deck: ")
            print("-"*15)
            for card in range(len(js[i]['team']['cards'])):
                print(f"[+] Card's name: {js[i]['team']['cards'][card]['name']}")
                print(f"[+] Card's level: {js[i]['teams']['cards'][card]['level']}")
            print("-"*15)
            print(f"[+] Opponent's name: {js[i]['opponent']['name']}")
            print(f"[+] Opponent's tag: {js[i]['opponent']['tag']}")
            print(f"[+] Crown's won: {js[i]['opponent']['crowns']}")
            print(f"[+] Opponent's clan name: {js[i]['opponent']['clan']['name']}")
            print("-"*15)
            print("[+] Opponent's deck: ")
            print("-"*15)
            for card in range(len(js[i]['opponent']['cards'])):
                print(f"[+] Card's name: {js[i]['opponent']['cards'][card]['name']}")
                print(f"[+] Card's level: {js[i]['opponent']['cards'][card]['level']}")
            print("-"*15)
    else:
        clear()
        main()

def Clan():
    print("[1] Display info for a clan")
    print("[2] Display clan members and info for each member")
    print("[3] Display info about clan's current river race")
    print("[4] Search a clan")
    print("[5] Return to menu")
    num=int(input("[::] Number >>> "))
    while num < 1 or num > 5 or num == None:
        print("[!] Invalid number !")
        sleep(1)
        num=int(input("[::] Number >>> "))
    sleep(1)
    tag=str(input("[::] Player tag >>> "))
    while checkTag(tag):
        print("[!] This field can't be blank !")
        sleep(1)
        tag=str(input("[::] Player tag >>> "))
    tag = tag.upper().strip()
    if tag[0] == "#":
        tag = tag[1:]
    if num == 1:
        page = requests.get(f"https://api.clashroyale.com/v1/clans/%23{tag}", headers=headers)
        js = page.json()
        print(f"[+] Clan name: {js['name']}")
        print(f"[+] Type: {js['type']}")
        print(f"[+] Description: {js['description']}")
        print(f"[+] War score: {js['clanScore']}")
        print(f"[+] War trophies: {js['clanWarTrophies']}")
        print(f"[+] Location: {js['location']['name']}")
        print(f"[+] Required trophies: {js['requiredTrophies']}")
        print(f"[+] Donations per week: {js['donationsPerWeek']}")
        print(f"[+] Number of members: {js['members']}")
    elif num == 2:
        page = requests.get(f"https://api.clashroyale.com/v1/clans/%23{tag}/members", headers=headers)
        js = page.json()
        for item in range(len(js['items'])):
            print(f"[+] Name: {js['items'][item]['name']}")
            print(f"[+] Role: {js['items'][item]['role']}")
            print(f"[+] Experience level: {js['items'][item]['expLevel']}")
            print(f"[+] Trophies: {js['items'][item]['trophies']}")
            print(f"[+] Arena: {js['items'][item]['arena']['name']}")
            print(f"[+] Clan rank: {js['items'][item]['clanRank']}")
            print(f"[+] Donations: {js['items'][item]['donations']}")
            print(f"[+] Donations received: {js['items'][item]['donationsReceived']}")
    elif num == 3:
        page = requests.get(f"https://api.clashroyale.com/v1/clans/%23{tag}/currentriverrace", headers=headers)
        js = page.json()
        print(f"[+] State: {js['state']}")
        print(f"[+] Clan score: {js['clanScore']}")
        print(f"[+] Period points: {js['periodPoints']}")
        print(f"[+] Period type: {js['periodType']}")
        print("-"*30)
        print(">>>participants  info<<<".upper())
        for i in range(len(js['participants'])):
            print(f"[+] Name: {js['participants'][i]['name']}")
            print(f"[+] Tag: {js['participants'][i]['tag']}")
            print(f"[+] Fame points: {js['participants'][i]['fame']}")
            print(f"[+] Repair points: {js['participants'][i]['repairPoints']}")
            print(f"[+] Boat attacks: {js['participants'][i]['boatAttacks']}")
            print(f"[+] Decks used: {js['participants'][i]['decksUsed']}")
            print(f"[+] Decks used today: {js['participants'][i]['decksUsedToday']}")
        for i in range(len(js['clans'])):
            print(f"[+] Clan name: {js['clans'][i]['name']}")
            print(f"[+] Clan's fame points: {js['clans'][i]['fame']}")
            print(f"[+] Clan's repair points: {js['clans'][i]['repairPoints']}")
            print(f"[+] Clan's score: {js['clans'][i]['clanScore']}")
            print(f"[-] Participants names for {js['clans'][i]['name']}")
            for j in range(len(js['clans'][i]['participants'])):
                print(f"[+] Name No{j+1}: {js['clans'][i]['participants'][j]['name']}")
    elif num == 4:
        name=str(input("[::] Clan name >>> "))
        while name == None or name == '' or name == ' ':
            print("[!] This field can't be blank !")
            sleep(1)
            name=str(input("[::] Please enter again the name of the clan: "))
        sleep(1)
        print("[+] Acceptable answers: [yes/no]")
        sleep(1.5)
        incMinMem=str(input("[?] Add a minimum value of players ? "))
        while incMinMem == None or incMinMem.lower() not in ANS or incMinMem == '' or incMinMem == ' ':
            if incMinMem == None or incMinMem == '' or incMinMem == ' ':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid answer !")
                sleep(1)
                print("[+] Acceptable answers: [yes/no]")
            sleep(1)
            incMinMem=str(input("[?] Add a minimum number of players ? "))
        if incMinMem.lower() == ANS[0]:
            countMin=int(input("[::] Number >>> "))
            while countMin < 1 or countMin == None:
                print("[!] Invalid number !")
                sleep(1)
                countMin=int(input("[::] Number >>> "))
            incMin = True
        else:
            incMin = False
        sleep(1)
        print("[+] Acceptable answers: [yes/no]")
        sleep(1.5)
        incMaxMem=str(input("[?] Add a maximum number of members ? "))
        while incMaxMem == None or incMaxMem not in ANS or incMaxMem == '' or incMaxMem == ' ':
            if incMaxMem == None or incMaxMem == '' or incMaxMem == ' ':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid answer !")
                sleep(1)
                print("[+] Acceptable answers: [yes/no]")
            sleep(1)
            incMaxMem=str(input("[?] Add a maximum number of members ? "))
        if incMaxMem.lower() == ANS[0]:
            count=int(input("[::] Number >>> "))
            while count == None or count <= 0:
                print("[!] Invalid number !")
                sleep(1)
                count=int(input("[::] Number >>> "))
            incMax = True
        else:
            incMax = False
        sleep(1)
        print("[+] Acceptable answers: [yes/no]")
        sleep(1.5)
        incMinScore=str(input("[?] Do you want to include a minimum score (of the team) ? [yes/no] "))
        while incMinScore == None or incMinScore not in ANS and incMinScore == '' or incMinScore == ' ':
            if incMinScore == None or incMinScore == '' or incMinScore == ' ':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid answer !")
                sleep(1)
                print("[+] Acceptable answers: [yes/no]")
            incMinScore=str(input("[?] Do you want to include a minimum score (of the team) ? [yes/no] "))
        if incMinScore.lower() == ANS[0]:
            incMscore = True
            score=int(input("[::] Enter score >>> "))
            while score == None or score <= 0:
                print("[!] Invalid score !")
                sleep(1)
                score=int(input("[::] Please enter again the score: "))
        else:
            incMscore = False
        sleep(1)
        print("[+] Acceptable answers: [yes/no]")
        sleep(1.5)
        incLim=str(input("[::] Include a limit to the results ? "))
        while incLim == None or incLim.lower() not in ANS or incLim == '' or incLim == ' ':
            if incLim == None or incLim == '' or incLim == ' ':
                print("[!] This field can't be blank !")
            else:
                print("[!] Invalid answer !")
                sleep(1)
                print("[+] Acceptable answers: [yes/no]")
            sleep(1)
            incLim=str(input("[::] Include a limit to the results ? "))
        if incLim.lower() in ANS:
            incl = True
            lim=int(input("[::] Limit (integer) >>> "))
            while lim == None or lim <= 0:
                print("[!] Invalid number !")
                sleep(1)
                lim=int(input("[::] Limit (integer) >>> "))
        else:
            incl = False
        if incMin and incMax and incMscore and incl:
            page = requests.get(f"https://api.clashroyale.com/v1/clans?name={name}&minMembers={countMin}&maxMembers={count}&minScore={score}&limit={lim}", headers=headers)
            js = page.json()
            for i in range(len(js['items'])):
                print(f"[+] Clan's tag: {js['items'][i]['tag']}")
                print(f"[+] Name: {js['items'][i]['name']}")
                print(f"[+] Type: {js['items'][i]['type']}")
                print(f"[+] Clan score: {js['items'][i]['clanScore']}")
                print(f"[+] Location: {js['items'][i]['location']['name']}")
                print(f"[+] Required trophies: {js['items'][i]['requiredTrophies']}")
                print(f"[+] Donations per week: {js['items'][i]['donationsPerWeek']}")
                print(f"[+] Clan chest level: {js['items'][i]['clanChestLevel']}")
                print(f"[+] Number of members: {js['items'][i]['members']}")
    else:
        clear()
        main()

def Cards():
    page = requests.get("https://api.clashroyale.com/v1/cards", headers=headers)
    js = page.json()
    print("-"*10+"cards".upper()+"-"*10)
    for i in range(len(js['items'])):
        print(f"[+] Name: {js['items'][i]['name']}")
        print(f"[+] Max level: {js['items'][i]['maxLevel']}")
        print(f"[+] Icon URL: {js['items'][i]['iconUrls']['medium']}")
        sleep(1)

def Search(name):
    def convert(x: int, num: int) -> int:
        if x == 1: 
            return num // 60
        else: 
            return num // 24
    page = requests.get(f'https://api.clashroyale.com/v1/tournaments?name={name}', headers=headers)
    js = page.json()
    for i in range(len(js['items'])):
        print(f"[+] Name: {js['items'][i]['name']}")
        print(f"[+] Description: {js['items'][i]['description']}")
        print(f"[+] Number of participants: {js['items'][i]['capacity']}")
        print(f"[+] Max capacity: {js['items'][i]['maxCapacity']} players")
        av = js['items'][i]['maxCapacity'] - js['items'][i]['capacity']
        if av == 0:
            print("[+] No available participations !")
        else:
            print(f"[+] Available participations: {av}")
        print(f"[+] Preparation duration: {convert(1,convert(1,js['items'][i]['preparationDuration']))} hour(s)")
        print(f"[+] Tournament duration: {convert(2,convert(1,convert(1,js['items'][i]['duration'])))} day(s)")
        print(f"[+] Tag: {js['items'][i]['tag']}")
        print(f"[+] Type: {js['items'][i]['type']}")
        print(f"[+] Status: {js['items'][i]['status']}")
        print(f"[+] Creator's tag: {js['items'][i]['creatorTag']}")
        pg = requests.get(f"https://api.clashroyale.com/v1/players/%23{js['items'][i]['creatorTag']}", headers=headers)
        jsn = pg.json()
        print(f"[+] Creator's name: {jsn['name']}")
        print(f"[+] Creator's clan: {jsn['clan']['name']}")
    
def Tour(tag):
    def convert(x: int, num: int) -> int:
        if x == 1: 
            return num // 60
        else: 
            return num // 24
    page = requests.get(f"https://api.clashroyale.com/v1/tournaments/%23{tag}", headers=headers)
    js = page.json()
    print(f"[+] Name: {js['name']}")
    print(f"[+] Description: {js['description']}")
    print(f"[+] Type: {js['type']}")
    print(f"[+] Status: {js['status']}")
    print(f"[+] Number of participants: {js['capacity']}")
    print(f"[+] Max capacity: {js['maxCapacity']} players")
    av = js['maxCapacity'] - js['capacity']
    if av == 0:
        print("[+] No available participations !")
    else:
        print(f"[+] Available participations: {av}")
    print(f"[+] Preparation duration: {convert(1,convert(1,js['preparationDuration']))} hour(s)")
    print(f"[+] Tournament duration: {convert(2,convert(1,convert(1,js['duration'])))} day(s)")
    print(f"[+] Creator's tag: {js['creatorTag']}")
    pg = requests.get(f"https://api.clashroyale.com/v1/players/%23{js['creatorTag']}", headers=headers)
    jsn = pg.json()
    print(f"[+] Creator's name: {jsn['name']}")
    print(f"[+] Creator's clan: {jsn['clan']['name']}")
    print("-"*20+"participants".upper()+"-"*20)
    for i in range(len(js['membersList'])):
        print(f"[+] Name: {js['membersList'][i]['name']}")
        print(f"[+] Tag: {js['membersList'][i]['tag']}")
        print(f"[+] Score: {js['membersList'][i]['score']}")
        print(f"[+] Rank: {js['membersList'][i]['rank']}")
        print(f"[+] Participant's clan: {js['membersList'][i]['clan']['name']}")

def UpcEvents():
    page = requests.get("https://api.clashroyale.com/v1/challenges", headers=headers)
    js = page.json()
    retypes = ['resource','consumable','tradeToken','chest']
    for i in range(len(js[:])):
        print(f"[+] Name: {js[i]['challenges']['name']}")
        print(f"[+] Description: {js[i]['challenges']['description']}")
        print(f"[+] Type: {js[i]['type']}")
        print(f"[+] Max losses: {js[i]['challenges']['maxLosses']}")
        print(f"[+] Gamemode: {js[i]['challenges']['gameMode']['name']}")
        print(f"[+] Icon URL: {js[i]['challenges']['iconUrl']}")
        print("-"*20+"prizes".upper()+"-"*20)
        for j in range(len(js[i]['challenges']['prizes'])):
            if js[i]['challenges']['prizes'][j]['type'] == retypes[0]:
                print(f"[+] Prize No{j+1}: {retypes[0]}")
                print(f"[+] Amount: {js[i]['challenges']['prizes'][j]['amount']}")
            elif js[i]['challenges']['prizes'][j]['type'] == retypes[1]:
                print(f"[+] Prize No{j+1}: {js[i]['challenges']['prizes'][j]['consumableName']}")
                print(f"[+] Amount: {js[i]['challenges']['prizes'][j]['amount']}")
            elif js[i]['challenges']['prizes'][j]['type'] == retypes[2]:
                print(f"[+] Prize No{j+1}: {retypes[2]}")
                print(f"[+] Amount: {js[i]['challenges']['prizes'][j]['amount']}")
                print(f"[+] Rarity: {js[i]['challenges']['prizes'][j]['rarity']}")
            elif js[i]['challenges']['prizes'][j]['type'] == retypes[3]:
                print(f"[+] Prize No{j+1}: {retypes[3]}")
                print(f"[+] Chest type: {js[i]['challenges']['prizes'][j]['chest']}")
def main():
    print(banner())
    print("\n")
    print("[+] Author: new92")
    print("[+] Github: @new92")
    print("\n")
    print("[+] RoyaleInfo: Script which provides info for players, clans, tournaments, cards etc. for the famous video game Clash Royale")
    print("\n")
    print("[1] Display info for a player")
    print("[2] Display info for a clan")
    print("[3] Display a list of all available cards (Updated)")
    print("[4] Search tournaments")
    print("[5] Display info about a tournament")
    print("[6] Display info about upcoming challenges")
    print("[7] Show RoyaleInfo's info and exit")
    print("[8] Uninstall RoyaleInfo")
    print("[9] Exit")
    num=int(input("[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 9 or num == None:
        print("[!] Invalid number !")
        sleep(1)
        print("[+] Acceptable numbers: [1-9]")
        sleep(1.3)
        num=int(input("[::] Please enter again a number (from the above ones): "))
    if num == 1:
        clear()
        Player()
    elif num == 2:
        clear()
        Clan()
    elif num == 3:
        clear()
        Cards()
    elif num == 4:
        clear()
        tour=str(input("[::] Tournament name >>> "))
        while tour == None or tour == '' or tour == ' ':
            print("[!] This field can't be blank !")
            sleep(1)
            tour=str(input("[::] Tournament name >>> "))
        Search(name=tour)
    elif num == 5:
        clear()
        tag=str(input("[::] Tournament tag >>> "))
        while checkTag(tag):
            print("[!] This field can't be blank !")
            sleep(1)
            tag=str(input("[::] Tournament tag >>> "))
        tag = tag.upper().strip()
        if tag[0] == '#':
            tag = tag[1:]
        Tour(tag)
    elif num == 6:
        clear()
        UpcEvents()
    elif num == 7:
        clear()
        ProgInfo()
    elif num == 8:
        clear()
        print(Uninstall())
        sleep(2)
        print("[+] Thank you for using RoyaleInfo 😁")
        sleep(2)
        print("[+] Until we meet again 🫡")
        sleep(1)
        quit(0)
    else:
        clear()
        print("[+] Thank you for using RoyaleInfo 😁")
        sleep(2)
        print("[+] See you next time 👋")
        sleep(1)
        quit(0)

if __name__ == '__main__':
    main()
