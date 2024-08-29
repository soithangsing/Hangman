import inquirer

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

expert_hangman_word_list = [
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
        choices=["Slow (Easy)","Fast (Hard)"]
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


def play_game(difficulty_setting_speed_input: str, word_difficulty_input: str):
    pass

# random.choice(list_name)

print(word_difficulty)