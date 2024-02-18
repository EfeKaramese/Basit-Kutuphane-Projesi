#!/usr/bin/env python
# coding: utf-8

# In[1]:



class Library:
    def __init__(self,file_name,mode):
        self.file_name=file_name
        self.mode=mode
        self.file=open(self.file_name,self.mode)
        self.file.seek(0)
    def __del__(self):
        self.file.close()
    def list_books(self):
        self.file.seek(0)
        for i in self.file:
            j=i.split(",")
            print(f"Book: {j[0]}, Author: {j[1]}")
    def add_book(self,title,author,release_date,pages):
        self.file.seek(0)
        self.file.write(f"{title},{author},{release_date},{pages}\n")
    def remove_book(self,book):
        lines = self.file.readlines()
        self.file.close()
        with open(self.file_name, "w") as new_file:
            for line in lines:
                if book not in line:
                    new_file.write(line)
        self.file = open(self.file_name, "a+")
        self.file.seek(0)

while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")
    choice=input("Enter your choice (1-4):")
    lib=Library("books.txt","a+")
    if choice=="1":
        lib.list_books()
    if choice=="2":
        title=input("Enter the book name: ")
        author=input("Enter the author: ")
        date=input("Enter the release date: ")
        pages=input("Enter the number of pages: ")
        lib.add_book(title,author,date,pages)
    if choice=="3":
        delete_book=input("Name of the deleted book: ")
        lib.remove_book(delete_book)
    if choice=="q":
        break
        


# In[ ]:




