import numpy as np      # number stuffs
import copy             # deep copy objects
import pickle           # decode the trie into an object
from trie import Node   # pickle needs this class to understand how to decode the trie

# Load the trie from the trie file
with open("trie.pkl", "rb") as file:
    trie = pickle.load(file)
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
possibleWords = getPossibleWords("____e","aoi",trie)
print(possibleWords)