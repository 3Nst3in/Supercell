"""
Author: new92
Github: @new92
Script built using Supercell's API.
It can be used to display info about a player, a clan, a league, an event etc.
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
    print("[!] WARNING: Not all packages used in this program have been installed !")
    sleep(2)
    print("[+] Ignoring warning...")
    sleep(1)
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
    'authorization': 'Bearer <ENTER YOUR API TOKEN HERE>'
}

def ProgInfo():
    author = 'new92'
    license = 'MIT'
    lang = 'Python'
    language = 'en-US'
    name = 'ClashofInfo'
    api = 'Clash of Clans API'
    lines = 360
    stars = 6
    forks = 4
    print("[+] Author: "+str(author))
    print("[+] Github: @"+str(author))
    print("[+] License: "+str(license))
    print("[+] Programming language(s) used: "+str(lang))
    print("[+] Language(s): "+str(language))
    print("[+] Program's name: "+str(name))
    print("[+] Lines of code: "+str(lines))
    print("[+] API used: "+str(api))
    print("[+] Github repo stars: "+str(stars))
    print("[+] Github repo forks: "+str(forks))
    
def GetUserInfo(tag):
    print("\n")
    tag = tag.upper()
    war = True
    page = requests.get("https://api.clashofclans.com/v1/players/%23"+str(tag), headers=headers)
    js = page.json()
    name = js['name']
    thlvl = js['townHallLevel']
    explvl = js['expLevel']
    trophies = js['trophies']
    highest_trophies = js['bestTrophies']
    warStars = js['warStars']
    attwins = js['attackWins']
    defwins = js['defenseWins']
    bdhlvl = js['builderHallLevel']
    vsTrophies = js['versusTrophies']
    highest_vs_trophies = js['bestVersusTrophies']
    vsWins = js['versusBattleWins']
    role = js['role']
    warpf = js['warPreference']
    dons = js['donations']
    dons_recv = js['donationsReceived']
    ccc = js['clanCapitalContributions']
    clan_tag = js['clan']['tag']
    clan_name = js['clan']['name']
    clanlvl = js['clan']['clanLevel']
    clan_logo = js['clan']['badgeUrls']['medium']
    total_vs_wins = js['versusBattleWinCount']
    labels = js['labels']
    troops = js['troops']
    spells = js['spells']
    if warpf != 'in':
        war = False
    print("-" * 40)
    print("[+] Name: "+str(name))
    print("[+] TownHall level: "+str(thlvl))
    print("[+] Experience level: "+str(explvl))
    print("[+] Number of trophies: "+str(trophies))
    print("[+] Highest number of trophies user reached: "+str(highest_trophies))
    print("[+] Stars from war: "+str(warStars))
    print("[+] Attack wins: "+str(attwins))
    print("[+] Defence wins: "+str(defwins))
    print("[+] BuilderHall level: "+str(bdhlvl))
    print("[+] Versus trophies: "+str(vsTrophies))
    print("[+] Highest number of trophies for versus battles user reached: "+str(highest_vs_trophies))
    print("[+] Versus battle wins: "+str(vsWins))
    print("[+] User's role in clan: "+str(role))
    print("[+] Is active in war: "+str(war))
    print("[+] Donations user made: "+str(dons))
    print("[+] Donations user received: "+str(dons_recv))
    print("[+] Clan capital contributions: "+str(ccc))
    print("[+] Clan's tag: "+str(clan_tag))
    print("[+] Clan's name: "+str(clan_name))
    print("[+] Clan's level: "+str(clanlvl))
    print("[+] Clan's logo: "+str(clan_logo))
    print("[+] Total number of versus battles wins: "+str(total_vs_wins))
    print("[+] User's label(s): "+str(labels))
    print("[+] User own's these troops: "+str(troops))
    print("[+] User own's these spells: "+str(spells))
    print("-" * 40)
def GetClanInfo(tag):
    print("\n")
    print("[1] Get and Display info for a clan")
    print("[2] Get and Display info for the members of a clan")
    print("[3] Search clans")
    option=int(input("[::] Please enter a number (from the above ones): "))
    while option < 1 or option > 4 or option == None:
        print("[!] Invalid number !")
        sleep(1)
        option=int(input("[::] Please enter again the number: "))
    if option == 1:
        disp_mems_info = False
        disp_labs = False
        clan_cap = False
        tag = tag.upper()
        page = requests.get("https://api.clashofclans.com/v1/clans/%23"+str(tag), headers=headers)
        js = page.json()
        name = js['name']
        clan_type = js['type']
        description = js['description']
        loc_name = js['location']['name']
        isCountry = js['isCountry']
        clan_logo = js['badgeUrls']['medium']
        clanlvl = js['clanLevel']
        clan_points = js['clanPoints']
        clan_vs_points = js['clanVersusPoints']
        req_trophies = js['requiredTrophies']
        warf = js['warFrequency']
        wws = js['warWinStreak']
        war_wins = js['warWins']
        war_ties = js['warTies']
        war_losses = js['warLosses']
        is_wlp = js['isWarLogPublic']
        war_league_name = js['warLeague']['name']
        num_of_mems = js['members']
        disp_labels=str(input("[?] Do you want to display the labels of the clan ? [yes/no]"))
        while disp_labels == None or disp_labels != "y" and disp_labels != "yes" and disp_labels != "Yes" and disp_labels != "YES" and disp_labels != "n" and disp_labels != "no" and disp_labels != "No" and disp_labels != "NO":
            print("[!] Sorry invalid input !")
            sleep(1)
            disp_labels=str(input("[?] Do you want to display the labels of the clan ? [yes/no]"))
        if disp_labels == "y" or disp_labels == "yes" or disp_labels == "Yes" or disp_labels == "YES":
            disp_labs = True
        else:
            print("[OK]")
        disp_clan_cap=str(input("[?] Do you want to display info about clan capital ? [yes/no] "))
        while disp_clan_cap == None or disp_clan_cap != "y" and disp_clan_cap != "yes" and disp_clan_cap != "Yes" and disp_clan_cap != "YES":
            print("[!] Sorry invalid input !")
            sleep(1)
            disp_clan_cap=str(input("[?] Do you want to display info about clan capital ? [yes/no] "))
        if disp_clan_cap == "y" or disp_clan_cap == "yes" or disp_clan_cap == "Yes" or disp_clan_cap == "YES":
            clan_cap = True
        else:
            print("[OK]")
        req_vs_trophies = js['requiredVersusTrophies']
        req_th_lvl = js['requiredTownhallLevel']
        chat_lang_name = js['chatLanguage']['name']
        print("-" * 40)
        print("[+] Name: "+str(name))
        print("[+] Type: "+str(clan_type))
        print("[+] Description: "+str(description))
        print("[+] Location: "+str(loc_name))
        print("[+] Is country: "+str(isCountry))
        print("[+] Logo: "+str(clan_logo))
        print("[+] Level: "+str(clanlvl))
        print("[+] Points: "+str(clan_points))
        print("[+] VS battle points: "+str(clan_vs_points))
        print("[+] Required Trophies: "+str(req_trophies))
        print("[+] War frequency: "+str(warf))
        print("[+] Current war win streak: "+str(wws))
        print("[+] War wins: "+str(war_wins))
        print("[+] War ties: "+str(war_ties))
        print("[+] War losses: "+str(war_losses))
        print("[+] Is war log public: "+str(is_wlp))
        print("[+] War league: "+str(war_league_name))
        print("[+] Number of members: "+str(num_of_mems))
        print("[+] Required VS trophies: "+str(req_vs_trophies))
        print("[+] Required town hall level: "+str(req_th_lvl))
        print("[+] Chat language: "+str(chat_lang_name))
        if disp_labs == True:
            print(js['labels'])
        if clan_cap == True:
            print(js['clanCapital'])
        print("-" * 40)
    elif option == 2:
        print("\n")
        count=int(input("[::] Please enter the number of members to display: "))
        while count == None or count == 0:
            print("[!] Sorry, invalid input !")
            sleep(1)
            count=int(input("[::] Please enter again the number of members to display: "))
        page = requests.get(f"https://api.clashofclans.com/v1/clans/%23{tag}/members?limit={count}", headers=headers)
        js = page.json()
        print("[+] Information: ")
        print("-" * 40)
        print("\n")
        print(js['items'])
        print("\n")
        print("-" * 40)
    elif option == 3:
        print("\n")
        name=str(input("[::] Please enter the name of the clan: "))
        while name == None:
            print("[!] Sorry, invalid name !")
            sleep(1)
            name=str(input("[::] Please enter again the name of the clan: "))
        count=int(input("[?] How many results to display (enter an integer number) ? "))
        while count == None or count == 0:
            print("[!] Sorry, invalid number !")
            sleep(1)
            count=int(input("[?] How many results to display (enter an integer number) ? "))
        page = requests.get(f"https://api.clashofclans.com/v1/clans?name={name}&limit={count}", headers=headers)
        js = page.json()
        wl_pub = "yes"
        for i in range(len(js['items'])):
            print("[+] Clan name: "+str(js['items']['name']))
            print("[+] Type: "+str(js['items']['type']))
            print("[+] Location: "+str(js['items']['location']['name']))
            print("[+] Badge: "+str(js['items']['badgeUrls']['medium']))
            print("[+] Level: "+str(js['items']['clanLevel']))
            print("[+] Points: "+str(js['items']['clanPoints']))
            print("[+] Versus points: "+str(js['items']['clanVerusPoints']))
            print("[+] Required trophies: "+str(js['items']['requiredTrophies']))
            print("[+] War frequency: "+str(js['items']['warFrequency']))
            print("[+] War win streak: "+str(js['items']['warWinStreak']))
            print("[+] War wins: "+str(js['items']['warWins']))
            print("[+] War ties: "+str(js['items']['warTies']))
            print("[+] War losses: "+str(js['items']['warLosses']))
            if not js['items']['isWarLogPublic']:
                wl_pub = "no"
            print("[+] Is the war log public ? "+str(wl_pub))
            print("[+] War league: "+str(js['items']['warLeague']['name']))
            print("[+] Required versus trophies: "+str(js['items']['requiredVersusTrophies']))
            print("[+] Required TownHall level: "+str(js['items']['requiredTownhallLevel']))
            print("[+] Chat language: "+str(js['items']['chatLanguage']['name']))
            print("[+] Number of members: "+str(js['items']['members']))

def GetLeagueInfo(id):
    print("\n")
    print("[1] Display a list of leagues")
    print("[2] Display info about a league")
    option=int(input("[::] Please enter a number (from the above ones): "))
    while option < 1 or option > 3 or option == None:
        print("[!] Sorry, invalid number !")
        sleep(1)
        option=int(input("[::] Please enter again the number of the option: "))
    if option == 1:
        count=int(input("[::] Please enter the amount: "))
        while count == None or count == 0:
            print("[!] Sorry, invalid number !")
            sleep(1)
            count=int(input("[::] Please enter again the amount: "))
        page = requests.get("https://api.clashofclans.com/v1/leagues?limit="+str(count), headers=headers)
        js = page.json()
        print("[+] List of leagues: ")
        print("-" * 30)
        print("\n")
        print(js['items'])
    elif option == 2:
        page = requests.get("https://api.clashofclans.com/v1/leagues/"+str(id), headers=headers)
        js = page.json()
        name = js['name']
        small_icon_url = js['iconUrls']['small']
        medium_icon_url = js['iconUrls']['medium']

        print("-" * 40)
        print("[+] Name: "+str(name))
        print("[+] Small size icon url: "+str(small_icon_url))
        print("[+] Medium size icon url: "+str(medium_icon_url))
        print("-" * 40)
    else:
        print("[+] Exiting...")
        quit(0)


print("""
░█████╗░██╗░░░░░░█████╗░░██████╗██╗░░██╗   ░█████╗░███████╗   ██╗███╗░░██╗███████╗░█████╗░
██╔══██╗██║░░░░░██╔══██╗██╔════╝██║░░██║   ██╔══██╗██╔════╝   ██║████╗░██║██╔════╝██╔══██╗
██║░░╚═╝██║░░░░░███████║╚█████╗░███████║   ██║░░██║█████╗░░   ██║██╔██╗██║█████╗░░██║░░██║
██║░░██╗██║░░░░░██╔══██║░╚═══██╗██╔══██║   ██║░░██║██╔══╝░░   ██║██║╚████║██╔══╝░░██║░░██║
╚█████╔╝███████╗██║░░██║██████╔╝██║░░██║   ╚█████╔╝██║░░░░░   ██║██║░╚███║██║░░░░░╚█████╔╝
░╚════╝░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝   ░╚════╝░╚═╝░░░░░   ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░
""")
print("\n")
print("[+] Author: new92")
print("[+] Github: @new92")
print("\n")
print("[+] Description: Script for getting information (on Clash of Clans videogame) about clans, users, leagues and much more... :)")
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
    id=str(input("[::] Please enter the tag of the user's account (please do not include the tag(#) symbol): "))
    while id == None or id[0] == '#':
        print("[!] Invalid tag !")
        sleep(1)
        if id[0] == '#':
            print("[!] Please DO NOT include the tag (#) symbol in your next input !")
        id=str(input("[::] Please enter again the tag of the user's account (do not include the tag(#) symbol): "))
    GetUserInfo(id)
elif option == 2:
    id=str(input("[::] Please enter the tag of the user's account (please do not include the tag(#) symbol): "))
    while id == None or id[0] == '#':
        print("[!] Invalid tag !")
        sleep(1)
        if id[0] == '#':
            print("[!] Please DO NOT include the tag (#) symbol in your next input !")
        id=str(input("[::] Please enter again the tag of the user's account (do not include the tag(#) symbol): "))
    GetClanInfo(id)
elif option == 3:
    id=str(input("[::] Please enter the tag of the user's account (please do not include the tag(#) symbol): "))
    while id == None or id[0] == '#':
        print("[!] Invalid tag !")
        sleep(1)
        if id[0] == '#':
            print("[!] Please DO NOT include the tag (#) symbol in your next input !")
        id=str(input("[::] Please enter again the tag of the user's account (do not include the tag(#) symbol): "))
    GetLeagueInfo(id)
elif option == 4:
    ProgInfo()
else:
    print("[+] Thank you for using my script 😁")
    sleep(2)
    print("See you next time 👋")
    sleep(1)
    exit(0)
