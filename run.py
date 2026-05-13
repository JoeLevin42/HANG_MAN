"""
Hang man game
"""
import random

# --- Advanced 256-Color Codes ---
GOLD = '\033[38;5;220m'
YELLOW = '\033[38;5;226m'
ORANGE = '\033[38;5;208m'
WHITE = '\033[38;5;231m'
RED = '\033[38;5;196m'
GREY = '\033[38;5;245m'
CYAN = '\033[38;5;51m'
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

# --- How to use them in your game ---
# Just call print_victory() when the word is guessed correctly!
# Just call print_game_over() when the guesses reach 0!


def load_words():
    """
    This fucntion loads word list from words.txt with 200 words
    """
    with open("words.txt" ,"r",encoding ="UTF-8") as f:
        content = f.read()
        words_list = content.split(",")
    return words_list

def initilaze(word_list):
    choosen_word = random.choice(word_list)
    shown_var = len(choosen_word) * "_".split()
    guess_cnt = len(choosen_word) +1
    guess_history = []
    return {"choosen_word": choosen_word , "shown_var": shown_var , "guess_cnt" : guess_cnt , "guess_history" : guess_history}

def valid_input():
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
    dict with the letters in the key and the apeearnes index ad value
    """
    index_dict = {}
    for i , w in enumerate(word):
        if w not in index_dict:
            index_dict[w] = [i]
        else:
            index_dict[w].append(i)
    return index_dict

def update_shown_var(shown_var:str ,letter :str, index_dict : dict):
    index_list = index_dict.get(letter)
    for i in index_list:
        shown_var[i] = letter
    return shown_var
    
def printf(initial_stat_dict):
    print(f"Hisotry of your guesses{initial_stat_dict["guess_history"]}")
    print(f"Hello please guess the next letter")
    print(f"You have another {initial_stat_dict["guess_cnt"]} guesses")
    print("".join(initial_stat_dict["shown_var"]))

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
    while initial_dict["guess_cnt"] >0:
        printf(initial_dict)
        user_input = valid_input()
        if user_input not in choosen_word:
            initial_dict["guess_cnt"] -= 1
            initial_dict["guess_history"].append(user_input)
            continue
        else:
            update_shown_var(shown_var,user_input,index_dict)
            initial_dict["guess_history"].append(user_input)
            if check_victory(shown_var):
                print_victory()
                break
    if initial_dict["guess_cnt"] == 0:
        print(f"The word is : {initial_dict["choosen_word"]}")
        print_game_over()
        


if __name__ == "__main__":
    main()
        

