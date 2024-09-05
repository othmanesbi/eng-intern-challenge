import sys

# Braille dictionary
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    ',': '..0...', '.': '..OO.O', '?': '..O.OO', '!': '..OOO.', ':': '..OO..',
    ';': '..O.O.', '-': '....OO', '/': '.O..O.', '<': '.00..0',
    '(': 'O.O..O', ')': '.O.OO.', 
    ' ': '......'
}

# Reverse dictionary
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

# Braille numbers
braille_numbers_dict = {
    "1": "O.....",  # Same as 'A'
    "2": "O.O...",  # Same as 'B'
    "3": "OO....",  # Same as 'C'
    "4": "OO.O..",  # Same as 'D'
    "5": "O..O..",  # Same as 'E'
    "6": "OOO...",  # Same as 'F'
    "7": "OOOO..",  # Same as 'G'
    "8": "O.OO..",  # Same as 'H'
    "9": ".OO...",  # Same as 'I'
    "0": ".OOO.."   # Same as 'J'
}

reverse_braille_numbers_dict = {v: k for k, v in braille_numbers_dict.items()}

# Special Braille characters
braille_special_dict = {
    ".....O": "capital_follows",  
    "O.OOOO": "decimal_follows",  
    ".O.OOO": "number_follows"   
}



braille_pattern = {'OO', 'O.', '.O', '..'}
# Function to know if string is in Braille
def is_braille(string):
    return string[0:2] in braille_pattern




# Function to convert Braille char to English

def braille_to_english(string):
    result = ""
    i = 0
    num_follow = False
    while i < len(string):
        char = string[i:i+6]
        special = braille_special_dict.get(char)
        if special == None:
            if num_follow:
                EN_char = reverse_braille_numbers_dict.get(char)
                if EN_char:
                    result += EN_char
                else:
                    num_follow = False
            else:        
                result += reverse_braille_dict.get(char)
        elif special == "capital_follows":
            i = i + 6
            char = string[i:i+6]
            result += reverse_braille_dict.get(char).upper()
        elif special == "decimal_follows":
            num_follow = True
            i = i + 6
            char = string[i:i+6]
            result += '.' + reverse_braille_dict.get(char)
        elif special == "number_follows":
            num_follow = True
            i = i + 6
            char = string[i:i+6]
            result += reverse_braille_numbers_dict.get(char)
        i += 6
    return result


# Function to convert English char to Braille

def english_to_braille(string):
    num_follow = False
    result = ""
    for char in string:
        if char.isupper():
            num_follow = False
            result += ".....O"
            result += braille_dict.get(char.lower())
        elif char.isdigit():
            if not num_follow:
                num_follow = True
                result += ".O.OOO"
            result += braille_numbers_dict.get(char)
        else:
            num_follow = False
            result += braille_dict.get(char)
    return result

def printBrille(string):
    i = 0
    while i < len(string):
        print(string[i] + string[i+1], end="\n")
        i += 2

# If there are arguments, convert them to Braille
if len(sys.argv) > 1:
    i = 0
    for arg in sys.argv[1:]:
        i += 1
        if is_braille(arg):
            print(braille_to_english(arg), end="")
        else:
            print(english_to_braille(arg), end="") 
        if i < len(sys.argv[1:]):
            print("\n", end="")

        

