# Take a string input and print its length.
string = ("Today is Monday")
print("Length of string:",len(string))

# Convert a sentence into lowercase.
sentence = ("TODAY IS MONDAY.")
print(sentence.lower())

# Replace space with underscore in a string.
string = ("Today is Monday.")
print(string.replace(" ","_"))

# Extract the first and last character of a string.
text = ("Today is Monday")
print("First Character:", text[0])
print("Last Character:",text[-1])

# Reverse a string using slicing.
string = ("Het")
print(string[-1:-4:-1])

# Count how many times a letter appears in a string.
text = ("Today is Monday")
count = input("Enter a letter: ")
print("Letter Count",text.count(count))

# Check if a word is present in a sentence.
sentence = ("Today is Monday")
word = input("Enter the word to find:")
if word in sentence:
    print("Word is present")
else:
    print("Word is not present")
    
# Take name & age and print using f-string formatting.
name = ("Het")
age = ("21")
print(f"My name is {name} and my age is {age}")   

# Remove extra spaces from the start and end of a string.
text = ("Today is Monday")
print(text.replace(" ",""))
 
# Join a list of words into a single string with - between them.
text = ("Today is Monday")
print(text.replace(" ","-"))


