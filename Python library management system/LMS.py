import datetime
import os
class LMS:
    def __init__(self,List_of_books,library_name):
        self.List_of_books= "list_of_books.txt"
        self.library_name= library_name
        self.books_dict={}
        id=101
        with open(self.List_of_books) as bk:
            content=bk.readlines()
        for line in content:
            self.books_dict.update({str(id):{"books_title":line.replace("\n",""),
            "lender_name": "","issue_data":"","status":"Available"}})
            id=id+1

    def display_books(self):
        print("---------list of books--------")
        print("Books id","\t","Title")
        print("-------------------------------")
        for key,value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"),"- [",value.get("status"),"]")

    def issue_books(self):
        books_id= input("Enter a id:")
        current_date= datetime.datetime.now().strftime("%y-%m_%D %h:%m:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["status"]=="Available":
                print(f"This books is already issued to {self.books_dict[books_id]['lender name']} on {self.books_dict[books_id]['issue_date']}")
                return self.issue_books()

            elif self.books_dict[books_id]['status']== "Available":
                your_name=input("enter a name:")
                self.books_dict[books_id]['lender name']=your_name
                self.books_dict[books_id]['issue_date']= current_date
                self.books_dict[books_id]['status'] ="Already issued"
                print("Books issued successfully!!")
        else:
            print("Books id is not found")
            return self.issue_books()

    def add_books(self):
        new_books=input("enter a books:")
        if new_books== " ":
            return self.add_books()
        elif new_books>25:
            print("Books title character are too long, you should enter lesser than 25 characters")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,'lender name':" ",'issue_date':"",'status':"Available"}})
                print(f"This book{new_books} has been added successfully")

    def return_books(self):
        books_id=input("Enter a id:")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["status"]=="Available":
                print("This book is already available in library. soo please check your id!!")
                return self.return_books()
            elif not self.books_dict[books_id]["status"]=="Available":
                self.books_dict[books_id]["lender name"]= " "
                self.books_dict[books_id]["issue_date"]= " "
                self.books_dict[books_id]["status"]="Available"
                print("Successfully return!! \n")
            else:
                print("Book id is not found")
            
try:
    myLMS=LMS("list_of_books.txt","Ashok's")
    press_key_list={"D":"display books","I":"issue books","A":"add books","R":"return books","Q":"quite operation"}
    key_press=False
    while not (key_press=="q"):
        print(f"\n-------welcome to {myLMS.library_name} library management system----------\n")
        for key,value in press_key_list.items():
            print("Press",key,"To",value)
        key_press=input("Press key:").lower()
        if key_press=="i":
            print("\n current suitation: issue books\n")
            myLMS.issue_books()
        elif key_press=="a":
            print("\n current suitation: add books\n")
            myLMS.add_books()
        elif key_press=="d":
            print("\n current suitation: display books\n")
            myLMS.display_books()
        elif key_press=="r":
            print("\n current suitation : return books\n")
            myLMS.return_books()
        elif key_press=="q":
            break
        else:
            continue
except Exception as e:
    print("somthing went wrong.please check your input!!")




