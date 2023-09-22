from time import sleep
from texts import *
from characters import characters

for i in range(len(graphics)):
    print(graphics[i], sep='', end='', flush=True); sleep(0.02)
print()
for i in range(len(heading)):
    print(heading[i], sep='', end='', flush=True); sleep(0.02)
print()
for i in range(len(graphics)):
    print(graphics[i], sep='', end='', flush=True); sleep(0.02)
print("\n")

for i in range(len(start_game)):
    print(start_game[i], sep='', end='', flush=True); sleep(0.02)
print()

print("\nAvailable characters:")
for idx, char in enumerate(characters):
    print(f"{idx + 1}. {char['name']} {char['emoji']}: (Health: {char['health']}, Attack: {char['attack']})")

selected_character = None

while selected_character is None:
    try:
        choice = int(input("Select a character by entering its number: "))
        if 1 <= choice <= len(characters):
            selected_character = characters[choice - 1]
        else:
            print("Invalid choice. Please select a valid character.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"You selected {selected_character['name']}!")



