from tkinter import *
from BST import *

tree = searchTree()

def add():
    tree.create(int(entry.get()))

def showTree():
    show.set(tree.preorder(tree.root))

def Task(level):
    res = ""
    string = ",".join(str(tree.searchAtLevel(tree.root , level)))
    for x in string.split(","):
        if x.isdigit() :
            res += "{} ".format(x)
    show.set(res)
    

root = Tk()
root.title("Search Tree")
root.geometry("300x300")
show = StringVar()
entry = StringVar()



addButton = Button(root, text="добавить элемент" , command = add)
addButton.place(x=0, y=0, width=150, height=50)

addEntry = Entry(root , textvariable = entry)
addEntry.place(x=150, y=0, width=150, height=50)
showButton = Button(root, text="показать дерево" , command = showTree)
showButton.place(x=0, y=50, width=150, height=50)

showButton = Button(root, text="показать на \n заданном уровне"  , command = lambda : Task(2))
showButton.place(x=150, y=50, width=150, height=50)

showLabel = Label(root, textvariable=show)
showLabel.place(x=0, y=100, width=300, height=200)

root.mainloop()
