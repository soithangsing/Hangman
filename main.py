import inquirer
import random

program_title_art = r"""______  __                                               
___  / / /_____ ______________ _______ _________ _______ 
__  /_/ /_  __ `/_  __ \_  __ `/_  __ `__ \  __ `/_  __ \
_  __  / / /_/ /_  / / /  /_/ /_  / / / / / /_/ /_  / / /
/_/ /_/  \__,_/ /_/ /_/_\__, / /_/ /_/ /_/\__,_/ /_/ /_/ 
                       /____/                            """

print(program_title_art)

hangman_start = r"""    +---+
        |
        |
        |
        |
        | """
print(hangman_start)

hangman_main_scene_1 = r"""    +---+
    |   |
        |
        |
        |
        | """

hangman_main_scene_2 = r"""    +---+
    |   |
    0   |
        |
        |
        | """

hangman_main_scene_3 = r"""    +---+
    |   |
    0   |
   /    |
        |
        | """

hangman_main_scene_4 = r"""    +---+
    |   |
    0   |
   /|   |
        |
        | """

hangman_main_scene_5 = r"""    +---+
    |   |
    0   |
   /|\  |
        |
        | """

hangman_main_scene_6 = r"""    +---+
    |   |
    0   |
   /|\  |
   /    |
        | """

hangman_main_scene_7 = r"""    +---+
    |   |
    0   |
   /|\  |
   / \  |
        | """


# for i in range(7):
#     variable_store = "hangman_main_scene_" + str(i + 1)
#     print(globals()[variable_store])

easy_hangman_word_list = [
"Cat",
"Dog",
"Bike",
"Tree",
"Fish",
"Moon",
"Book",
"Cake"
"Bird",
"Frog"
]

medium_hangman_word_list = [
"Elephant",
'Flower',
'Guitar',
'House',
'Island',
'Jungle',
'Kitten',
'Lemon',
'Monkey',
'Nest',
]

veteran_hangman_word_list = [
'Existential',
'Facetious',
'Heterogeneous',
'Juxtaposition',
'Kafkaesque',
'Metamorphosis',
'Neologism',
'Oligarchy',
'Paradox',
'Transcendental',
]

hangman_draw_speed = [
    inquirer.List(
        "draw_speed",
        message="Choose game difficulty (move with arrow keys)",
        choices=["Slow (7 Lives)","Fast (4 Lives)"]
    )
]

difficulty_setting_speed = inquirer.prompt(hangman_draw_speed).get("draw_speed").split()[0]

hangman_speed_setting_1 = [hangman_main_scene_1, hangman_main_scene_2, hangman_main_scene_3, hangman_main_scene_4, hangman_main_scene_5, hangman_main_scene_6, hangman_main_scene_7]

hangman_speed_setting_2 = [hangman_main_scene_1, hangman_main_scene_2, hangman_main_scene_5, hangman_main_scene_7]

hangman_word_difficulty = [
    inquirer.List(
        "word_difficulty",
        message="Choose word difficulty (move with arrow keys)",
        choices=["Easy","Medium","Veteran","Custom"]
    )
]

word_difficulty = inquirer.prompt(hangman_word_difficulty).get("word_difficulty")

def secret_word_letter_matcher(input_char: str) -> bool:
    pass

def play_game(difficulty_setting_speed_input: str, word_difficulty_input: str):
    hangman_game_scene_list = []
    if difficulty_setting_speed_input.lower() == "slow":
        hangman_game_scene_list = hangman_speed_setting_1
    elif difficulty_setting_speed_input.lower() == "fast":
        hangman_game_scene_list = hangman_speed_setting_2
    
    secret_word = ""

    if word_difficulty_input.lower() == "easy":
        secret_word = random.choice(easy_hangman_word_list)
    elif word_difficulty_input.lower() == "medium":
        secret_word = random.choice(medium_hangman_word_list)
    elif word_difficulty_input.lower() == "veteran":
        secret_word = random.choice(veteran_hangman_word_list)

    secret_word_blanks = "Secret Word: "

    for letter in secret_word:
        secret_word_blanks += "_ "

    print(secret_word_blanks)

    player_points = 0

    while True:
        guess_letter = input("Please type in a letter (type in \"esc\" to exit): ")
        if guess_letter.lower() == "esc":
            break

        # Secret word matcher -> Returns bool and prints the blank with filled and awards points
        # Secret word matcher function must first also consult a list and see what characters are already input, for a new game it should create a new list
        # Secret word matcher function must know what is the current state of the filled blanks and should disallow repeat characters
        # Print hangman -> accepts a bool and prints the next sequence from the current index

# random.choice(list_name)

play_game(difficulty_setting_speed, word_difficulty)