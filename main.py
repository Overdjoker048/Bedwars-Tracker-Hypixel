import requests
import os
import sys
import colorama
import pyfiglet
import platform

print(pyfiglet.Figlet(font='Bedwars Tracker').renderText('text to render'))

colorama.init()
print(colorama.Fore.GREEN)

if platform.system() == "Windows":
    os.system("title Bedwars Tracker")
elif platform.system() == "Linux":
    os.system("sudo apt-get install xtitle")
    os.system("xtitle 'Bedwars Tracker'")
elif platform.system() == "Darwin":
    os.system("touch 'Bedwars Tracker'")

player = input("Enter the name of the target: ")
API_KEY = "Hypixel API Key "
if requests.get(f"https://api.mojang.com/users/profiles/minecraft/{player}").status_code == 200:
    uuid = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{player}").json()["id"]
    try:
        data = requests.get(f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}").json()
        if data["success"]:
            statistiques = data["player"]["stats"]["Bedwars"]
            print(f"Number of game: {int(statistiques['beds_lost_bedwars'])+int(statistiques['wins_bedwars'])}")
            print(f"Lits detruit: {statistiques['beds_broken_bedwars']}")
            print(f"All kills: {statistiques['kills_bedwars']}")
            print(f"Finals kills: {statistiques['final_kills_bedwars']}")
            print(f"Win: {statistiques['wins_bedwars']}")
            print(f"Loose: {statistiques['beds_lost_bedwars']}")
            print(f"Win rate: {round(int(statistiques['wins_bedwars'])/int(statistiques['beds_lost_bedwars']), 2)}")
            print(f"Void Death: {statistiques['void_deaths_bedwars']}")
            print(f"Fall Death: {statistiques['fall_deaths_bedwars']}")
            input("Press enter for finished...")
            sys.exit()
        else:
            print("An error occurred while requesting the Hypixel API.")
            print(data["cause"])

    except requests.exceptions.RequestException as e:
        print("An error occurred during the request to the Hypixel API.")
        print(e)
else:
    print("An error as occured.")
    input("Press enter for finished...")
    sys.exit()
