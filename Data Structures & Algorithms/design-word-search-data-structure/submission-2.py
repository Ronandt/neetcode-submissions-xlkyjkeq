class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for x in word:
            if x not in current.children:
                current.children[x] = TrieNode()
            current = current.children[x]
        current.endOfWord = True

            

    def search(self, word: str) -> bool:
        current = self.root
        return self.searchRec(word, current)
    
    def searchRec(self, word, current):
        if(len(word) == 0): #can be . or any 
            return  current.endOfWord

        if word[0] == ".":
            
            for x,y in current.children.items():

                if(self.searchRec(word[1:], y)):
                    return True


        if word[0] not in current.children and word[0] != ".":
            return False
        if word[0] in current.children and word[0] !=".":
            return self.searchRec(word[1: ], current.children[word[0]])
        #condition to continue if exists
        return False
            
        
