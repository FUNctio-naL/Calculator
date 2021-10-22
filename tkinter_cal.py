from tkinter import *

root = Tk()
root.title("So you wanna Calculate...")
root.iconbitmap('C:/Users/Swastik Sharma/Documents/Icon 2/Mirrors-Edge-1.ico')
ins = Entry(root, width=75, fg ="bLUe", highlightthickness= 15)
ins.grid(row=1, column=4)
ind =0; f=-999; s=0
def put(a):
    global ind,s
    if s: ins.delete(0, END)
    ins.insert(ind, a)
    ind+=1; s=0
def cle():
    global ind, f
    ins.delete(0, END)
    ind=0 ; f=-999

def eql():
    global ind
    sum =0; p =''
    l = list(ins.get())
    ins.delete(0, END); 
    y =[]
    for i in l:
        if i == '+': y.append(float(p)); y.append('+')  ; p=''
        elif i == '*': y.append(float(p)); y.append('*'); p=''
        elif i == '-': y.append(float(p)); y.append('-'); p=''
        elif i == '/': y.append(float(p)); y.append('/'); p=''
        else : p+= i
    y.append(float(p))
    sum = y[0]
    for i in range(len(y))[2::2]:
        if y[i-1] == '+' : sum +=float(y[i])
        if y[i-1] == '-' : sum -=float(y[i])
        if y[i-1] == '/' and y[i] : sum /=float(y[i])
        if y[i-1] == '*' : sum *=float(y[i])
    ins.delete(0, END); 
    ins.insert(0, sum)
    return 

def bck():
    global f; global ind
    if ind>0 : ind-=1
    ins.delete(ind, END)
    return 


se7 = Button(root, text=7, padx=30, pady=12, bg="black", fg='#76FF03', command =lambda: put(7))
se7.grid(row=0, column=0)

se8 = Button(root, text=8, padx=30, pady=12, bg="black", fg='#76FF03', command =lambda: put(8))
se8.grid(row=0, column=1)

se9 = Button(root, text=9, padx=30, pady=12,  bg="black", fg='#76FF03',command =lambda: put(9))
se9.grid(row=0, column=2)

se6 = Button(root, text=6, padx=30, pady=12, bg="black", fg='#76FF03', command =lambda: put(6))
se6.grid(row=1, column=2)

se5 = Button(root, text=5, padx=30, pady=12,  bg="black", fg='#76FF03',command =lambda: put(5))
se5.grid(row=1, column=1)
se4 = Button(root, text=4, padx=30, pady=12, bg="black", fg='#76FF03', command =lambda: put(4))
se4.grid(row=1, column=0)

se3 = Button(root, text=3, padx=30, pady=12,  bg="black", fg='#76FF03',command =lambda: put(3))
se3.grid(row=2, column=2)

se2 = Button(root, text=2, padx=30, pady=12, bg="black", fg='#76FF03', command =lambda: put(2))
se2.grid(row=2, column=1)

se1 = Button(root, text=1, padx=30, pady=12, bg="black", fg='#76FF03', command =lambda: put(1))
se1.grid(row=2, column=0)

se0 = Button(root, text=0, padx=30, pady=12, bg="black", fg='#76FF03', command =lambda: put(0))
se0.grid(row=3, column=0)
sec = Button(root, text = "CLEAR" , padx=53,  bg="black", fg='#03A9F4',pady =12, command= cle)
sec.grid(row=3, column=1, columnspan=2)
ad = Button(root, text="+", padx =30, pady=12, bg="black", fg='#E65100', command =lambda: put('+')).grid(row=4, column=0)
ad = Button(root, text="-", padx =30, pady=12,  bg="black", fg='#E65100',command =lambda: put('-')).grid(row=5, column=0)
ad = Button(root, text="/", padx =30, pady=12, bg="black", fg='#E65100', command =lambda: put('/')).grid(row=5, column=1)
ad = Button(root, text="*", padx =30, pady=12,  bg="black", fg='#E65100',command =lambda: put('*')).grid(row=5, column=2)
ad = Button(root, text="<<--", padx =100, pady=12, bg="black", fg='#E65100', command =bck).grid(row=6, column=0, columnspan=3)
eq = Button(root, text = "=", padx =66.5, pady=12, bg="black", fg='#95b8cf', command =eql).grid(row=4,column=1, columnspan=2)

root.mainloop()
