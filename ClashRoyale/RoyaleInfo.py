"""
Author: new92
Github: @new92
Script for displaying info for players, clans, tournaments, cards etc. in Clash Royale.
Hope you like it :)
"""

try:
    import sys
    import platform
    from os import system
    from time import sleep
    import json
    import os
    import requests
except ImportError as imp:
    print("[!] WARNING: Not all packages used in this program have been installed !")
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
        pass
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")
        pass

headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer <ENTER YOUR API TOKEN HERE>'
}

ANS = ['yes','YES','Yes','y','Y','YeS','yEs','yES','YEs','yeS']
NANS = ['no','NO','n','N','No','nO']

def ProgInfo():
    author = 'new92'
    lang = 'en-US'
    name = 'RoyaleInfo'
    language = 'Python'
    license = 'MIT'
    lines = 531
    api = 'Clash Royale API'
    size = 27.4
    stars = 6
    forks = 4
    print("[+] Author: "+str(author))
    print("[+] Github: @"+str(author))
    print("[+] Natural Language: "+str(lang))
    print("[+] Program's name: "+str(name))
    print("[+] Programming language(s) used: "+str(language))
    print("[+] License: "+str(license))
    print("[+] API used: "+str(api))
    print("[+] File size: "+str(size)+"kb")
    print("[+] Number of lines: "+str(lines))
    print("[+] Github repository stars: "+str(stars))
    print("[+] Github repository forks: "+str(forks))

def Logo():
    print("""
    ██████╗░░█████╗░██╗░░░██╗░█████╗░██╗░░░░░███████╗    ██╗███╗░░██╗███████╗░█████╗░
    ██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗██║░░░░░██╔════╝    ██║████╗░██║██╔════╝██╔══██╗
    ██████╔╝██║░░██║░╚████╔╝░███████║██║░░░░░█████╗░░    ██║██╔██╗██║█████╗░░██║░░██║
    ██╔══██╗██║░░██║░░╚██╔╝░░██╔══██║██║░░░░░██╔══╝░░    ██║██║╚████║██╔══╝░░██║░░██║
    ██║░░██║╚█████╔╝░░░██║░░░██║░░██║███████╗███████╗    ██║██║░╚███║██║░░░░░╚█████╔╝
    ╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝    ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░
    """)

def GetPlayerInfo() -> str:
    print("\n")
    print("[1] Display info for a player")
    print("[2] Display info about the upcoming chests of a player")
    print("[3] Display the battlelog of a player")
    option=int(input("[::] Please enter a number (from the above ones): "))
    while option < 1 or option > 3 or option == None:
        print("[!] Invalid number !")
        sleep(1)
        option=int(input("[::] Please enter again a number (from the above ones): "))
    tag=str(input("[::] Please enter the tag of the player (please do not include the tag symbol(#)): "))
    while tag == None:
        print("[!] Invalid tag !")
        sleep(1)
        tag=str(input("[::] Please enter again the tag of the player (without the tag symbol(#)): "))
    if option == 1:
        page = requests.get("https://api.clashroyale.com/v1/players/%23"+str(tag), headers=headers)
        js = page.json()
        print("[+] Name: "+str(js['name']))
        print("[+] Experience level: "+str(js['expLevel']))
        print("[+] Trophies: "+str(js['trophies']))
        print("[+] Highest trophies: "+str(js['bestTrophies']))
        print("[+] Number of wins: "+str(js['wins']))
        print("[+] Number of losses: "+str(js['losses']))
        print("[+] Number of battles: "+str(js['battleCount']))
        print("[+] Number of three crown wins: "+str(js['threeCrownWins']))
        print("[+] Challenge cards won: "+str(js['challengeCardsWon']))
        print("[+] Challenge max wins: "+str(js['challengeMaxWins']))
        print("[+] Tournament cards won: "+str(js['tournamentCardsWon']))
        print("[+] Tournament battles: "+str(js['tournamentBattleCount']))
        print("[+] Number of donations: "+str(js['donations']))
        print("[+] Donations received: "+str(js['donationsReceived']))
        print("[+] Total donations: "+str(js['totalDonations']))
        print("[+] Number of War-Day wins: "+str(js['warDayWins']))
        print("[+] Clan cards collected: "+str(js['clanCardsCollected']))
        print("[+] Arena: "+str(js['arena']['name']))
        print("[+] Trophies current season: "+str(js['leagueStatistics']['currentSeason']['trophies']))
        print("[+] Highest trophies current season: "+str(js['leagueStatistics']['currentSeason']['bestTrophies']))
        print("[+] Trophies previous season: "+str(js['leagueStatistics']['previousSeason']['trophies']))
        print("[+] Trophies best season: "+str(js['leagueStatistics']['bestSeason']['trophies']))
        disp_bd = str(input("[?] Do you want to display player's badges ? [yes/no] "))
        while disp_bd == None or disp_bd not in ANS and disp_bd not in NANS:
            print("[!] Invalid input !")
            sleep(1)
            disp_bd = str(input("[?] Do you want to display player's badges ? [yes/no] "))
        if disp_bd in ANS:
            for i in range(len(js['badges'])):
                print("[+] Number of badges: "+str(len(js['badges'])))
                print("[+] Badge name: "+str(js['badges'][i]['name']))
                print("[+] Level: "+str(js['badges'][i]['level']))
                print("[+] Max level: "+str(js['badges'][i]['maxLevel']))
                print("[+] Player's progress: "+str(js['badges'][i]['progress']))
                print("[+] Url: "+str(js['badges'][i]['iconUrls']['large']))
                print("[+] Player's star points: "+str(js['starPoints'][i]))
                print("[+] Player's experience points: "+str(js['expPoints'][i]))
                print("-" * 25)
        else:
            print("[OK]")
            pass
        disp_ach = str(input("[?] Do you want to display player's achievements ? [yes/no] "))
        while disp_ach == None or disp_ach not in ANS and disp_ach not in NANS:
            print("[!] Invalid input !")
            sleep(1)
            disp_ach = str(input("[?] Do you want to display player's achievements ? [yes/no] "))
        if disp_ach in ANS:
            for i in range(len(js['achievements'])):
                print("[+] Number of player's achievemenents: "+str(len(js['achievements'])))
                print("[+] Name: "+str(js['achievements'][i]['name']))
                if js['achievements'][i]['name'] == "Team Player":
                    print("[+] Player has joined: "+str(js['achievements'][0]['value']+" clans so far..."))
                else:
                    continue
                print("[+] How many times does a player has to make the action in order to receive the achievement ? "+str(js['achievements'][i]['target']))
                print("[+] Achievement description: "+str(js['achievements'][i]['info']))
                print("-" * 25)
        else:
            print("[OK]")
            pass
        disp_cards = str(input("[?] Do you want to display the cards the player owns ? [yes/no] "))
        while disp_cards == None or disp_cards not in ANS and disp_cards not in NANS:
            print("[!] Invalid input !")
            sleep(1)
            disp_cards = str(input("[?] Do you want to display the cards the player owns ? [yes/no] "))
        if disp_cards in ANS:
            for i in range(len(js['cards'])):
                print("[+] Total cards player owns: "+str(len(js['cards'])))
                print("[+] Card name: "+str(js['cards'][i]['name']))
                print("[+] Card level: "+str(js['cards'][i]['level']))
                print("[+] Card's max level: "+str(js['cards'][i]['maxLevel']))
                print("[+] Current number of points for upgrade: "+str(js['cards'][i]['count']))
                print("[+] Icon url: "+str(js['cards'][i]['iconUrls']['medium']))
                print("-" * 25)

    elif option == 2:
        page = requests.get("https://api.clashroyale.com/v1/players/%23"+str(tag)+"/upcomingchests", headers=headers)
        js = page.json()
        for item in range(len(js['items'])):
            print("[+] Number of wins: "+str(js['items'][item]['index']))
            print("[+] Chest: "+str(js['items'][item]['name']))
            print("-" * 15)

    else:
        page = requests.get("https://api.clashroyale.com/v1/players/%23"+str(tag)+"/battlelog", headers=headers)
        js = page.json()
        for i in range(len(js[:])):
            print("[+] Type of battle: "+str(js['type'][i]))
            if js['type'][i] == "challenge":
                if js['isLadderTournament'][i] == True:
                    is_lad_t = "yes"
                else:
                    is_lad_t = "no"
                print("[+] Is the challenge ladder tournament ? ["+str(is_lad_t)+"]")
            print("[+] Arena: "+str(js[i]['arena']['name']))
            print("[+] Gamemode: "+str(js[i]['gameMode']['name']))
            if js[i]['deckSelection'] == "eventDeck":
                dk_sel = "via event"
            else:
                dk_sel = "other"
            print("[+] How is the deck being selected ? "+str(dk_sel))
            print("[+] Player's name: "+str(js[i]['team']['name']))
            print("[+] Crown's won: "+str(js[i]['team']['crowns']))
            print("[+] Player's clan name: "+str(js[i]['team']['clan']['name']))
            print("-"*15)
            print("[+] Player's deck: ")
            print("-"*15)
            for card in range(len(js[i]['team']['cards'])):
                print("[+] Card's name: "+str(js[i]['team']['cards'][card]['name']))
                print("[+] Card's level: "+str(js[i]['teams']['cards'][card]['level']))
            print("-"*15)
            print("[+] Opponent's name: "+str(js[i]['opponent']['name']))
            print("[+] Opponent's tag: "+str(js[i]['opponent']['tag']))
            print("[+] Crown's won: "+str(js[i]['opponent']['crowns']))
            print("[+] Opponent's clan name: "+str(js[i]['opponent']['clan']['name']))
            print("-"*15)
            print("[+] Opponent's deck: ")
            print("-"*15)
            for card in range(len(js[i]['opponent']['cards'])):
                print("[+] Card's name: "+str(js[i]['opponent']['cards'][card]['name']))
                print("[+] Card's level: "+str(js[i]['opponent']['cards'][card]['level']))
            print("-"*15)
        quit(0)

def GetClanInfo() -> str:
    print("[1] Display info for a clan")
    print("[2] Display clan members and info for each member")
    print("[3] Display info about clan's current river race")
    print("[4] Search a clan")
    num=int(input("[::] Please enter a number (from the above ones): "))
    while num < 1 or num > 4 or num == None:
        print("[!] Invalid number !")
        sleep(1)
        num=int(input("[::] Please enter again a number (from the above ones): "))
    tag=str(input("[::] Please enter the tag of the player (please do not include the tag symbol(#)): "))
    while tag == None or tag[0] == "#":
        print("[!] Invalid tag !")
        sleep(1)
        if tag[0] == '#':
            print("[!] Please DO NOT include the tag (#) symbol in your next input !")
            sleep(1)
        tag=str(input("[::] Please enter again the tag of the player (please do not include the tag symbol (#)): "))
    if num == 1:
        page = requests.get("https://api.clashroyale.com/v1/clans/%23"+str(tag), headers=headers)
        js = page.json()
        descr = js['description']
        score = js['clanScore']
        war_trophies = js['clanWarTrophies']
        loc = js['location']['name']
        req_trophies = js['requiredTrophies']
        don_per_week = js['donationsPerWeek']
        num_mem = js['members']
        print("[+] Clan name: "+str(js['name']))
        print("[+] Type: "+str(js['type']))
        print("[+] Description: "+str(descr))
        print("[+] War score: "+str(score))
        print("[+] Location: "+str(loc))
        print("[+] Required trophies: "+str(req_trophies))
        print("[+] Donations per week: "+str(don_per_week))
        print("[+] Number of members: "+str(num_mem))
    elif num == 2:
        page = requests.get(f"https://api.clashroyale.com/v1/clans/%23{tag}/members", headers=headers)
        js = page.json()
        for item in range(len(js['items'])):
            print("[+] Name: "+str(js['items'][item]['name']))
            print("[+] Role: "+str(js['items'][item]['role']))
            print("[+] Experience level: "+str(js['items'][item]['expLevel']))
            print("[+] Trophies: "+str(js['items'][item]['trophies']))
            print("[+] Arena: "+str(js['items'][item]['arena']['name']))
            print("[+] Clan rank: "+str(js['items'][item]['clanRank']))
            print("[+] Donations: "+str(js['items'][item]['donations']))
            print("[+] Donations received: "+str(js['items'][item]['donationsReceived']))
    elif num == 3:
        page = requests.get(f"https://api.clashroyale.com/v1/clans/%23{tag}/currentriverrace", headers=headers)
        js = page.json()
        print("[+] State: "+str(js['state']))
        print("[+] Clan score: "+str(js['clanScore']))
        print("[+] Period points: "+str(js['periodPoints']))
        print("[+] Period type: "+str(js['periodType']))
        print("-"*30)
        print(">>>participants  info<<<".upper())
        for i in range(len(js['participants'])):
            print("[+] Name: "+str(js['participants'][i]['name']))
            print("[+] Tag: "+str(js['participants'][i]['tag']))
            print("[+] Fame points: "+str(js['participants'][i]['fame']))
            print("[+] Repair points: "+str(js['participants'][i]['repairPoints']))
            print("[+] Boat attacks: "+str(js['participants'][i]['boatAttacks']))
            print("[+] Decks used: "+str(js['participants'][i]['decksUsed']))
            print("[+] Decks used today: "+str(js['participants'][i]['decksUsedToday']))
        for i in range(len(js['clans'])):
            print("[+] Clan name: "+str(js['clans'][i]['name']))
            print("[+] Clan's fame points: "+str(js['clans'][i]['fame']))
            print("[+] Clan's repair points: "+str(js['clans'][i]['repairPoints']))
            print("[+] Clan's score: "+str(js['clans'][i]['clanScore']))
            print("[-] Participants names for "+str(js['clans'][i]['name']))
            for j in range(len(js['clans'][i]['participants'])):
                print(f"[+] Name No{j+1}: {js['clans'][i]['participants'][j]['name']}")
    else:
        name=str(input("[::] Please enter the name of the clan: "))
        while name == None:
            print("[!] Invalid name !")
            sleep(1)
            name=str(input("[::] Please enter again the name of the clan: "))
        inc_min_mem=str(input("[?] Do you want to add a minimum value of members [yes/no] ? "))
        while inc_min_mem == None or inc_min_mem not in ANS and inc_min_mem not in NANS:
            print("[!] Invalid input !")
            sleep(1)
            inc_min_mem=str(input("[?] Do you want to add a minimum value of members [yes/no] ? "))
        if inc_min_mem in ANS:
            full = False
            count_min=int(input("[::] Please enter the value: "))
            while count_min < 1 or count_min == None:
                print("[!] Invalid value !")
                sleep(1)
                count_min=int(input("[::] Please enter again the value: "))
            inc_min = True
        else:
            inc_min = False
            print("[OK]")
        inc_max_mem=str(input("[?] Do you want to add a maximum value of members [yes/no] ? "))
        while inc_max_mem == None or inc_max_mem not in ANS and inc_max_mem not in NANS:
            print("[!] Invalid input !")
            sleep(1)
            inc_max_mem=str(input("[?] Do you want to add a maximum value of members [yes/no] ? "))
        if inc_max_mem in ANS:
            count=int(input("[::] Please enter the number: "))
            while count == None or count <= 0:
                print("[!] Invalid number !")
                sleep(1)
                count=int(input("[::] Please enter the number: "))
            inc_max = True
        else:
            inc_max = False
            print("[OK]")
        inc_min_score=str(input("[?] Do you want to include a minimum score (of the team) ? [yes/no] "))
        while inc_min_score == None or inc_min_score not in ANS and inc_min_score not in NANS:
            print("[!] Invalid input !")
            sleep(1)
            inc_min_score=str(input("[?] Do you want to include a minimum score (of the team) ? [yes/no] "))
        if inc_min_score in ANS:
            inc_mscore = True
            score=input("[::] Please enter the score: ")
            while score == None or score <= 0:
                print("[!] Invalid score !")
                sleep(1)
                score=input("[::] Please enter again the score: ")
        else:
            inc_mscore = False
            print("[OK]")
        inc_lim=str(input("[::] Do you want to include a limit to the results ? [yes/no] "))
        while inc_lim == None or inc_lim not in ANS and inc_lim not in NANS:
            print("[!] Invalid input !")
            sleep(1)
            inc_lim=str(input("[::] Do you want to include a limit to the results ? [yes/no] "))
        if inc_lim in ANS:
            incl = True
            lim=int(input("[::] Please enter the limit: "))
            while lim == None or lim <= 0:
                print("[!] Invalid limit !")
                sleep(1)
                lim=int(input("[::] Please enter again the limit: "))
        else:
            incl = False
            print("[OK]")
        if inc_min == True and inc_max == True and inc_mscore == True and incl == True:
            page = requests.get("https://api.clashroyale.com/v1/clans?name={name}&minMembers={count_min}&maxMembers={count}&minScore={score}&limit={lim}", headers=headers)
            js = page.json()
            for i in range(len(js['items'])):
                print("[+] Clan's tag: "+str(js['items'][i]['tag']))
                print("[+] Name: "+str(js['items'][i]['name']))
                print("[+] Type: "+str(js['items'][i]['type']))
                print("[+] Clan score: "+str(js['items'][i]['clanScore']))
                print("[+] Location: "+str(js['items'][i]['location']['name']))
                print("[+] Required trophies: "+str(js['items'][i]['requiredTrophies']))
                print("[+] Donations per week: "+str(js['items'][i]['donationsPerWeek']))
                print("[+] Clan chest level: "+str(js['items'][i]['clanChestLevel']))
                print("[+] Number of members: "+str(js['items'][i]['members']))
def Cards() -> str:
    page = requests.get("https://api.clashroyale.com/v1/cards", headers=headers)
    js = page.json()
    for i in range(len(js['items'])):
        print("[+] Name: "+str(js['items'][i]['name']))
        print("[+] Max level: "+str(js['items'][i]['maxLevel']))
        print("[+] Icon url: "+str(js['items'][i]['iconUrls']['medium']))
        sleep(1)
def SearchT(name):
    def convert(x: int, num: int) -> int:
        if x == 1: #1 to convert seconds to minutes and minutes to hours
            return num // 60
        else: #2 to convert hours to days
            return num // 24
    page = requests.get('https://api.clashroyale.com/v1/tournaments?name='+str(name), headers=headers)
    js = page.json()
    for i in range(len(js['items'])):
        print("[+] Name: "+str(js['items'][i]['name']))
        print("[+] Description: "+str(js['items'][i]['description']))
        print("[+] Number of participants: "+str(js['items'][i]['capacity']))
        print("[+] Max capacity: "+str(js['items'][i]['maxCapacity'])+" players")
        av = js['items'][i]['maxCapacity'] - js['items'][i]['capacity']
        if av == 0:
            print("[+] No available participations !")
        else:
            print("[+] Available participations: "+str(av))
        print("[+] Preparation duration: "+str(convert(1,convert(1,js['items'][i]['preparationDuration'])))+" hour(s)")
        print("[+] Tournament duration: "+str(convert(2,convert(1,convert(1,js['items'][i]['duration']))))+" day(s)")
        print("[+] Tag: "+str(js['items'][i]['tag']))
        print("[+] Type: "+str(js['items'][i]['type']))
        print("[+] Status: "+str(js['items'][i]['status']))
        print("[+] Creator's tag: "+str(js['items'][i]['creatorTag']))
        pg = requests.get("https://api.clashroyale.com/v1/players/%23"+str(js['items'][i]['creatorTag']), headers=headers)
        jsn = pg.json()
        print("[+] Creator's name: "+str(jsn['name']))
        print("[+] Creator's clan: "+str(jsn['clan']['name']))
    
def getTourInfo(tag):
    def convert(x: int, num: int) -> int:
        if x == 1: #1 to convert seconds to minutes and minutes to hours
            return num // 60
        else: #2 to convert hours to days
            return num // 24
    page = requests.get("https://api.clashroyale.com/v1/tournaments/%23"+str(tag), headers=headers)
    js = page.json()
    print("[+] Name: "+str(js['name']))
    print("[+] Description: "+str(js['description']))
    print("[+] Type: "+str(js['type']))
    print("[+] Status: "+str(js['status']))
    print("[+] Number of participants: "+str(js['capacity']))
    print("[+] Max capacity: "+str(js['maxCapacity'])+" players")
    av = js['maxCapacity'] - js['capacity']
    if av == 0:
        print("[+] No available participations !")
    else:
        print("[+] Available participations: "+str(av))
    print("[+] Preparation duration: "+str(convert(1,convert(1,js['preparationDuration'])))+" hour(s)")
    print("[+] Tournament duration: "+str(convert(2,convert(1,convert(1,js['duration']))))+" day(s)")
    print("[+] Creator's tag: "+str(js['creatorTag']))
    pg = requests.get("https://api.clashroyale.com/v1/players/%23"+str(js['creatorTag']), headers=headers)
    jsn = pg.json()
    print("[+] Creator's name: "+str(jsn['name']))
    print("[+] Creator's clan: "+str(jsn['clan']['name']))
    print("-"*20+"participants".upper()+"-"*20)
    for i in range(len(js['membersList'])):
        print("[+] Name: "+str(js['membersList'][i]['name']))
        print("[+] Tag: "+str(js['membersList'][i]['tag']))
        print("[+] Score: "+str(js['membersList'][i]['score']))
        print("[+] Rank: "+str(js['membersList'][i]['rank']))
        print("[+] Participant's clan: "+str(js['membersList'][i]['clan']['name']))

def UpcEvents():
    page = requests.get("https://api.clashroyale.com/v1/challenges", headers=headers)
    js = page.json()
    retypes = ['resource','consumable','tradeToken','chest']
    for i in range(len(js[:])):
        print("[+] Name: "+str(js[i]['challenges']['name']))
        print("[+] Description: "+str(js[i]['challenges']['description']))
        print("[+] Type: "+str(js[i]['type']))
        print("[+] Max losses: "+str(js[i]['challenges']['maxLosses']))
        print("[+] Gamemode: "+str(js[i]['challenges']['gameMode']['name']))
        print("[+] Icon URL: "+str(js[i]['challenges']['iconUrl']))
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
    Logo()
    print("\n")
    print("[+] Author: new92")
    print("[+] Github: @new92")
    print("\n")
    print("[+] RoyaleInfo: Script which provides info for players, clans, tournaments, cards etc. for Clash Royale")
    print("\n")
    print("[1] Display info for a player")
    print("[2] Display info for a clan")
    print("[3] Display a list of all available cards (Updated)")
    print("[4] Search tournaments")
    print("[5] Display info about a tournament")
    print("[6] Display info about upcoming challenges (most popular)")
    print("[7] Show program's info and exit")
    print("[8] Exit")
    option=int(input("[::] Please enter a number (from the above ones): "))
    while option < 1 or option > 8 or option == None:
        print("[!] Sorry, invalid number !")
        sleep(1)
        option=int(input("[::] Please enter again a number (from the above ones): "))
    if option == 1:
        GetPlayerInfo()
    elif option == 2:
        GetClanInfo()
    elif option == 3:
        Cards()
    elif option == 4:
        tour=str(input("[::] Please enter the name of the tournament: "))
        while tour == None:
            print("[!] Invalid name !")
            sleep(1)
        SearchT(name=tour)
    elif option == 5:
        tag=str(input("[::] Please enter the tag of the tournament (please don't include the tag (#) symbol): "))
        while tag == None or tag[0] == '#':
            print("[!] Invalid tag !")
            sleep(1)
            if tag[0] == '0':
                print("[!] Please DO NOT include the tag (#) symbol in your next input !")
                sleep(1)
            tag=str(input("[::] Please enter the tag of the tournament: "))
        getTourInfo(tag)
    elif option == 6:
        UpcEvents()
    elif option == 7:
        ProgInfo()
    else:
        print("[+] Thank you for using my script 😁")
        sleep(2)
        print("See you next time 👋")
        sleep(1)
        exit(0)
