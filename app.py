# Load Json Data
import json
data = json.load(open("data.json"))

def translate(w):
    w = w.lower() # Sets to lowercase
    if w in data:
        return data[w] # Return the definition of a word
    else:
        return "The word does not exist. Please double check it."

word = input("Enter Word: ")

print(translate(word))