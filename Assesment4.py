# Create a list of your 5 favorite movies.
movies = ["KGF","Avatar","Jurassic world","Intersteller","Tomorrow world"]
print(movies)

# Add a new movie to the list.
movies = ["KGF","Avatar","Jurassic world","Intersteller","Tomorrow world"]
movies.append("YJHD")
print(movies)
       
# Remove the first movie from the list.
movies = ["KGF","Avatar","Jurassic world","Intersteller","Tomorrow world"]
movies.pop(0)
print(movies)

# Sort a list of numbers in ascending order
list = [12,34,10,24,6,8]
list.sort()
print(list)

# Reverse a list.
movies = ["KGF","Avatar","Jurassic world","Intersteller","Tomorrow world"]
movies.reverse()
print(movies)

# Find the largest number in a list.
list = [12,34,10,24,6,8]
print(max(list))

# Merge two lists into one.
list1 = [12,34,10,24,6,8]
list2 = [3,33,23,56,48]
merge_list = list1+list2
print(merge_list)

# Access the last element of a list without using index number.
list = [12,34,10,24,6,8]
l = list.pop()
print(l)

# Create a nested list and access a specific inner element.
list=[[1,2,3],["KGF","Avatar","Jurassic world"],[True,False,]]
element=list[1][1]
print(element)

# Count how many times an element appears in a list.
list = [43,4,5,3,83,56,3,2,9,4]
element = 3
l=list.count(element)
print(l)

# Create a tuple with 5 numbers.
tuple = (2,3,4,18,15)
print(tuple)

# Access the third element in a tuple.    
tuple = (2,3,4,18,15)  
print(tuple[2])

# Unpack a tuple into separate variables.
tuple = (2,3,4,18,15)
a,b,c,d,e= tuple
print("a =",a)
print("b =",b)
print("c =",c)
print("d =",d)
print("e =",e)

# Create a set of 5 fruits.
fruit={"Apple","Banana","Mango","Cherry","Grapes"}
print(fruit)

# # Add a new fruit to the set.
fruit={"Apple","Banana","Mango","Cherry","Grapes"}
fruit.add("Pineapple")
print(fruit)

# # Remove an element from a set.
fruit={"Apple","Banana","Mango","Cherry","Grapes"}
fruit.remove("Banana")
print(fruit)

# Find union of two sets.
set1={"apple","banana","watermelon"}
set2={"grapes","watermelon","mango"}
set_union = set1.union(set2)
print(set_union)

# Find intersection of two sets.
set1={"apple","banana","watermelon"}
set2={"grapes","watermelon","mango"}
set3 = set1.intersection(set2)
print(set3)

# Check if one set is subset of another.
set1={"grapes","watermelon"}
set2={"grapes","watermelon","mango"}
set3 = set1.issubset(set2)
print(set3)

# Convert a list with duplicate values into a set to remove duplicates.
list= [2,3,4,4,5,6,6,6,7,7]
set=set(list)
print(set)

# Create a dictionary storing student names and marks.
student={"Het":32,"Jay":46,"krish":34}
print(student)

# Add a new key-value pair to an existing dictionary.
student={"Het":32,"Jay":46,"krish":34}
student["Harsh"]=52
print(student)

# Delete a key-value pair from a dictionary.
student={"Het":32,"Jay":46,"krish":34,"Harsh":54}
student.pop("Harsh")
print(student)

# Merge two dictionaries into one.
dic1 = {"Het":32,"Jay":46,"krish":34,}
dic2 = {"meet":32,"drish":46,"sanjay":34,}
merge_dic=dic1|dic2
print(merge_dic)

# Check if a key exists in a dictionary.
student={"Het":32,"Jay":46,"krish":34,"Harsh":54}
if "Het" in student:
    print("Key Exist")
else:
    print("Not Exist")

# Count word frequency in a given string using a dictionary.
text = ("Today is monday is")
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# Find the key with the maximum value in a dictionary.
dic1 = {"Het":32,"Jay":46,"krish":34,}
max_key= max(dic1, key=dic1.get)
print(max_key)

# Reverse keys and values in a dictionary.
dic1 = {"Het":32,"Jay":46,"krish":34,}
reversed_dict = {value: key for key, value in dic1.items()}
print(reversed_dict)

# Update the value for a specific key.
student={"Het":32,"Jay":46,"krish":34}
student["Jay"]=52
print(student)

# Convert a list of tuples into a dictionary.
student={("Het",32),("Jay",46),("krish",34)}
my_dic=dict(student)
print(my_dic)
