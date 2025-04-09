import numpy as np
import copy

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
# print(len(trie.children))
# print(trie.children[1].children[0].isEndPoint)
def exploreTrie(knownLetters,exclude,current,built):
    # define what this call represents so far and see if it can be returned
    built = built + current.c

    # define depth to be the length of built
    depth = len(built)
    
    # if this is the deepest we can explore, return the word if it is an endpoint or nothing if not
    if (depth == len(knownLetters)):
        if (current.isEndPoint):
            return [built]
        return []

    # if this line is made, it means we must explore new children for new potential words and pass it on
    foo = [] # we can store them here
    # for each child, see if it is valid for exploration; if so, do
    for child in current.children:
        letter = knownLetters[depth]
        # if the space is unkown, assume it works
        # otherwise, only permit it if it matches the letter
        if ((letter == "_" and not child.c in exclude) or letter == child.c):
            # explore the child's children nodes
            foo = foo + exploreTrie(knownLetters,exclude,child,copy.deepcopy(built))
    # return words added
    return foo
    
def getPossibleWords(knownLetters, exclude, trie):
    # explore trie for word that meet the correct criteria
    return exploreTrie(knownLetters,exclude,trie,"")
# possibleWords = getPossibleWords("a_t","p",trie)
# print(possibleWords)