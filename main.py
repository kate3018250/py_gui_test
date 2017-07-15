import tkinter as tk
import menubar_function as mf
import sys
import random

class Gui:
    
    def __init__(self):
        self.msg_len = 0
        self.win=tk.Tk()
        self.message = tk.StringVar()
        self.message.set('')
        self.vocabularies = []
        self.answer = ''
        self._SetParameters(self.win)
        self.correct_text = tk.Text(self.win)
        self.incorrect_text = tk.Text(self.win)

    def _SetParameters(self,win):
        #size title
        win.title("My GRE Trainer")

        # set size 
        win.minsize(1000,450)
        win.maxsize(1400,850)
        win.geometry("1000x450")
        self.center(win)
        #icon
        win.iconbitmap('icon.ico')

        #Label
        label =  tk.Label(win,text="              This is GRE Vocabulary Trainer!",font = "Courier 28")
        label.place(x = 0 , y = 10)

        word_label = tk.Label(win,text="Word :",font ="Courier 20")
        word_label.place(x = 30 , y = 70)

        definition_label = tk.Label(win,text="Definition :",font ="Courier 20")
        definition_label.place(x = 20 , y = 110)
        
        word_def = tk.Label(win , textvariable = self.message , font = 'Courier 20')
        word_def.place( x = 220 ,y = 110 )

        correct_label = tk.Label (win , text = 'Correct' , font = 'Courier 22 bold' , bg = 'green')
        correct_label.place( x = 100 , y = 190)

        incorrect_label = tk.Label (win , text = 'Incorrect' , font = 'Courier 22 bold', bg = 'red')
        incorrect_label.place( x = 480 , y = 190 )

        #menu

        #entry 
        input_entry  = tk.Entry(win, font = "28" )
        input_entry.place(x = 170 , y = 80)
        input_entry.focus()
        self.win.bind('<Return>',lambda eff:self._get_user_answer(eff,input_entry))

        #button

        btn = tk.Button(win, text = "Start Test", command = self._loadfile,font = "bold" , width = "10" )
        btn.place(x = 10,y = 0)

        next_btn = tk.Button(win, text = "Next", command = self._change_definition, font = "bold" , width = "4" , height = "1")
        next_btn.place(x = 400,y = 70)

        exit_btn = tk.Button(win , text = 'Exit', command = self._exit, font = 'bold' , width = "4" )
        exit_btn.place( x = 900 , y = 380)

        #show correctness
        
        self.correct_text = tk.Text(win , fg = 'green' , width = '40' , height = '9' , font = '16')
        self.correct_text.place( x = 30 , y = 240)

        self.incorrect_text = tk.Text(win , fg = 'red' , width = '40' , height = '9' , font = '16')
        self.incorrect_text.place ( x = 410 , y = 240)
    
    def _get_user_answer(self,eff,input_entry):
        user_answer = input_entry.get()
        if(user_answer == self.answer):
            print('y')
            self.correct_text.insert(tk.INSERT,user_answer)
        else:
            print('n')
            self.incorrect_text.insert(tk.INSERT,user_answer)
        
    def _change_definition(self):
        index = random.randint(0,(self.msg_len-1))
        self.message.set(self.vocabularies[index][1])
        self.answer = self.vocabularies[index][0]
    
    def _loadfile(self):
        with open('gre_word_2.txt') as f:
            for line in f:
                split_data = line.split('\t')
                self.vocabularies.append(split_data)
                self.msg_len += 1
        self._change_definition()
         
    def _exit(self):
        sys.exit(0)
        
    def center(self,toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
    