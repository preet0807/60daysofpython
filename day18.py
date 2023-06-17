# # def minion_game(string):
# #     #s split
# #     #s starts with 
# def is_consonant(string1):
#     consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
#     return string1 in consonants

# def is_vowel(string1):
#     vowels = 'aeiouAEIOU'
#     return string1 in vowels
# if __name__ == '__main__':
# #     s = input()
# #     minion_game(s)
#     string = input()
#     substrings = []
#     n = len(string)
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             substrings.append(string[i:j])
#     stuart=0
#     kevin=0
#     for words in substrings:
#         string1= words[0:1]
        
#         if is_consonant(string1):
#             stuart=stuart+1
#         elif is_vowel(string1):
#             kevin=kevin+1
#     if stuart>kevin:
#         print("Stuart", +stuart)
#     else:
#         print("Kevin",+kevin)


def is_consonant(string1):
        consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        return string1 in consonants
    
def is_vowel(string1):
        vowels = 'aeiouAEIOU'
        return string1 in vowels
def minion_game(string):
    substrings = []
    n = len(string)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(string[i:j])
    stuart=0
    kevin=0
    for words in substrings:
        string1= words[0:1]
        
        if is_consonant(string1):
            stuart=stuart+1
        elif is_vowel(string1):
            kevin=kevin+1
    if stuart>kevin:
        print("Stuart", +stuart)
    else:
        print("Kevin",+kevin)
    return
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)



