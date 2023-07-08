# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


#def find_anagrams(word):
    # [assignment] Add your code here

 #   return True

word1 = input("Enter First Word :")
word2 = input("Enter Second Word :")

def find_anagrams(word1, word2):
    # [assignment] Add your code here
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False

check = find_anagrams(word1, word2)
if check == True:
    print("The Two Words are Anagrams")
else:
    print("The Two Words are Not Anagrams")