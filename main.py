# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = word.strip()
    anagram = anagram.strip()

    if sorted(word) == sorted(anagram):
        check = True
    else:
        check = False

    return print(check)

find_anagram("hello", "check")
find_anagram("elbow", "below")
find_anagram("semi", "mice")
find_anagram("listen", "silent")