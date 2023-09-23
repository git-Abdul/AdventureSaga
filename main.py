from time import sleep
from texts import *
from characters import characters
import pyfiglet
from colorama import Fore, Style

selected_character = None
chosen_char = None
character_selected = False

TITLE_COLOR = Fore.CYAN
INFO_COLOR = Fore.GREEN
ERROR_COLOR = Fore.RED
PROMPT_COLOR = Fore.YELLOW
RESET_COLOR = Style.RESET_ALL

def print_colored(text, color):
    print(color + text + RESET_COLOR, end='', flush=True)

for i in range(len(graphics)):
    print_colored(graphics[i], TITLE_COLOR)
    sleep(0.02)
print()

text = pyfiglet.figlet_format(text="Adventure Saga")
print_colored(text, TITLE_COLOR)

for i in range(len(graphics)):
    print_colored(graphics[i], TITLE_COLOR)
    sleep(0.02)
print("\n")

def select_char():
    global selected_character
    selected_character = None
    while selected_character is None:
        try:
            choice = int(input(f"{PROMPT_COLOR}Select a character by entering its number: {RESET_COLOR}"))
            if 1 <= choice <= len(characters):
                selected_character = characters[choice - 1]
            else:
                print_colored("Invalid choice. Please select a valid character.\n", ERROR_COLOR)
        except ValueError:
            print_colored("Invalid input. Please enter a number.\n", ERROR_COLOR)

def char_select():
    global selected_character
    global chosen_char
    global character_selected
    while selected_character is None:
        try:
            print_colored("\nAvailable characters:\n", INFO_COLOR)
            for idx, char in enumerate(characters):
                print(
                    f"{idx + 1}. {char['name']} {char['emoji']}: (Health: {char['health']}, Attack: {char['attack']})")

            choice = int(input(f"{PROMPT_COLOR}Select a character by entering its number: {RESET_COLOR}"))
            if 1 <= choice <= len(characters):
                selected_character = characters[choice - 1]
                print_colored(f"\nYou selected {selected_character['name']}!\n", INFO_COLOR)
                print(f"\n 📜 Description: {selected_character['description']}\n\n")
                print(f" 🗡️ Attack: {selected_character['attack']}\n")
                print(f" 🩹 Health: {selected_character['health']}\n")
                choice = input(f"Choose character {selected_character['name']}? (yes/no): ")
                if choice == 'yes':
                    chosen_char = selected_character
                    print_colored(f"Chosen character: {chosen_char['name']}", INFO_COLOR)
                    character_selected = True
                else:
                    selected_character = None
            else:
                print_colored("Invalid choice. Please select a valid character.\n", ERROR_COLOR)
        except ValueError:
            print_colored("Invalid input. Please enter a number.\n", ERROR_COLOR)

while not character_selected:
    try:
        print_colored("\nGame menu:\n", INFO_COLOR)
        print("1. Start\n2. About\n3. Version")
        choice = input(f"{PROMPT_COLOR}Select an option by entering its number: {RESET_COLOR}")
        if choice == "1":
            char_select()
        elif choice == "2":
            print_colored("This is the Adventure Saga game.\n", INFO_COLOR)
        elif choice == "3":
            print_colored("Adventure Saga Version 1.0\n", INFO_COLOR)
        else:
            print_colored("Invalid choice. Please select a valid option.\n", ERROR_COLOR)
    except ValueError:
        print_colored("Invalid input. Please enter the option number.\n", ERROR_COLOR)
