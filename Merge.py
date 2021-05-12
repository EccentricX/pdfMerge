#Importing needed library

from tkinter import Tk, Button, Menu, Listbox, Label, Frame, messagebox, filedialog, END,ttk,LEFT,BOTTOM,VERTICAL,HORIZONTAL,Y,X
from PyPDF3 import PdfFileWriter, PdfFileReader
from os import listdir, path
from random import choice
pfw=PdfFileWriter()

preference=[]

for d in range(97,97+26):
    preference.append(chr(d))

for d in range(65,65+26):
    preference.append(chr(d))

preference.extend(['1','2','3','4','5','6','7','8','9','10'])

name=choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)

root=Tk()
root.title('Merge PDF')
root.resizable(height=False, width=False)

f1=Frame(root)
f1.pack()

f2=Frame(root)
NoDirLabel=Label(f2,text='*No Directory\nChoosen.',font='times 25 bold')
NoDirLabel.pack()
f2.pack()

f3=Frame(root)
f3.pack()

f4=Frame(root)
f4.pack()

List_1=[]   # Name of PDF Files
List_2=[]   # Name + Location of PDF Files
List_3=[]   # Stream of Selected Files
Position={} # Tracks the position of FILES

selected_or_not=0

#Defination Starts

def getintodir():
    global dir_location
    dir_location=filedialog.askdirectory()
    if dir_location!='' or path.exists(dir_location):
        getpdffiles()
    else:
        pass
    
def getpdffiles():
    global List_1
    global List_2
    for i in listdir(dir_location):
        if i.endswith('.pdf'):
            List_1.append(i)
            List_2.append(dir_location+'/'+i)
    CreateListBox()

Title_label=Label(f1,text='Merge PDF',font='times 20 bold',fg='red',borderwidth=0)
Title_label.pack(pady=5)

Browse_button=Button(f1,text='Browse Directory',font='times 15 bold',command=getintodir,borderwidth=5)
Browse_button.pack()

Exit_button=Button(f4,text='Exit!!',font='times 15 bold',command=root.destroy,borderwidth=5)
Exit_button.pack(pady=5)

def grab_them(event):
    global Position
    ListPDF.itemconfig(ListPDF.curselection(),bg='lightblue')
    Position[ListPDF.index(ListPDF.curselection())]=List_2[ListPDF.index(ListPDF.curselection())]
    ListPDF.selection_clear(0,END)
    global selected_or_not
    selected_or_not+=1

def leave_them(event):
    global Position
    if ListPDF.itemcget(ListPDF.index(ListPDF.curselection()),'bg')=='lightblue':
        Position.pop(ListPDF.index(ListPDF.curselection()))
        ListPDF.itemconfig(ListPDF.curselection(),bg='white')
        ListPDF.selection_clear(0,END)
        global selected_or_not
        selected_or_not-=1
    else:
        grab_them(event)

def CreateListBox():
    global vertical_scroll,horizontal_scroll
    vertical_scroll=ttk.Scrollbar(f2,orient=VERTICAL)
    vertical_scroll.pack(side=LEFT,fill=Y)
    
    horizontal_scroll=ttk.Scrollbar(f2,orient=HORIZONTAL)
    horizontal_scroll.pack(side=BOTTOM,fill=X)
    
    if len(List_2)!=0:
        global ListPDF
        ListPDF=Listbox(f2,width=50,fg='black',font='times 7 bold',highlightthickness=0,borderwidth=0,yscrollcommand=vertical_scroll.set,xscrollcommand=horizontal_scroll.set)
        
        vertical_scroll.config(command=ListPDF.yview)
        horizontal_scroll.config(command=ListPDF.xview)
        
        for i in List_2:
            try:
                PdfFileReader(i)
                ListPDF.insert(END,List_1[List_2.index(i)])
            except:
                List_1.remove(List_1[List_2.index(i)])
                List_2.remove(i)
        ListPDF.pack()
        ListPDF.bind('<<ListboxSelect>>',leave_them)
    else:
        NoDirLabel.config(text='*No Directory\nChoosen.')
    NoDirLabel.config(text='*No Directory\nChoosen.')

def renewthem():
    global ListPDF,vertical_scroll,horizontal_scroll
    ListPDF.destroy()
    vertical_scroll.destroy()
    horizontal_scroll.destroy()

    global List_3
    global List_2
    global List_1

    List_1=[]
    List_2=[]
    List_3=[]

    global name
    name=choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)+choice(preference)

    global selected_or_not
    selected_or_not=0

    global Position
    Position={}

def mergeandsave():

    global Position
    global List_3
    for i in Position:
        List_3.append(PdfFileReader(Position[i]))

    for file in List_3:
        for page in range(file.numPages):
            pageobj=file.getPage(page)
            pfw.addPage(pageobj)
    
    Mergedfile=open(saving_name,'wb')
    pfw.write(Mergedfile)
    Mergedfile.close()
    messagebox.showinfo('Merge Completed!','All desired file merged.')
    renewthem()

def namethefile():
    global saving_name
    if selected_or_not!=0:
    	saving_name=filedialog.asksaveasfilename(initialdir=dir_location,title='Save Merged File',filetypes=[('PDF Files','*.pdf')])
    	if saving_name!='':
        	mergeandsave()
    	else:
            saving_name=dir_location+'/'+name
            mergeandsave()
    else:
    	messagebox.showwarning('Alert!!','No PDF files choosen to be merged,\nclick " BROWSE DIRECTORY "\nfor merging file.')

def helpuser():
    messagebox.showinfo('Help Guide','Hi everyone, This is " KESHAV ABHISHEK "\n\nPresenting a PDF File Merging Bot, this will help you to merge multipe PDF files in just a flash and it\'s pretty to handle..\n\nFor example...\n\n If you have 3 PDF files named 1.pdf, 2.pdf, 3.pdf with pages 1,2,3,......,20 and 21,22,23,......,40 and 41,42,43,......60 respectively,\nthen you will get PDF file as 1,2,3,.......20,21,22,23,......40,41,42,43,......60\n\nHope you enjoyed, if yes use this software..\n\nAny query contact "crystaled2003@gmail.com" .')

#   Function Defination Ends

# Defining the Merge Button
Merge_button=Button(f3,text='Merge',font='times 15 bold',borderwidth=5,command=namethefile,fg='red')
Merge_button.pack(pady=5)

# Define Menu Bar

my_menu=Menu(root)
root.config(menu=my_menu)
help_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label='Option...',menu=help_menu)
help_menu.add_command(label='Help & About',command=helpuser)

root.mainloop()