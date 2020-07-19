from typing import List
import collections
"""
Author: ztonege
https://leetcode.com/problems/search-suggestions-system/discuss/508775/Python-Trie-%2B-sort-Trie-%2B-Heap
Trie + Sort

Sort
n = number of characters in the products list
Time: O(nlog(n))

Build Trie
k = 3
m = number of characters in the longest product
Time: O(n)
Space: O(nkm)

Output Result
s = number of characters in searchword
Time: O(s)
Space: O(sk)

---
Test Cases:

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

s1=Solution()
s1.suggestedProducts(products,'m')
s1.suggestedProducts(products,'mo')
s1.suggestedProducts(products,'mou')
s1.suggestedProducts(products,'mous')

products = ["havana"]
searchWord = "havana"

s2=Solution()

s2.suggestedProducts(products,'h')
s2.suggestedProducts(products,'ha')
s2.suggestedProducts(products,'hav')
s2.suggestedProducts(products,'hava')
s2.suggestedProducts(products,'havan')
s2.suggestedProducts(products,'havana')


products = ["bags","baggage","banner","box","cloths"]
searchWord = "bags"

s3=Solution()
s3.suggestedProducts(products,'b')
s3.suggestedProducts(products,'ba')
s3.suggestedProducts(products,'bag')
s3.suggestedProducts(products,'bags')

products = ["havana"]
searchWord = "tatiana"
s4=Solution()
s4.suggestedProducts(products,'t')
s4.suggestedProducts(products,'ta')
s4.suggestedProducts(products,'tia')
s4.suggestedProducts(products,'tian')
s4.suggestedProducts(products,'tiana')
"""
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        Args:
        products: a list of product names
        searchWord: a string
        
        Returns:
        lists of the suggested products after each character of searchWord is typed. 
        """
        class TrieNode:
            def __init__(self):
                self.children = collections.defaultdict(TrieNode)
                self.suggestion = []
            
            def add_sugestion(self, product):
                # suggests at most three product names from products after each character of searchWord is typed
                if len(self.suggestion) < 3:
                    self.suggestion.append(product)
        
        #print("Original Products:",products)
        
        # O(nlog(n))
        products = sorted(products)
        #print("Sorted Products:",products)    

        # build a trie from the products list
        root = TrieNode()
        for p in products:
            node = root
            # for every character in the product
            for char in p:
                node = node.children[char]
                node.add_sugestion(p)
        
        result =[]
        node = root
        
        for char in searchWord:
            node = node.children[char]
            result.append(node.suggestion)
            
        return result
    
    
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

s1=Solution()
s1.suggestedProducts(products,'m')
s1.suggestedProducts(products,'mo')
s1.suggestedProducts(products,'mou')
s1.suggestedProducts(products,'mous')
