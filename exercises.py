'''
Write a function code to find total count of word little in the given string: "Mary had a little lamb Little lamb, 
little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, 
Mary went Everywhere that Mary went The lamb was sure to go"**
'''


string = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"
key = "little"

def word_count (string, key):
    words = string.lower().replace(",", "").replace(".", "")split()
    Dict = {}

    print(words)
    for word in words:
        Dict[word] = freq_dict.get(word, 0) + 1
      # Dict[word] stores the updated count back into the dictionary using square brackets.
      #.get function os used to check if an specific attribute exists in a dictionary.
    
  
    print(f'Total count of the word {key} in the string is: {Dict[key]}')

    #return Dict #retrieves the total count for all words in the string
    return Dict[key] #retrieves the total count for a specific word in the string

word_count (string, key)
