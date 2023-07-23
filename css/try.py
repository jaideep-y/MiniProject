# lis= ["apple", "banana", "cat", "dog","dear", "elephant", "frog", "grape"]
# jai={}
# for word in lis:
#     fchar=word[0]
#     if fchar in jai:
#         jai[fchar].append(word)
#     else:
#         jai[fchar]=[word]
# print(jai)

# data = [[3, 9], [2, 5], [1, 7], [4, 2], [5, 4]]
# sortedlist=sorted(data,key=lambda x:x[1])
# print(sortedlist)

# deep = {'a': 1, 'b': 2, 'c': 3}
# jai={}
# jai.update(deep)
# print(jai)


# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# jai={**dict1,**dict2}
# print(jai)

# with open("try.txt","r") as file:
#     count=0
#     for line in file:
#         count+=1
# print(count)

# with open("try.txt","r") as file:
#     vc=0
#     cc=0
#     content=file.read()
#     content=content.lower()
#     v=["a","e","i","o","u"]
#     for char in content:
#         if char.isalpha():
#             if char in v:
#                 vc+=1
#             else:
#                 cc+=1
# print("vowels",vc)
# print("consonants",cc)
# jai=input("enter the word you want to search:")
# with open("try.txt","r") as file:
#     con=file.read()
#     if jai in con:
#         print(con.index(jai))
#     else:
#         print("not found")

# def sum(a,b):
#     print(a+b)
# sum(1,2)


# def avg(num):
#     s=sum(num)
#     a=len(num)
#     if a>0:
#         print("avg",s/a)
#     else:
#         print("0")
# avg([1,2,3,4,5])


# class Student:
#     def __init__(self):
#         self.name=""
#         self.usn=""

#     def details(self):
#         self.name=input("enter name")
#         self.usn=input("enter usn")

#     def display(self):
#         print(self.name)
#         print(self.usn)

# jai=Student()
# jai.details()
# jai.display()

#...................................................

# class Cal:
#     def add(self,a,b):
#         print(a+b)

#     def add(self,a,b,c):
#         print(a+b+c)
# jai=Cal()
# jai.add(1,2,3)
# jai.add(1,2,3,4)

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         print("woof")

# class Cat(Animal):
#     def sound(self):
#         print("meow")

# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# animals = [dog, cat]
# for animal in animals:
#     print(animal.name)
#     animal.sound()















































































