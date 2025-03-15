"""
Student information for this assignment:

On my/our honor,Palash Pawar, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: ppp625

"""

import random
import sys

# ANSI escape codes for text color
CORRECT_COLOR = "\033[3;1;102m"
WRONG_SPOT_COLOR = "\033[3;1;90;103m"
NOT_IN_WORD_COLOR = "\033[3;1m"
NO_COLOR = "\033[0m"

BOLD_COLOR = "\033[1m"

NUM_LETTERS = 5

INVALID_INPUT = "Bad input detected. Please try again."


class Keyboard:
    def __init__(self):
        self.rows = ("qwertyuiop", "asdfghjkl", "zxcvbnm")
        self.colors = {letter: NO_COLOR for letter in "qwertyuiopasdfghjklzxcvbnm"}

    def update(self, feedback_colors, guessed_word):
        for i, letter in enumerate(guessed_word):
            current_color = self.colors[letter]
            new_color = feedback_colors[i]
            
            if new_color == CORRECT_COLOR:
                self.colors[letter] = CORRECT_COLOR
            elif new_color == WRONG_SPOT_COLOR and current_color != CORRECT_COLOR:
                self.colors[letter] = WRONG_SPOT_COLOR
            elif new_color == NOT_IN_WORD_COLOR and current_color == NO_COLOR:
                self.colors[letter] = NOT_IN_WORD_COLOR

    def __str__(self):
        result = []
        result.append(" ".join(color_word(self.colors[letter], letter) 
                              for letter in self.rows[0]))
        result.append(" " + " ".join(color_word(self.colors[letter], letter) 
                                    for letter in self.rows[1]))
        result.append("   " + " ".join(color_word(self.colors[letter], letter) 
                                      for letter in self.rows[2]))
        return "\n".join(result)


class WordFamily:
    COLOR_DIFFICULTY = {CORRECT_COLOR: 0, WRONG_SPOT_COLOR: 1, NOT_IN_WORD_COLOR: 2}

    def __init__(self, feedback_colors, words):
        self.feedback_colors = feedback_colors
        self.words = words
        self.difficulty = sum(self.COLOR_DIFFICULTY[color] 
                            for color in feedback_colors)

    def __lt__(self, other):
        if not isinstance(other, WordFamily):
            raise NotImplementedError("< operator only valid for WordFamily comparisons.")
        
        # First tiebreaker: largest word family (opposite of normal sort)
        if len(self.words) != len(other.words):
            return len(self.words) > len(other.words)
        
        # Second tiebreaker: highest difficulty (opposite of normal sort)
        if self.difficulty != other.difficulty:
            return self.difficulty > other.difficulty
        
        # Third tiebreaker: lexicographical order (normal sort)
        return self.feedback_colors < other.feedback_colors

    def __str__(self):
        return (
            f"({len(self.words)}, {self.difficulty}, "
            f"{color_word(self.feedback_colors, ['░'] * 5)})"
        )

    def __repr__(self):
        return str(self)


def print_explanation(attempts):
    print("Welcome to Command Line Evil Wordle!")
    print()
    print("".join([BOLD_COLOR + letter + NO_COLOR for letter in "How To Play"]))
    print(f"Guess the secret word in {attempts} tries.")
    print("Each guess must be a valid 5-letter word.")
    print("The color of the letters will change to show")
    print("how close your guess was.")
    print()
    print("Examples:")
    print(CORRECT_COLOR + "w" + NO_COLOR, end="")
    print("".join([NOT_IN_WORD_COLOR + letter + NO_COLOR for letter in "eary"]))
    print(BOLD_COLOR + "w" + NO_COLOR, end=" ")
    print("is in the word and in the correct spot.")
    print(NOT_IN_WORD_COLOR + "p" + NO_COLOR, end="")
    print(WRONG_SPOT_COLOR + "i" + NO_COLOR, end="")
    print("".join([NOT_IN_WORD_COLOR + letter + NO_COLOR for letter in "lls"]))
    print(BOLD_COLOR + "i" + NO_COLOR, end=" ")
    print("is in the word but in the wrong spot.")
    print("".join([NOT_IN_WORD_COLOR + letter + NO_COLOR for letter in "vague"]))
    print(BOLD_COLOR + "u" + NO_COLOR, end=" ")
    print("is not in the word in any spot.")
    print()


def color_word(colors, word):
    if isinstance(colors, str):
        colors = [colors]
    assert len(colors) == len(word), "The length of colors and word do not match."
    colored_word = [f"{colors[i]}{char}{NO_COLOR}" 
                   for i, char in enumerate(word)]
    return "".join(colored_word)


def get_attempt_label(attempt_number):
    if 11 <= attempt_number <= 12:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(attempt_number % 10, "th")
    return f"{attempt_number}{suffix}"


def prepare_game():
    valid_words_file_name = "valid_guesses.txt"
    if len(sys.argv) > 3:
        raise ValueError()
    if sys.argv[-1] == "debug":
        valid_words_file_name = "test_guesses.txt"
        sys.argv.pop()
    if len(sys.argv) == 1:
        attempts = 6
    elif sys.argv[1].isnumeric():
        attempts = int(sys.argv[1])
        if not 1 < attempts < 100:
            raise ValueError()
    else:
        raise ValueError()
    with open(valid_words_file_name, "r", encoding="ascii") as valid_words:
        valid_words = [word.rstrip() for word in valid_words.readlines()]
    return attempts, valid_words


def fast_sort(lst):
    if len(lst) <= 1:
        return lst[:]
    
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    
    return fast_sort(left) + middle + fast_sort(right)


def get_feedback_colors(secret_word, guessed_word):
    feedback = [NOT_IN_WORD_COLOR] * NUM_LETTERS
    secret_count = {}
    
    # First pass: mark correct positions and count remaining letters
    for i in range(NUM_LETTERS):
        if guessed_word[i] == secret_word[i]:
            feedback[i] = CORRECT_COLOR
        else:
            secret_count[secret_word[i]] = secret_count.get(secret_word[i], 0) + 1
    
    # Second pass: mark wrong positions
    for i in range(NUM_LETTERS):
        if feedback[i] != CORRECT_COLOR:
            letter = guessed_word[i]
            if letter in secret_count and secret_count[letter] > 0:
                feedback[i] = WRONG_SPOT_COLOR
                secret_count[letter] -= 1
                
    return feedback


def get_feedback(remaining_secret_words, guessed_word):
    # Group words by feedback pattern
    feedback_groups = {}
    for secret_word in remaining_secret_words:
        colors = tuple(get_feedback_colors(secret_word, guessed_word))
        if colors not in feedback_groups:
            feedback_groups[colors] = []
        feedback_groups[colors].append(secret_word)
    
    # Create WordFamily objects
    families = [WordFamily(colors, words) 
                for colors, words in feedback_groups.items()]
    
    # Sort to get hardest family (first element after sorting)
    if not families:  # Handle empty case
        return [NOT_IN_WORD_COLOR] * NUM_LETTERS, remaining_secret_words
    sorted_families = fast_sort(families)
    
    # Return feedback colors and words from hardest family
    hardest_family = sorted_families[0]
    return list(hardest_family.feedback_colors), hardest_family.words


def main():
    try:
        valid = prepare_game()
    except ValueError:
        print(INVALID_INPUT)
        return

    attempts, valid_guesses = valid
    secret_words = valid_guesses

    print_explanation(attempts)

    keyboard = Keyboard()
    attempt = 1

    while attempt <= attempts:
        attempt_number_string = get_attempt_label(attempt)
        prompt = f"Enter your {attempt_number_string} guess: "
        guess = input(prompt)

        if not sys.stdin.isatty():
            print(guess)

        if guess not in valid_guesses:
            print(INVALID_INPUT)
            continue

        feedback_colors, secret_words = get_feedback(secret_words, guess)
        feedback = color_word(feedback_colors, guess)
        print(" " * (len(prompt) - 1), feedback)

        keyboard.update(feedback_colors, guess)
        print(keyboard)
        print()

        if len(secret_words) == 1 and guess == secret_words[0]:
            print("Congratulations! ", end="")
            print("You guessed the word '" + feedback + "' correctly.")
            break

        attempt += 1

    if attempt > attempts:
        random.seed(0)
        secret_words = fast_sort(secret_words)
        random.seed(0)
        secret_word = random.choice(secret_words)
        formatted_secret_word = "".join(
            [CORRECT_COLOR + c + NO_COLOR for c in secret_word]
        )
        print("Sorry, you've run out of attempts. The correct word was ", end="")
        print("'" + formatted_secret_word + "'.")


if __name__ == "__main__":
    main()