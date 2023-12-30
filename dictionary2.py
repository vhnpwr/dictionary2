from tkinter import *
from tkinter import messagebox
root=Tk()

root.title("dictionary")
root.geometry("400x600")

list1=["red","blue","green","violet","white"]

dictionary={"name":"vihaan",
            "last_name":"pawar",
            "mother_name":"sanika",
            "father_name":"sachin"
    }

try:
    print(list1[2])
    print(dictionary["name"])
   # print(list1[7])
    print(dictionary["age"])
    
except(KeyError):
    print("error","there is an key error")       
    
except(IndexError):
    messagebox.askokcancel("error","there is an index error")


    
root.mainloop()