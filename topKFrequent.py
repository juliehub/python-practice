"""
Count the frequency of each word, then add it to heap that stores the best k candidates. 
Here, "best" is defined with our custom ordering relation, 
which puts the worst candidates at the top of the heap. 
At the end, we pop off the heap up to k times and reverse the result so that the best candidates are first.

Complexity Analysis:

Time Complexity: O(Nlogk), where NN is the length of words.
We count the frequency of each word in O(N) time, 
then we add NN words to the heap, each in O(logk) time. 
Finally, we pop from the heap up to kk times. 
As k≤N, this is O(Nlogk) in total.

In Python 3, we improve this to O(N+klogN). We use counter.most_common(k)
to return a list of the n most common elements and their counts from the most common to the least. 

Space Complexity: O(N), the space used to store our count.
"""
import re
from collections import Counter

def topKFrequent(k, keywords, reviews):
    '''
    k: int
    keywords: list of string
    reviews: list of string
    '''
        
    word_list = []
    
     # Store keywords in a set (make sure they are lowercase)
    kw = set([w.lower() for w in keywords]) 
        
    # Iterate through each review
    # Remove all special characters that are not letters or numbers, add to word_list
    # i.strip(string.punctuation).isalpha()
    # Use a set to make sure we count each word only once per review
    for review in reviews:
        word_list += set(review.lower().replace('[^a-z0-9]', '').split())
                       
    # Tally occurrences of words in a list
    count = Counter(word_list)
    result = Counter()
    
    # Iterate through each keyword in the counter
    for word in kw:
        result[word]=count[word]
        
    #print(count)
    #print(result)
    result = result.most_common(k)
    result_list=[]
    
    print(result)
    
    for item in result:
        result_list.append(item[0])
    
    return result_list

k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]

print("Top K Frequently Mentioned Keywords:",topKFrequent(k, keywords, reviews))


"""
Output:
["anacell", "betacellular"]

Explanation:
"anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.
"""

k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]

"""
Output:
["betacellular", "anacell"]

Explanation:
"betacellular" is occuring in 3 different reviews.
"anacell" and "deltacellular" are occuring in 2 reviews, 
but "anacell" is lexicographically smaller.

"""

print("Top K Frequently Mentioned Keywords:",topKFrequent(k, keywords, reviews))
