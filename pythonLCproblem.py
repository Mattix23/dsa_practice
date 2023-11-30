class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

# Given two strings, ransomNote & magazine, we have to use the letters from 
# magazine to create ransomNote and return boolean True or False basedo 
# on the specific conditionals 


def can_Construct(): 
    string1 = "cat"
    string2 = "catpaw"
    expect = True


    assert can_Construct(string1) == expect 

#Step 3: 
// Create strings 
// indentify if string1 can be constucted from string2 
// create a test 
// return boolean results
    
#Step 4 : 

class Solution:
    def canConstruct(ransomNote: str, magazine: str) -> bool:
    # Create a dictionary to store the counts of each letter in the magazine
        magazine_counts = {}
    for letter in magazine:
        if letter not in magazine_counts:
            magazine_counts[letter] = 0
        magazine_counts[letter] += 1

    # Iterate through the ransom note and decrement the counts of corresponding letters in the magazine
    for letter in ransomNote:
        if letter not in magazine_counts or magazine_counts[letter] <= 0:
            return False
        magazine_counts[letter] -= 1

  
# thoughts on the problem 