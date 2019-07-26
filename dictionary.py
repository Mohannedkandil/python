import json 
from difflib import get_close_matches
data = json.load(open("data.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        ch = input("Did you mean %s instead? Enter Y or N: "% get_close_matches(w,data.keys())[0])
        ch = ch.lower()
        if ch == 'Y' or 'y':
            return data[get_close_matches(w,data.keys())[0]]
        else:
            return "Please check the word you want"
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
out = translate(word) #output
if type(out) == list:
    for item in out:
        print(item)
    else:
        print(out)