from time import sleep
from texts import *
from arrays import *
import pyfiglet
from colorama import Fore, Style

selected_character = None  # Select character menu
chosen_char = None  # Select a character
character_selected = False  # Is any character selected
selected_object = None  # Any object selected for the menu
exit_obj1 = False  # Exit function
exit_obj2 = None # Exit function 2
sword_taken = False  # Is the sword interacted with?
path = None # What path selected?

TITLE_COLOR = Fore.CYAN
INFO_COLOR = Fore.GREEN
ERROR_COLOR = Fore.RED
PROMPT_COLOR = Fore.YELLOW
TEXT_COLOR = Fore.BLUE
RESET_COLOR = Style.RESET_ALL

def print_colored(text, color):
    print(color + text + RESET_COLOR, end='', flush=True)

# Print title
for i in range(len(graphics)):
    print_colored(graphics[i], TITLE_COLOR)
    sleep(0.02)
print()

text = pyfiglet.figlet_format(text="Runez", font="isometric1")
print_colored(text, TITLE_COLOR)

# Print title again
for i in range(len(graphics)):
    print_colored(graphics[i], TITLE_COLOR)
    sleep(0.02)
print("\n")

def start_game():
    global chosen_char
    global selected_object
    global exit_obj1
    global exit_obj2
    global sword_taken
    global attack_Value
    global health_Value
    global path

    if chosen_char is None:
        print_colored("You need to select a character first.\n", ERROR_COLOR)
        return

    for i in range(len(start_text)):
        print_colored(start_text[i], TEXT_COLOR)
        sleep(0.001)
    name = str(input(f"{PROMPT_COLOR}Now tell us your name by which you would like to be called: {RESET_COLOR}"))
    print()
    for i in range(len(graphics)):
        print_colored(graphics[i], TITLE_COLOR)
        sleep(0.02)
    print(village, "\n\n")
    for i in range(len(graphics)):
        print_colored(graphics[i], TITLE_COLOR)
        sleep(0.02)
    print("\n")
    name_text = f"Welcome home {name}! This is now your village to protect and people to serve... Now, let's start by getting you a sword!\n"
    for i in range(len(name_text)):
        print_colored(name_text[i], TEXT_COLOR)
        sleep(0.001)
    print_colored(f"You wake up in your room, here's what you find lying around nearby:", TEXT_COLOR)

    print_colored("\n\nAvailable objects:\n\n", INFO_COLOR)
    for idx, obj in enumerate(room_objects):
        print(f"{idx + 1}. {INFO_COLOR}Object name:{RESET_COLOR} {obj['name']}; {INFO_COLOR}Object description:{RESET_COLOR} {obj['desc']}\n")

    while exit_obj1 is False:
        global exit_obj2
        choice = input(f"{PROMPT_COLOR}Enter object number to interact with: {RESET_COLOR}")
        if not choice:
            continue
        try:
            choice = int(choice)
            if 1 <= choice <= len(room_objects):
                selected_object = room_objects[choice - 1]
                if selected_object['name'] == "Sword":
                    sword_taken = True
                    if 'sword_used' not in chosen_char:
                        chosen_char['sword_used'] = True
                        attack_Value = chosen_char['attack'] + selected_object['attack'] 
                        print(f"{selected_object['interaction']} Your attack stats: {chosen_char['attack']} + {selected_object['attack']} = {chosen_char['attack'] + selected_object['attack']}")
                    else:
                        print(f"You've already used the sword.")
                elif selected_object['name'] == 'Lantern':
                    if 'lantern_lit' not in chosen_char:
                        chosen_char['lantern_lit'] = True
                        print(f"You have chosen to interact with {selected_object['name']}.")
                        print(f"{selected_object['interaction']}")
                    else:
                        print(f"You've already lit the lantern.")
                elif selected_object['name'] == 'Scroll':
                    if 'scroll_opened' not in chosen_char:
                        chosen_char['scroll_opened'] = True
                        print(f"You have chosen to interact with {selected_object['name']}.")
                        print(f"{selected_object['interaction']}")
                    else:
                        print(f"You've already opened the scroll.")
                elif selected_object['name'] == 'Exit':
                    if not sword_taken:
                        print_colored("You haven't taken the sword yet!\n", ERROR_COLOR)
                    else:
                        print_colored("You have left the room.\n\n", INFO_COLOR)
                        print_colored("Leaving the room, you see three paths, which one would you take?", PROMPT_COLOR)
                        print_colored("\nAvailable Paths:\n\n", INFO_COLOR)
                        for idx, obj in enumerate(paths):
                            print(f"{idx + 1}. {INFO_COLOR}Path name:{RESET_COLOR} {obj['name']}; {INFO_COLOR}Path description:{RESET_COLOR} {obj['desc']}\n")
                        
                        global exit_obj2
                        exit_obj2 = False
                        exit_obj1 = True
                else:
                    print("You have chosen to exit the room.")
            else:
                print_colored("Invalid choice.\n", ERROR_COLOR)
        except ValueError:
            print_colored("Invalid input. Please enter a number.\n", ERROR_COLOR)
        
        #Choosing a path - 1
        while exit_obj2 is False:
            choice = input(f"{PROMPT_COLOR}Choose your path by entering the path number: {RESET_COLOR}")
            try:
                choice = int(choice)
                if 1 <= choice <= len(paths):
                    path = paths[choice - 1]
                    if path['name'] == "Forest Path":
                        print("You embark on a daring journey into the heart of the dark forest. The trees loom overhead, and mysterious sounds surround you.")
                        exit_obj2 = True
                    elif path['name'] == "Cave Entrance":
                        print("You venture into the cave, and the entrance disappears behind you. The darkness is absolute, and the cave walls seem to whisper secrets.")
                        exit_obj2 = True
                    elif path['name'] == "Mountain Trail":
                        print("You approach the entrance of the mountain trail. The path winds steeply upward, and the air becomes thinner. Your adventure to the peaks begins.")
                        exit_obj2 = True
                else:
                    print_colored("Invalid choice.\n", ERROR_COLOR)
            except ValueError:
                print_colored("Invalid input. Please enter a number.\n", ERROR_COLOR)

                

# Select character function
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

# Character selection function
def char_select():
    global selected_character
    global chosen_char
    global character_selected
    global attack_Value
    global health_Value
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
                print(f"\n📜 Description: {selected_character['description']}\n\n")
                print(f"🗡️ Attack: {selected_character['attack']}\n")
                print(f"🩹 Health: {selected_character['health']}\n")
                choice = input(f"{PROMPT_COLOR}Choose character {selected_character['name']}? (yes/no): {RESET_COLOR}")
                if choice == 'yes':
                    chosen_char = selected_character
                    health_Value = chosen_char['health']
                    attack_Value = chosen_char['attack']
                    print_colored(f"Chosen character: {chosen_char['name']}\n\n", INFO_COLOR)
                    start_game()
                    character_selected = True
                else:
                    selected_character = None
            else:
                print_colored("Invalid choice. Please select a valid character.\n", ERROR_COLOR)
        except ValueError:
            print_colored("Invalid input. Please enter a number.\n", ERROR_COLOR)

# Main game loop
while not character_selected:
    try:
        print_colored("\nGame menu:\n", INFO_COLOR)
        print("1. Start\n2. About\n3. Version")
        choice = input(f"{PROMPT_COLOR}Select an option by entering its number: {RESET_COLOR}")
        if choice == "1":
            char_select()
        elif choice == "2":
            print_colored("An ASCII art game made using Python that can be played in the terminal itself. \n", INFO_COLOR)
        elif choice == "3":
            print_colored("Runez Version Alpha 0.1\n", INFO_COLOR)
        else:
            print_colored("Invalid choice. Please select a valid option.\n", ERROR_COLOR)
    except ValueError:
        print_colored("Invalid input. Please enter the option number.\n", ERROR_COLOR)
