import re
print("Starting Python Basics...")

# not requirement define the variable with datatype
# C / C++ / Java int var = 10
x = 10
y = 20.5
z = "Hello, World!"
bool_var = True
z = 'Python is a versatile language'
print(x ,"is a ", type(x))
print(y ,"is a ", type(y))
print(z ,"is a ", type(z))
print(bool_var ,"is a ", type(bool_var))
print(z, "is a ", type(z))

# list, set, tuple, dictionary
my_list = ['A825662','Giri Prasad P', 10, 20.5, True]
print("List:", my_list)
# indexd, mutable, ordered
my_list[1] = 'Giri'
my_list.append('Python Developer')
my_list.insert(2,'giri-prasad.p@ato.net')
print("Updated List:", my_list)

# Tuple
my_tuple = ('A825662', 'Giri Prasad P', 10, 20.5, True)
# indexd, immutable, ordered
print("Tuple:", my_tuple)
print("Name is ", my_tuple[1])
print("Type of my_tuple:", type(my_tuple))
# my_tuple[1] = 'Giri' # TypeError: 'tuple' object does not support item assignment

templist = list(my_tuple)
templist[1] = 'Giri'
templist.append('Python Developer')
templist.append(30)
templist.insert(2, 'giri-prasad.p@ato.net')
my_tuple = tuple(templist)
print("Updated Tuple:", my_tuple)

t1 = ('A825662', 'A825663', 'A825664',
      'A825665', 'A825666', 'A825667')
t2 = ('A825668', 'A825669', 'A825670')
newtuple = t1 + t2 # concatenation #('A825662', 'A825663', 'A825664', 'A825665', 'A825666', 'A825667')
print("New Tuple after concatenation:", newtuple)

set1 = {1,2,2,1,2,1,2,53435,4,64,65,76,8,7,7,98,9,989,8}
# unique, unordered, mutable
print("Set:", set1)


l1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]

l2 = [[1,1,1]]

l3 = l1 + l2

print("List 1:", l1)
print("List 2:", l2)
print("List 3:", l3)

t1 = ((1,2,3),
      (4,5,6),
        (7,8,9))    
t2 = ((1,1,1))



t3 = t1 + t2
print("Tuple 1:", t1)
print("Tuple 2:", t2)
print("Tuple 3:", t3)

Tuple_Sample = ((1,2,3),
                (4,5,6),
                (7,8,9))
print("Tuple Sample:", Tuple_Sample)

T4 = (0,1,0)
T5 = Tuple_Sample + T4
print("Tuple 5:", T5)


t1 = (1,2,3,5,3,2,0,1,2)
print("Tuple 1:", t1)

s2 = set(t1)
print("Set from Tuple:", s2)
t1 = tuple(s2)
print("Tuple from Set:", t1)

data = [('e1', 'emaild1@atos.net','EmplName1',),
        ( 'EmplName2','emailid2@atos.net', 'e2'),
        ('e3', 'EmplName3','emailid3@atos.net'),
        ('e4', 'EmplName4','emailid4@atos.net'),
        ('e5', 'EmplName5','emailid5@atos.net'),
        ('e6', 'EmplName6','emailid6@atos.net'),
        ('e7', 'EmplName7','emailid7@atos.net'),
        ('e8', 'EmplName8','emailid8@atos.net'),
        ('e9', 'EmplName9','emailid9@atos.net'),
        ('e10', 'EmplName10','emailid10@atos.net')]


emails =  [val for tup in data for val in tup if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', val)]
print("Extracted Emails:", emails)

s1 = {'Giri','Prasad','Prabhu','Piyush','Peter'}
print("Set 1:", s1)

s2 = {'Giri','Gauri','Piyush','Latheef','Rose','Prabhu'}
print("Set 2:", s2)

# concatenate -> union 
s3 = s1.union(s2)
print("Union of Set 1 and Set 2:", s3)

s3 = s1 & s2  # intersection s1 | s2
print("Intersection of Set 1 and Set 2:", s3)   

s3 = s1.intersection(s2)  # intersection
print("Intersection of Set 1 and Set 2 using intersection method:", s3)

s3 = s2 - s1  # difference
print("Difference of Set 1 and Set 2:", s3)

# Dictionary
# Key Value Pair
dict1 = {
    'das_id' : 'A825662',
    'name' : 'Giri Prasad P',
    'email' : 'giri.prasad.p@atos.net',
    'age' : 30
}

print("Dictionary:", dict1)
print("Dictionary Keys:", dict1.keys())
print("Dictionary Values:", dict1.values())
print("Name from Dictionary:", dict1['name'])
dict1['age'] = 31  # update age
print("The name of the trainer is ", dict1['name'],
      "and he is not "  + str(dict1['age']) + ' years old.')
# change the name, ordered, mutable

dict2 = {
    'das_id' : 'A825663',
    'name' : 'Guru Prasad P',
    'email' : 'guru.prasad.p@atos.net',
    'age' : 30
}

print("Dictionary 2:", dict2, "Type:", type(dict2))

if (dict1['age'] > dict2['age']):
    print("Trainer 1 is older than Trainer 2")

# key and value -> type of each value
for key, value in dict1.items():
    print(f"Key: {key}, Value: {value}, Type: {type(value)}")


#  Conditional Statements - if elif else, match case
ip1 = int(input("Enter a number: "))
# str
# convert to int
# ip1 = int(ip1)
ip2 = int(input("Enter score for sub1 number: "))
if ip1 > ip2:
    print(f"{ip1} is greater than {ip2}")
else: 
    print(f"ip2 : {ip2} is greater than ip1 {ip1}")


s1 = float(input("S1 marks: "))
s2 = float(input("S2 marks: "))
s3 = float(input("S3 marks: "))
avg = (s1 + s2 + s3) / 3
# Grade 
if avg == 100:
    print("Grade: A+")
elif avg >= 90:
    print("Grade: A")
elif avg >= 80:
    print("Grade: B")
elif avg >= 70:
    print("Grade: C")
elif avg >= 60:
    print("Grade: D")
elif avg >= 50:
    print("Grade: E")
else:
    print("Grade: F")


# Match Case - Switch Case

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
inputvalue = input("Enter your choice (1-3): 1. Add, 2. Subtract, 3. Multiply): ")
match inputvalue:
    case '1':
        result = x + y
        print(f"The result of addition is: {result}")
        print("You chose Addition")
    case '2':
        result = x - y
        print(f"The result of subtraction is: {result}")
        print("You chose Subtraction")
    case '3':
        result = x * y
        print(f"The result of multiplication is: {result}")
        print("You chose Multiplication")
    case _:
        print("Invalid choice")


# Loops - for, while
# For Loop
for i in range(1, 11):
    print(f"Square of {i} is {i**2}")

l1 = [11,22,33,44,55]
for i in l1:
    print(f"Square of {i} is {i**2}")

count = 0
while count <= 9:
    count += 1
    if(count == 5):
        continue
    if(count == 8):
        break
    print(f"{count}. Giri Prasad P")

# create function   def function_name(): 
