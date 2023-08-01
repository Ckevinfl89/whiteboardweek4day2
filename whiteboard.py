# You need to write a function, that returns the first non-repeated character in the given string.

# If all the characters are unique, return the first character of the string.
# If there is no unique character, return None.

# You can assume, that the input string has always non-zero length.

# Examples
# "test"   returns "e"
# "teeter" returns "r"
# "trend"  returns "t" (all the characters are unique)
# "aabbcc" returns None (all the characters are repeated)

def solution(name): 
    word={}
    for char in name:
        if char in word:
            word[char] += 1
        else:
            word[char] = 1
    for letter in name:
        if word[letter] == 1:
            return letter
    print(word)

def solution(string):
    empty_list = []
    running_count = 0
    for char in string:
        running_count = string.count(char)
        if running_count == 1:
            empty_list.append(char)
    print(empty_list)
    if empty_list:
        return empty_list[0]


def solution(sample):
    char_count = {}
    for letter in sample:
        char_count[letter] = char_count.get(letter, 0) + 1

    for letter in sample:
        if char_count[letter] == 1:
            return letter

    return None

def solution(word):
    pattern = re.compile('[a-z]')
    letter_list = pattern.findall(word.lower())
    for letter in letter_list:
        tot_insts = word.lower().count(letter)
        if tot_insts > 1:
            pass
        else:
            print(letter)
            return letter
    print(None)
    return None