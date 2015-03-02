#LastName: McConnell
#FirstName: Brennan
#Email: brmc3887@colorado.edu
#Comments:

from __future__ import print_function
import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
  
    def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        #self.isRoot = False # is this a root node
        self.count = 0 # frequency count
        self.data = None
        self.next = {} # Dictionary mapping each character from a-z to the child node



    def addWord(self,w):
        wordLen = len(w)
        assert(wordLen > 0)

        for i in range(0,wordLen):
            if w[i] not in self.next:
                if i == (wordLen-1):
                    newNode = MyTrieNode(False)
                    newNode.isWordEnd = True
                    newNode.data = w
                    newNode.count += 1
                    self.next[w[i]] = newNode
                else:
                    newNode = MyTrieNode(False)
                    newNode.isWordEnd = False
                    self.next[w[i]] = newNode
                    self = self.next[w[i]]
            elif w[i] in self.next:
                self = self.next[w[i]]
                if i == (wordLen-1):
                    if self.isWordEnd == False:
                        self.data = w
                        self.count += 1
                        self.isWordEnd = True
                    else:
                        self.count += 1
        

    def lookupWord(self,w):
        wordLen = len(w)
        if wordLen == 0:
            return 0

        for i in range(0,wordLen):
            if w[i] not in self.next:
                return 0
            else:
                self = self.next[w[i]]
                if i == (wordLen-1):
                    if self.isWordEnd == True:
                        return self.count
                    else:
                        return 0


    def searchTree(self,arr):
        if self.isWordEnd == True:
            arr.append((self.data, self.count))

        for i in self.next:
            tmp = self
            self = self.next[i]
            self.searchTree(arr)
            self = tmp


    def autoComplete(self,w):
        ac_words = []
        wordLen = len(w)
        if wordLen == 0:
            return ac_words

        for i in range(0,wordLen):
            if w[i] not in self.next:
                return ac_words
            elif w[i] in self.next:
                self = self.next[w[i]]

        self.searchTree(ac_words)
        return ac_words
    
            

if (__name__ == '__main__'):
    t = MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']
    
    for w in lst1:
        t.addWord(w)

    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    print(j, j2 ,j3)

    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)
    
    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
     
