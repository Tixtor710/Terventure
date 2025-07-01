import time
import random

class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.hp = 100

def intro():
    print("\n=== TERMINAL ADVENTURE: The Key of SAAT-NUAST ===")
    time.sleep(1)

    print("Year 4052. The Luken Empire governs the stars.")
    time.sleep(2)

    print("\nFour great houses form the ruling council:")
    print("- Deleak: The house of Prophecy")
    print("- Dnert: Warriors and Engineers of Silock")
    print("- Delins: Healers of Foszen")
    print("- Dez: Tricksters of Qazta")
    time.sleep(3)

    print("\nBut one house has been erased from history — Aphis.")
    print("The Aphisites were forced into labor. Their history? Scrubbed.")
    time.sleep(2)

    print("\nA prophecy is seen by House Deleak...")
    print("A key lies hidden in the ruins of SAAT-NUAST. It grants wisdom beyond time.")
    time.sleep(2)

    name = input("\n🌠 What is your name, traveler? ").strip().title()
    print(f"\nWelcome, {name}.")

    print("\nChoose your origin:")
    print("1. The Warrior")
    print("2. The Lone Wolf")
    print("3. The Trickster")
    print("4. The Wanderer")

    role_input = input("Enter the number or name of your role: ").strip().lower()
    roles = {
        "1": "The Warrior",
        "2": "The Lone Wolf",
        "3": "The Trickster",
        "4": "The Wanderer"
    }

    role = None
    for key, value in roles.items():
        if role_input == key or role_input == value.lower():
            role = value
            break

    if not role:
        print("Invalid choice. Defaulting to 'The Wanderer'.")
        role = "The Wanderer"

    print()
    print(f"\n🧐 Initializing genetic profile: {name} the {role}...\n")
    time.sleep(2)
    return Player(name, role)

def main_story(player):
    role_functions = {
        "The Warrior": warrior_story,
        "The Lone Wolf": lone_wolf_story,
        "The Trickster": trickster_story,
        "The Wanderer": wanderer_story
    }
    role_func = role_functions.get(player.role, wanderer_story)
    role_func(player)

def end_with_key():
    print("\nYou stand before the Key of Infinite Knowledge. It glows in your grasp.")
    print("\nWhat will you do?")
    print("1. Use the Key to reveal the truth.")
    print("2. Destroy the Key to protect the galaxy.")
    print("3. Hide the Key and keep its secret.")

    choice = input("Choose your ending: ").strip()
    print()
    if choice == "1":
        print("💁 You expose the history and truths hidden for centuries.")
        print("The Luken Empire fractures. The age of secrets ends.")
    elif choice == "2":
        print("🔥 You destroy the Key. The galaxy is safe... but unchanged.")
        print("The silence remains. But no power shall abuse this wisdom.")
    elif choice == "3":
        print("🧘 You vanish into the void. The Key sleeps once more.")
        print("The story ends in whispers and shadows.")
    else:
        print("The Key vanishes. A chance lost to hesitation.")

    print("\n=== END OF CHAPTER ONE ===")

def warrior_story(player):
    print("\n🗡️ You are a proud soldier of House Dnert. Loyal. Feared. Feared.")
    time.sleep(2)

    print("\nYou raid a rebel base. Inside: civilians. The squad leader says: 'Take the shot!'")
    print("1. Obey.")
    print("2. Disobey.")
    print("3. Fake report.")

    choice = input("Choose your action: ").strip()

    if choice == "1":
        print("You fire. The child screams. Guilt follows.")
        player.hp -= 10
    elif choice == "2":
        print("You refuse. You're demoted. But the innocent live.")
        player.hp += 10
    elif choice == "3":
        print("You lie. 'All clear.' They live. But trust is thin.")
        player.hp += 5
    else:
        print("You freeze. Someone else fires. Innocents die.")
        player.hp -= 5

    time.sleep(2)
    print("\nYou reach SAAT-NUAST...")
    end_with_key()

def lone_wolf_story(player):
    print("\n🐅 Your past is ash. Wife and child lost in crossfire.")
    print("You live for vengeance.")
    time.sleep(2)

    print("\nYou find the Dnert captain who led the operation.")
    print("1. Kill him.")
    print("2. Interrogate.")
    print("3. Walk away.")

    choice = input("Choose your action: ").strip()

    if choice == "1":
        print("His blood spills. Your pain dulls. Justice or revenge?")
        player.hp -= 10
    elif choice == "2":
        print("He confesses. Names, dates. You record everything.")
        player.hp += 10
    elif choice == "3":
        print("You walk away. Pain intact. But stronger.")
        player.hp += 5
    else:
        print("You hesitate. He escapes. Regret lingers.")
        player.hp -= 5

    time.sleep(2)
    print("\nSAAT-NUAST awaits...")
    end_with_key()

def trickster_story(player):
    print("\n🎭 You are the Joke. The Outsider. They laughed. You came anyway.")
    time.sleep(2)

    print("\nThe ruins test your mind. An AI offers a riddle:")
    print("'I speak without a mouth and hear without ears. I have no body, but I come alive with wind.'")
    print("1. Answer: Echo")
    print("2. Answer: Silence")
    print("3. Answer: Memory")

    choice = input("Choose your answer: ").strip()

    if choice == "1":
        print("Correct. The AI bows. A path opens.")
        player.hp += 10
    elif choice == "2":
        print("Incorrect. You are hit by psychic backlash.")
        player.hp -= 10
    elif choice == "3":
        print("Wrong. The door stays shut. You break it.")
        player.hp -= 5
    else:
        print("No answer. The AI vanishes. You sneak past.")

    time.sleep(2)
    print("\nYou reach the heart of SAAT-NUAST...")
    end_with_key()

def wanderer_story(player):
    print("\n🧰 No banners. No name. You are a ghost of House Aphis.")
    print("You were never supposed to matter. You came anyway.")
    time.sleep(2)

    print("\nInside the ruins, you find carvings — your people’s language.")
    print("They built SAAT-NUAST. Their history lives here.")

    print("\nDo you:")
    print("1. Record everything.")
    print("2. Deface the empire’s symbols.")
    print("3. Say nothing and continue.")

    choice = input("Choose your action: ").strip()

    if choice == "1":
        print("You copy every mark. Your history will be heard.")
        player.hp += 10
    elif choice == "2":
        print("You rage. You scar their lies. But lose strength.")
        player.hp -= 10
    elif choice == "3":
        print("You move on. But your heart burns.")
        player.hp += 0
    else:
        print("Indecision. The ghosts whisper... and fade.")

    time.sleep(2)
    print("\nYou find the Key, Aphisite.")
    end_with_key()

# === Run Game ===
if __name__ == "__main__":
    player = intro()
    main_story(player)
