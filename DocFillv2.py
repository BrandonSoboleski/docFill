#from user import openfiles
from tkinter import *
import openfiles
from openfiles import editall
import os
#//////////////////////////////////////////////////////
#GUI                                                  /
#//////////////////////////////////////////////////////
entries = []

fields = 'Name', 'Admission Date', 'Diagnosis'

def fetch(entries):
   args = []
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text))
      args.append(text)
   editall(args)

def makeform(root, fields):
   
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='Fill Documents',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
   
#//////////////////////////////////////////////////////
#Function Calls                                       /
#//////////////////////////////////////////////////////
