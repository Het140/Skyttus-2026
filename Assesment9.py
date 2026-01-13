# Write a program to read a file and display its contents.
# file = open("sample.txt","r")
# content = file.read()
# print(content)
# file.close()

# Write a program to count the number of lines in a file.
# with open("sample.txt", "r") as file:
#     print("Number of lines:", len(file.readlines()))

# Write a program to count how many times each word appears in a file.
# file = open("sample.txt","r")
# text = file.read()
# file.close()
# word = text.split()
# count = {}

# for word in word:
#     if word in count:
#         count[word] += 1
#     else:
#         count[word] = 1
#         for word in count:
#             print(word,":",count[word])
            
# Write a program to write 5 user-entered sentences to a file.
# with open("sample.txt", "a") as file:
#     for i in range(5):
#         sentence = input(f"Enter sentence {i+1}:")
#         file.write(sentence + "\n")
        
# Write a program to append a list of strings to an existing file.
# string_append = ["Python\n","File Handling\n","Append Mode\n"]
# with open("sample.txt", "a") as file:
#     for line in string_append:
#      file.write(line)

# Write a program to read a file and print only lines containing a specific word.
# file = open("sample.txt","r")
# word = input("Enter word to search:")
# for line in file:
#     if word in line:
#         print(line.strip())
      
# Write a program to replace a specific word in a file and save changes.
# file = open("sample.txt","r")
# content = file.read()
# file.close()
# old_word = input("Enter word to replace:")
# new_word = input("Enter new word:")
# content = content.replace(old_word,new_word)
# file = open("sample.txt","w")
# file.write(content)
# file.close()

# Write a program to merge the contents of two text files into a third file.
# file1 = open("sample.txt","r")
# file2 = open("sample1.txt","r")
# file3 = open("Mergesample.txt","w")
# file3.write(file1.read())
# file3.write(file2.read())
# file1.close()
# file2.close()
# file3.close()

# Write a program to read a CSV file and display its content in a formatted way.
# import csv
# with open("sample.csv","r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print("|".join(row))
        
# Write a program to back up a file by copying its contents into another file.	
source = open("sample.txt","r")
backup = open("sample1.txt","w")
backup.write(source.read())
source.close()
backup.close()
print("File Backup Created successfully")