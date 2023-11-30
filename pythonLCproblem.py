# Step 1:
# Given two strings, ransomNote & magazine, we have to use the letters from 
# magazine to create ransomNote and return boolean True or False basedo 
# on the specific conditionals 

#Step 2:
# Examples would include if ransomNote was the string "cat" and magazine was "catpaw", this should return true because we have characters in magazine that will create ransomNote
# If ransomNote was "potato" and magazine was "catpaw" this would return false because we cannot create the string in ransomNote from magainze.

#Step 3: 
# Create strings 
# indentify if string1 can be constucted from string2 
# create a test 
# return boolean results
        
#Step 4 : 
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