import requests
import sys
import pyfiglet

print(pyfiglet.figlet_format("Bedwars Tracker"))

print("="*60)
while True:
    try:
        player = input("\nEnter the name of the target: ")
        API_KEY = "3bc7d52f-43f0-49dc-ad01-1af2342d8e2f"
        if requests.get(f"https://api.mojang.com/users/profiles/minecraft/{player}").status_code == 200:
            uuid = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{player}").json()["id"]
            try:
                data = requests.get(f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}").json()
                if data["success"]:
                    statistiques = data["player"]["stats"]["Bedwars"]
                    try:
                        print(f"Number of game: {int(statistiques['beds_lost_bedwars'])+int(statistiques['wins_bedwars'])}")
                        print(f"Lits detruit: {statistiques['beds_broken_bedwars']}")
                        print(f"All kills: {statistiques['kills_bedwars']}")
                        print(f"Finals kills: {statistiques['final_kills_bedwars']}")
                        print(f"Win: {statistiques['wins_bedwars']}")
                        print(f"Loose: {statistiques['beds_lost_bedwars']}")
                        print(f"Win rate: {round(int(statistiques['wins_bedwars'])/int(statistiques['beds_lost_bedwars']), 2)}")
                        print(f"Void Death: {statistiques['void_deaths_bedwars']}")
                        print(f"Fall Death: {statistiques['fall_deaths_bedwars']}")
                        print("="*60)
                    except:
                        print(f"An error occurred while getting {player}'s stats.\nMaybe the account is too young or doesn't play much.")
                else:
                    print("An error occurred while requesting the Hypixel API.")
                    print(data["cause"])

            except requests.exceptions.RequestException as e:
                print("An error occurred during the request to the Hypixel API.")
                print(e)
        else:
            print("An error occured.")
        input("Press enter for finished...")
        sys.exit()
    except KeyboardInterrupt:
        break