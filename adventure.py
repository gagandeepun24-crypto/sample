import random
import time
import os

# Utility for dramatic effect
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# Clear screen for cleaner UI
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Game intro
clear()
print("================================")
print("      🗡️ THE DARK FOREST 🗡️")
print("================================")

name = input("Enter your name, brave adventurer: ")

clear()
slow_print(f"\nWelcome, {name}!")
slow_print("You wake up in a mysterious forest...")
slow_print("🌲 The trees whisper secrets of old.")
slow_print("You see a dark cave 🕳️ and an ancient castle 🏰.")
slow_print("A glowing path ✨ also appears behind you.")

choice = input("\nWhere do you want to go? (cave/castle/path): ").lower()

# CAVE
if choice == "cave":
    clear()
    slow_print("\nYou enter the dark cave...")
    slow_print("Suddenly, a monster 👹 appears!")

    fight = input("Do you want to fight or run? (fight/run): ").lower()

    if fight == "fight":
        player = random.randint(1, 12)
        monster = random.randint(1, 12)

        slow_print(f"\n⚔️ Your power: {player}")
        slow_print(f"👹 Monster power: {monster}")

        if player > monster:
            slow_print("\n⚔️ You defeated the monster!")
            slow_print("💰 You found 200 gold coins!")
            slow_print("✨ A secret tunnel leads you to freedom!")
            slow_print("🏆 YOU WIN!")
        elif player < monster:
            slow_print("\n💀 The monster defeated you!")
            slow_print("GAME OVER!")
        else:
            slow_print("\n😮 It's a draw! You escape safely.")

    elif fight == "run":
        slow_print("\n🏃 You escaped from the cave!")
        slow_print("But you got lost in the forest...")
        slow_print("GAME OVER!")

    else:
        slow_print("\n❌ Invalid choice!")

# CASTLE
elif choice == "castle":
    clear()
    slow_print("\nYou enter the mysterious castle...")
    slow_print("There are three doors 🚪")
    slow_print("1. A red door 🔴")
    slow_print("2. A blue door 🔵")
    slow_print("3. A golden door 🟡")

    door = input("\nWhich door do you choose? (red/blue/golden): ").lower()

    if door == "red":
        slow_print("\n🔥 The room is full of fire!")
        slow_print("You quickly escape!")
        slow_print("GAME OVER!")

    elif door == "blue":
        slow_print("\n✨ You found a treasure room!")
        slow_print("💎 You found a legendary diamond!")
        slow_print("🏆 YOU WIN!")

    elif door == "golden":
        slow_print("\n👑 You enter a throne room...")
        slow_print("A ghost king appears and offers you a crown.")
        crown = input("Do you accept the crown? (yes/no): ").lower()
        if crown == "yes":
            slow_print("\n👑 You become ruler of the castle!")
            slow_print("🏆 YOU WIN!")
        else:
            slow_print("\n👻 The ghost king curses you...")
            slow_print("GAME OVER!")

    else:
        slow_print("\n❌ Invalid choice!")

# PATH
elif choice == "path":
    clear()
    slow_print("\nYou follow the glowing path...")
    slow_print("It leads to a magical lake 🌊")
    slow_print("A fairy 🧚 offers you a wish.")
    wish = input("Do you wish for power or wisdom? (power/wisdom): ").lower()

    if wish == "power":
        slow_print("\n⚡ You gain immense strength!")
        slow_print("You defeat all enemies in the forest.")
        slow_print("🏆 YOU WIN!")

    elif wish == "wisdom":
        slow_print("\n📜 You gain infinite knowledge!")
        slow_print("You discover the secrets of the forest.")
        slow_print("🏆 YOU WIN!")

    else:
        slow_print("\n❌ Invalid choice!")

else:
    slow_print("\n❌ You got confused and wandered into the forest.")
    slow_print("GAME OVER!")

slow_print("\nThanks for playing! 🎮")
