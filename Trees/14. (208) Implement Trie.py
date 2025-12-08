class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False 
""" we create a class for the trienode and use its properties 
1. the dictionary to store the character nodes and then 
2. marker for the end of the word
"""

class Trie:
    def __init__(self):
        # We create an empty TrieNode as the root for the Initialization 
        self.root = TrieNode()

    def insert(self , word:str ) -> None:
        # First we call the root and then we assign a pointer to the root for the traversal purpose
        curr = self.root
        for c in word:
            if c not in curr.children:
                # If we find that the character is missing in the word , 
                # then we create an empty trieNode and add that char to the children prop of the prev root 
                curr.children[c] = TrieNode()
            # else we shift the curr pointer to the TrieNode of the child
            curr = curr.children[c]
        # for eg we have a word 'TREE' then we mark the last character 'E' property endofword = True
        curr.endofWord = True 

    def startsWith(self , prefix: str ) -> bool:
        curr = self.root 
        for c in prefix:
            if c not in curr.children:
                return False 
            curr = curr.children[c]
        return True
        
    def search(self , word: str ) -> bool:
        curr = self.root 
        for c in word:
            if c not in curr.children:
                return False 
            curr = curr.children[c]
        return curr.endofWord 
        
# Time Complexity - O(H) where H is the height of the trie
# Space Complexity - O(T) where T is the no of nodes in the trie
        
        
    
