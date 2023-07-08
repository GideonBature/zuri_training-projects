# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#def read_file_content(filename):
    # [assignment] Add your code here
#    with open("story.txt") as file:
#        print(file.read())
#read_file_content(filename)

#def count_words():
#    text = read_file_content("./story.txt")
    # [assignment] Add your code here

#    return {"as": 10, "would": 20}

from collections import Counter

def read_file_content(filename):
    # [assignment] Add your code here
    with open("story.txt") as file:
      listWords = file.read().split()
      return listWords

print(read_file_content("story.txt"))


def count_words(filename):
        text = read_file_content(filename)
     #[assignment] Add your code here
        return (Counter(text))
    
print("Number of Words in the file :", count_words("story.txt"))


#return {"as": 10, "would": 20}