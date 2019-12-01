from tkinter import *
from DLL import *
import copy

dllFirst = DoublyLinkedList()
dllSecond = DoublyLinkedList()

def addToFirst():
    dllFirst.push(int(entry1.get()))

def addToSecond():
    dllSecond.push(int(entry2.get()))

def showFirst():
    show.set(dllFirst.printList(dllFirst.head))

def showSecond():
    show.set(dllSecond.printList(dllSecond.head))
    
def Task(k):
    cursor = k
    dllSecond_copy = copy.deepcopy(dllSecond)
    dllSecond_copy.reverse()
    node_iterator = dllSecond_copy.head
    while node_iterator is not None:
        dllFirst.pushToK(node_iterator.data , cursor)
        node_iterator = node_iterator.next
        cursor += 1

root = Tk()
root.title("Double Linked List")
root.geometry("300x300")

show = StringVar()
entry1 = StringVar()
entry2 = StringVar()

addButton1 = Button(root, text="добавить элемент в 1",command = addToFirst)
addButton1.place(x=0, y=0, width=150, height=50 )

addEntry = Entry(root , textvariable = entry1)
addEntry.place(x=150, y=0, width=150, height=50)
showButton1 = Button(root, text="показать 1-ый список" , command = showFirst )
showButton1.place(x=0, y=50, width=150, height=50)

addButton2 = Button(root, text="добавить элемент в 2" , command = addToSecond)
addButton2.place(x=0, y=100, width=150, height=50)

addEntry = Entry(root , textvariable = entry2)
addEntry.place(x=150, y=100, width=150, height=50)
showButton2 = Button(root, text="показать 2-ой список " , command = showSecond)
showButton2.place(x=0, y=150, width=150, height=50)


showButton = Button(root, text="задание" , command = lambda : Task(1))
showButton.place(x=150, y=150, width=150, height=50)

showLabel = Label(root, textvariable=show)
showLabel.place(x=0, y=300, width=300, height=150)

root.mainloop()
