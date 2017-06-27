import tkinter as tk
import menubar_function as mf

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
    
win=tk.Tk()

#size title
win.title("My GRE Trainer")

# set size 
win.minsize(1000,450)
win.maxsize(1400,850)
win.geometry("1000x450")
center(win)
#icon
win.iconbitmap('icon.ico')

#Label
label =  tk.Label(win,text="              This is GRE Vocabulary Trainer!",font = "Courier 28")
label.place(x = 0 , y = 10)

word_label = tk.Label(win,text="Word :",font ="Courier 20")
word_label.place(x = 30 , y = 70)

definition_label = tk.Label(win,text="Definition :",font ="Courier 20")
definition_label.place(x = 20 , y = 110)

def_content = 'test'
word_def = tk.Label(win , text = def_content , font = 'Courier 20')
word_def.place( x = 220 ,y = 110 )

correct_label = tk.Label (win , text = 'Correct' , font = 'Courier 22 bold' , bg = 'green')
correct_label.place( x = 100 , y = 190)

incorrect_label = tk.Label (win , text = 'Incorrect' , font = 'Courier 22 bold', bg = 'red')
incorrect_label.place( x = 480 , y = 190 )

#menu

#entry 

input_entry  = tk.Entry(win, font = "28")
input_entry.place(x = 170 , y = 80)

#button

btn = tk.Button(win, text = "Start Test", command = mf.donothing(),font = "bold" , width = "10" )
btn.place(x = 10,y = 0)

next_btn = tk.Button(win, text = "Next", command = mf.donothing(), font = "bold" , width = "4" , height = "1")
next_btn.place(x = 400,y = 70)

exit_btn = tk.Button(win , text = 'Exit', command = mf.donothing(), font = 'bold' , width = "4" )
exit_btn.place( x = 900 , y = 380)

#show correctness

correct_text = tk.Text(win , fg = 'green' , width = '40' , height = '9' , font = '16')

correct_text.place( x = 30 , y = 240)

incorrect_text = tk.Text(win , fg = 'red' , width = '40' , height = '9' , font = '16')
incorrect_text.place ( x = 410 , y = 240)

# execute window
win.mainloop()
