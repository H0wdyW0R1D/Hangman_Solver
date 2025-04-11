import pickle
# run this file to build the trie from a list of words

# get list of words from txt file
with open('english.txt', 'r') as file:
    english = file.readlines()
    english = [s.strip() for s in english]

# build trie (very fast)
class Node:
    def __init__(self,letter):
        self.c = letter
        self.isEndPoint = False
        self.children = []
    
    def __str__(self):
        return "letter: " + (self.c) + " is end?: " + str(self.isEndPoint) + " children: " + ("".join(str(element.c) for element in self.children))

def buildTrie(wordlist):
    foo = Node("") # root node
    for word in wordlist:
        # add word to trie
        current = foo # defines the node we are working with to add letters or explore to find lower nodes
        for letter in word:
            # for each letter in the word, determine if the child exists. If it does, set it to current, otherwise, create it
            doesChildExist = False
            for child in current.children:
                if (child.c == letter):
                    current = child
                    doesChildExist = True
                    break
            # if the child doesn't exist, create it and set current to it
            if (not doesChildExist):
                current.children.append(Node(letter))
                current = current.children[len(current.children)-1]
        # when the end of the word is reached, set the endPoint flag to true
        current.isEndPoint = True
    return foo

trie = buildTrie(english)

with open("trie.pkl", "wb") as file:
    pickle.dump(trie, file)