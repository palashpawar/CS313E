

"""
Student information for this assignment:

On my/our honor, Palash, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: ppp625
"""

STEP_SIZE_CONSTANT = 3

def is_prime(n):
    if n == 1:
        return False
    limit = int(n**0.5) + 1
    div = 2
    while div < limit:
        if n % div == 0:
            return False
        div += 1
    return True

def hash_word(s, size):
    hash_idx = 0
    for c in s:
        letter = ord(c) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

def step_size(s):
    return STEP_SIZE_CONSTANT - (hash_word(s, STEP_SIZE_CONSTANT) % STEP_SIZE_CONSTANT)

def insert_word(s, hash_table):
    size = len(hash_table)
    idx = hash_word(s, size)
    step = step_size(s)
    while hash_table[idx] != "":
        if hash_table[idx] == s:
            return
        idx = (idx + step) % size
    hash_table[idx] = s

def find_word(s, hash_table):
    size = len(hash_table)
    idx = hash_word(s, size)
    step = step_size(s)
    while hash_table[idx] != "":
        if hash_table[idx] == s:
            return True
        idx = (idx + step) % size
    return False

def is_reducible(s, hash_table, hash_memo):
    if s in ["a", "i", "o"]:
        return True
    if find_word(s, hash_memo):
        return True
    for i in range(len(s)):
        sub_word = s[:i] + s[i+1:]
        if find_word(sub_word, hash_table):
            if is_reducible(sub_word, hash_table, hash_memo):
                insert_word(s, hash_memo)
                return True
    return False

def get_longest_words(string_list):
    if not string_list:
        return []
    max_len = max(len(word) for word in string_list)
    return [word for word in string_list if len(word) == max_len]

def main():
    word_list = []
    try:
        while True:
            word = input().strip()
            if word:
                word_list.append(word)
    except EOFError:
        pass

    n = len(word_list)
    size = 2 * n
    while not is_prime(size):
        size += 1
    hash_table = [""] * size
    for word in word_list:
        insert_word(word, hash_table)

    m = int(0.2 * n)
    while not is_prime(m):
        m += 1
    hash_memo = [""] * m

    reducible_words = []
    for word in word_list:
        if is_reducible(word, hash_table, hash_memo):
            reducible_words.append(word)

    longest = sorted(get_longest_words(reducible_words))
    for word in longest:
        print(word)

if __name__ == "__main__":
    main()
