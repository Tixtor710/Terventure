#A space-based adventure of a crew of curious individuals exploring an unknown galaxy.
#A “Day in the Life” story that walks you through choices the main character makes based on conditions like the time of day, the actions that the player take, etc.
#A classic mini-RPG (role-playing game) with hp health points, character moves like attack/block/heal, and NPCs (non-player characters) that attacks based on a random number generator.
import time

def intro():
    print("\n=== TERMINAL ADVENTURE ===")
    print("A space-based saga across the stars...\n")
    time.sleep(1)

    char_name = input("🌠 Enter your character's name: ").strip().title()

    print(f"\nWelcome aboard, {char_name}.")
    print("Your personality will shape your fate... Choose wisely.\n")

    print("Choose your role:")
    print("1. The Warrior")
    print("2. The Lone Wolf")
    print("3. The Trickster")

    valid_roles = {"1": "The Warrior", "2": "The Lone Wolf", "3": "The Trickster"}
    
    role_input = input("Enter the number or name of your role: ").strip().lower()
    role = None

    # Normalize input
    for key, value in valid_roles.items():
        if role_input == key or role_input == value.lower():
            role = value
            break

    if not role:
        print("❌ Invalid choice. Defaulting to 'The Wanderer'.")
        role = "The Wanderer"

    print()
    print_role_intro(char_name, role)
    return Player(char_name, role)


def print_role_intro(name, role):
    print(f"🧬 Initializing profile: {name} the {role}\n")
    time.sleep(1)

    if role == "The Warrior":
        print("⚔️ A day in the life of a warrior is filled with danger, but your crew stands beside you.")
    elif role == "The Lone Wolf":
        print("🐺 Trouble follows you like a shadow, but your strength knows no master.")
    elif role == "The Trickster":
        print("🎭 You dance on the edge of chaos, charming fate into your favor.")
    else:
        print("🌌 A mysterious traveler, your path is yours to write.")


class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.hp = 100
        self.inventory = []
        # Future stats: attack, defense, alignment, etc.

    def status(self):
        print(f"{self.name} the {self.role} | HP: {self.hp}")


# === Entry Point ===
if __name__ == "__main__":
    player = intro()
    # player.status()  # Optional debug
    print("\nYour adventure begins now...\n")
    time.sleep(1)
    