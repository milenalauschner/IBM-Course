'''
Write a function code to find total count of word little in the given string: "Mary had a little lamb Little lamb, 
little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, 
Mary went Everywhere that Mary went The lamb was sure to go"**
'''


string = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"
key = "little"

def freq (string, key):
    words = string.lower().replace(",", "").replace(".", "")split()
    Dict = {}

    print(words)
    for word in words:
        Dict[word] = freq_dict.get(word, 0) + 1
      # Dict[word] stores the updated count back into the dictionary using square brackets.
      #.get function os used to check if an especific attribute is exist in a dict
    
  
    print(f'Total count of the word {key} in the string is: {Dict[key]}')

    #return Dict #retrieves the total count for all words in the string
    return Dict[key] #retrieces the total count for a specific work in the string

freq(string, key)
