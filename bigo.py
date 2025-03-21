"""
Student information for this assignment:

On my honor, Palash Pawar, this 
programming assignment is my own work and I have not provided this code to 
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: ppp625

"""


def length_of_longest_substring_n3(s):
    """
    Finds the length of the longest substring without repeating characters
    using a brute force approach (O(N^3)).

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """
    n = len(s)
    max_length = 0
    
    for i in range(n):
        for j in range(i, n):
            seen = set()
            valid = True
            
            for k in range(i, j + 1):
                if s[k] in seen:
                    valid = False
                    break
                seen.add(s[k])
            
            if valid:
                max_length = max(max_length, j - i + 1)
    
    return max_length

    pass


def length_of_longest_substring_n2(s):
    """
    Finds the length of the longest substring without repeating characters
    using a frequency list approach (O(N^2)), converting each character to
    their corresponding numeric representation in ASCII as the index into the
    frequency list.

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """
    n = len(s)
    max_length = 0
    
    for i in range(n):
        seen = set()
        
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_length = max(max_length, j - i + 1)
    
    return max_length
    pass


def length_of_longest_substring_n(s):
    """
    Finds the length of the longest substring without repeating characters
    using a frequency list approach (O(N)), converting each character to
    their corresponding numeric representation in ASCII as the index into the
    frequency list. However, this approach stops early, breaking out of the inner
    loop when a repeating character is found. You may also choose to challenge
    yourself by implementing a sliding window approach.

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """
    n = len(s)
    max_length = 0
    seen = set()
    left = 0
    
    for right in range(n):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length
    pass
