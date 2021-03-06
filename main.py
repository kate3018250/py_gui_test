import tkinter as tk
import menubar_function as mf
import sys
import random

class Gui:
    
    def __init__(self):
        self.start_flag = False
        self.msg_len = 0
        self.win=tk.Tk()
        self.message = tk.StringVar()
        self.message.set('')
        self.tmp_str = ''
        self.answer_list = ''
        self.vocabularies = []
        self.correct_answer = tk.StringVar()
        self.correct_answer.set('')
        self.user_answer = tk.StringVar()
        self.user_answer.set('')
        self.hint_variable = tk.StringVar()
        self.hint_variable.set('Hint : ')
        self._SetParameters(self.win)
        self.record = {}

    def _SetParameters(self,win):
        #size title
        win.title("My GRE Trainer")

        # set size 
        win.minsize(1000,450)
        win.maxsize(1400,850)
        win.geometry("1250x450")
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

        correct_label = tk.Label (win , text = 'Your Answers' , font = 'Courier 18 bold' )
        correct_label.place( x = 100 , y = 190)

        incorrect_label = tk.Label (win , text = 'Correct Answers' , font = 'Courier 18 bold')
        incorrect_label.place( x = 480 , y = 190 )
        
        hint_label = tk.Label (win , textvariable = self.hint_variable , font = 'Courier 18 bold')
        hint_label.place(x = 480,y = 70)
        
        #menu

        #entry 
        input_entry  = tk.Entry(win, font = "28" )
        input_entry.place(x = 170 , y = 80)
        input_entry.focus()
        self.win.bind('<Return>',lambda eff:self._get_user_answer(eff,input_entry))

        #button

        btn = tk.Button(win, text = "Start Test", command = self._loadfile,font = "bold" , width = "10" )
        btn.place(x = 10,y = 10)

        next_btn = tk.Button(win, text = "Next", command = self._change_definition, font = "bold" , width = "4" , height = "1")
        next_btn.place(x = 400,y = 70)

        exit_btn = tk.Button(win , text = 'Exit', command = self._exit, font = 'bold' , width = "4" )
        exit_btn.place( x = 900 , y = 380)

        #show correctness
        
        self.show_user_answer = tk.Label(win , width = '40' , height = '9' , font = '16' , textvariable = self.user_answer , anchor = 'n')
        self.show_user_answer.place( x = 30 , y = 240)
 
        self.show_correct_answer = tk.Label(win , fg = 'green' , width = '40' , height = '9' , font = '16' , textvariable = self.correct_answer , anchor = 'n')
        self.show_correct_answer.place ( x = 410 , y = 240)
        
        #History record
        
        record = tk.Button(win , text = "此次答題情形", command = self._show_history , font ="標楷體" , width = "14" , height = "2")
        record.place(x = 1050,y = 70)
    
    def _get_new_win(self):
        tmp_win = tk.Tk()
        tmp_win.geometry("1000x200")
        self.center(tmp_win)
        return tmp_win
        
    def _get_user_answer(self,eff,input_entry):
        if(self.start_flag == False):
            new_win = self._get_new_win()
            start_label = tk.Label (new_win, text = "You haven't load files yet" , font = 'Courier 35 bold' ).pack()           
        self. answer_list += self.answer+'\n'
        self.tmp_str += input_entry.get() + '\n'
        tmp_input_answer = input_entry.get()
        if(self.answer == input_entry.get()):
            self.show_user_answer['fg'] = 'green'
        else:
            self.show_user_answer['fg'] = 'red'
        
        self.correct_answer.set(self.answer_list)
        self.user_answer.set(self.tmp_str)
        self.record[self.answer] = [tmp_input_answer]
        input_entry.delete(0,'end')
        self._change_definition()

    def _show_history(self):
        record = tk.Tk()
        record.title("Record!")
        # set size 
        record.minsize(1000,450)
        record.maxsize(1400,850)
        record.geometry("900x350")
        
        Your_answer = tk.Label(record,text="Your Answer",font ="標楷體")
        Your_answer.place(x = 200 , y = 20)
        Your_answer_list = tk.Label(record , width = '40' , height = '9' , font = '16' , text = self.user_answer.get() , anchor = 'n')
        Your_answer_list.place( x = 50 , y = 50)
        
        Correct_answer = tk.Label(record,text="Correct Answer",font ="標楷體")
        Correct_answer.place(x = 500 , y = 20)
        correct_answer_List = tk.Label(record , fg = 'green' , width = '40' , height = '9' , font = '16' , text = self.correct_answer.get() , anchor = 'n')
        correct_answer_List.place( x = 350 , y = 50)
        
        
        Accuracy = tk.Label(record,text="Accuracy",font ="標楷體 22")
        Accuracy.place( x = 850 , y = 5)
        Accuracy_str = self._calculate_accuracy()
        Accuracy_number = tk.Label(record,text=Accuracy_str,font ="標楷體 22",)
        Accuracy_number.place( x = 850 , y = 50) 
        self.center(record)
        record.mainloop()
        
    def _calculate_accuracy(self):
        cnt = 0
        crt = 0
        for key , value in self.record.items():
            cnt+=1
            if(key == value):
                crt+=1
        return str(crt)+"/"+str(cnt)
        
    def _change_definition(self):
        
        if(self.start_flag == False):
            new_win = self._get_new_win()
            start_label = tk.Label (new_win, text = "You haven't load files yet" , font = 'Courier 35 bold' ).pack()

        index = random.randint(0,(self.msg_len-1))
        self.message.set(self.vocabularies[index][1])
        self.answer = self.vocabularies[index][0] 
        self.hint_variable.set('Hint : '+self.answer[0:2])
    
    def _loadfile(self):
        self.start_flag = True
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
    