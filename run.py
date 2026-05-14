#https://github.com/yoelo0505-wq/HANG_MAN.git

import random

#Advanced 256-Color Codes ---
GOLD = '\033[38;5;220m'
YELLOW = '\033[38;5;226m'
ORANGE = '\033[38;5;208m'
WHITE = '\033[38;5;231m'
RED = '\033[38;5;196m'
GREY = '\033[38;5;245m'
CYAN = '\033[3`8;5;51m'
RESET = '\033[0m'

def print_victory():
    """Prints a colorful golden trophy when the user wins."""
    print(f"""
{YELLOW}       ___________
{GOLD}      '._==_==_=_.'
{ORANGE}      .-\\:      /-.
{YELLOW}     | (|:.     |) |
{GOLD}      '-|:.     |-'
{ORANGE}        \\::.    /
{YELLOW}         '::. .'
{GOLD}           ) (
{GREY}         _.' '._
{GREY}        `"""""""`
  🎉 YOU ARE THE CHAMPION! 🎉
""")

def print_game_over():
    """Prints a terrifying pirate skull when the user loses."""
    print(f"""
{WHITE}         ______
{WHITE}      .-"      "-.
{WHITE}     /            \\
{WHITE}    |              |
{WHITE}    |,  {RED}.-.{WHITE}  {RED}.-.{WHITE}  ,|
{WHITE}    | )({RED}__/{WHITE}  {RED}\\__{WHITE})( |
{WHITE}    |/     /\\     \\|
{WHITE}    (_     ^^     _)
{GREY}     \\__|IIIIII|__/
{GREY}      | \\IIIIII/ |
{WHITE}      \\          /
{WHITE}       `--------`
{RED}  💀 GAME OVER, MATEY! 💀{RESET}
""")



def load_words():
    """
    This fucntion loads word list from words.txt with 200 words
    """
    try:
        with open("words.txt" ,"r",encoding ="UTF-8") as f:
            content = f.read()
            words_list = content.split(",")
        return words_list
    except:
        return [ "apple", "banana", "orange", "grape", "melon",
    "water", "house", "table", "chair", "window",
    "school", "teacher", "student", "pencil", "paper",]

def initilaze(word_list):
    """Inilazing the game varibles

    This function is basically inilazing all the vars like choosen word from random choice
    taken from local data base of words , creating the shown var to the user, creating the guess counter
    and initiate empty list for the guesses history

    Args:
    word_list: file with 200 different words 

    Returns:
    dict of all the values the key is string of the varibles names
    """
    choosen_word = random.choice(word_list)
    shown_var = len(choosen_word) * " _ ".split()
    guess_cnt = len(choosen_word) +1
    guess_history = set()
    return {"choosen_word": choosen_word , "shown_var": shown_var , "guess_cnt" : guess_cnt , "guess_history" : guess_history}

def valid_input():
        """Checking the input if its valid

        This fuction checking the input if its alpha and if the lenght of the 
        input is not big then 1

        Returns:
        the valid user input if not its in while true
        """
        while True:
            user_input = input("Please enter your guess: ")
            if user_input.isalpha() and len(user_input) == 1:
                return user_input.lower()
            
        
def analyze_word_index(word):
    """Analyzing the word and index

    This fucntion taked the choosen word and making dict that every letter is  the key
    and the appearnes index is the value

    Args:
    word: the choosen word from random.choice

    Returns:
    dict with the letters in the key and the apeearnes index and value list
    """
    index_dict = {}
    for i , w in enumerate(word):
        if w not in index_dict:
            index_dict[w] = [i]
        else:
            index_dict[w].append(i)
    return index_dict

def update_shown_var(shown_var:str ,letter :str, index_dict : dict):
    """Updating the shown var for the user

    This function is basically taking the letter indexes and replacing the shown var "-"
    whith the real letter of the words one or more

    Args:
    shown_var : the shown var to the user
    letter: this is the user input
    index_dict : the index dict of the word every letter is key and indexex is value

    Returns:
    shown_var : return the sown var to the user
    letter : 
    """
    index_list = index_dict.get(letter)
    for i in index_list:
        shown_var[i] = letter
    return shown_var
    
def printf(initial_stat_dict):
    print(f"Hisotry of your guesses{initial_stat_dict["guess_history"]}")
    print(f"Hello please guess the next letter")
    print(f"You have another {initial_stat_dict["guess_cnt"]} guesses")
    print(" ".join(initial_stat_dict["shown_var"]))

def check_victory(shown_var):
    if "_" not in shown_var:
        print("You win")
        return True 
    return False

def main():
    word_list = load_words()
    initial_dict = initilaze(word_list)
    shown_var = initial_dict["shown_var"]
    choosen_word = initial_dict["choosen_word"]
    index_dict = analyze_word_index(choosen_word)
    while initial_dict["guess_cnt"] > 0:
        printf(initial_dict)
        user_input = valid_input()
        if user_input not in choosen_word:
            if user_input in initial_dict["guess_history"]:
                continue
            initial_dict["guess_cnt"] -= 1
            initial_dict["guess_history"].add(user_input)
            continue
        else:
            update_shown_var(shown_var,user_input,index_dict)
            initial_dict["guess_history"].add(user_input)
            if check_victory(shown_var): 
                print_victory()
                break
    if initial_dict["guess_cnt"] == 0:
        print(f"The word is : {initial_dict["choosen_word"]}")
        print_game_over()
        


if __name__ == "__main__":
    main()
    
