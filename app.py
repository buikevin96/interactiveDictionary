# Load Json Data
import json
from difflib import get_close_matches #library to compare text
data = json.load(open("data.json"))

def translate(w):
    w = w.lower() # Sets to lowercase
    if w in data:
        return data[w] # Return the definition of a word
    elif len(get_close_matches(w, data.keys())) > 0: # Word that match close
        return "Did you mean %s instead?" % get_close_matches(w, data.keys())[0]
    else:
        return "The word does not exist. Please double check it."

word = input("Enter Word: ")

print(translate(word))

